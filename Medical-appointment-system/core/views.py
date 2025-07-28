from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.urls import reverse
from .forms import PatientRegisterForm, LoginForm, AppointmentBookingForm, AppointmentRescheduleForm
from .models import User, Doctor, TimeSlot, Appointment
from django.utils import timezone
import logging

logger = logging.getLogger('clinic')  # type: ignore

# Role checks
def patient_required(view_func):
    return user_passes_test(lambda u: u.is_authenticated and u.role == 'patient', login_url='login')(view_func)

def doctor_required(view_func):
    return user_passes_test(lambda u: u.is_authenticated and u.role == 'doctor', login_url='login')(view_func)

# Registration view
def register(request):
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'patient'
            user.save()
            login(request, user)
            return redirect('patient_dashboard')
    else:
        form = PatientRegisterForm()
    return render(request, 'register.html', {'form': form})

# Login view
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logger.info(f"User login: {user.username} (role: {user.role})")  # type: ignore
            if user and hasattr(user, 'role') and user.role == 'doctor':
                return redirect('doctor_dashboard')
            else:
                return redirect('patient_dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def user_logout(request):
    logout(request)
    return redirect('login')

# Patient dashboard
@login_required
@patient_required
def patient_dashboard(request):
    appointments = Appointment.objects.filter(patient=request.user).order_by('-booking_time')  # type: ignore
    return render(request, 'patient_dashboard.html', {'appointments': appointments})

# Doctor dashboard
@login_required
def doctor_dashboard(request):
    if request.user.role != 'doctor':
        return redirect('login')
    doctor = get_object_or_404(Doctor, user=request.user)
    appointments = Appointment.objects.filter(doctor=doctor).order_by('time_slot__date', 'time_slot__start_time')  # type: ignore
    return render(request, 'doctor_dashboard.html', {'appointments': appointments})

# List doctors
@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()  # type: ignore
    return render(request, 'doctor_list.html', {'doctors': doctors})

# Book appointment
@login_required
@patient_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    available_slots = TimeSlot.objects.filter(doctor=doctor, is_booked=False, date__gte=timezone.now().date()).order_by('date', 'start_time')  # type: ignore
    if request.method == 'POST':
        form = AppointmentBookingForm(request.POST)
        form.fields['doctor'].initial = doctor
        form.fields['time_slot'].queryset = available_slots
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.doctor = doctor
            appointment.save()
            # Mark slot as booked
            slot = appointment.time_slot
            slot.is_booked = True
            slot.save()
            logger.info(f"Appointment booked: patient={request.user.username}, doctor={doctor.user.username}, slot={slot}")  # type: ignore
            # Send confirmation emails
            send_mail(
                'Appointment Confirmation',
                f'Your appointment with {doctor} is confirmed for {slot.date} at {slot.start_time}.',
                'noreply@clinic.com',
                [request.user.email, doctor.user.email],
            )
            return redirect('patient_dashboard')
    else:
        form = AppointmentBookingForm(initial={'doctor': doctor})
        form.fields['doctor'].queryset = Doctor.objects.filter(id=doctor_id)  # type: ignore
        form.fields['time_slot'].queryset = available_slots
    return render(request, 'book.html', {'form': form, 'doctor': doctor, 'available_slots': available_slots})

@login_required
@patient_required
def reschedule_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user)  # type: ignore
    doctor = appointment.doctor
    old_slot = appointment.time_slot
    if request.method == 'POST':
        form = AppointmentRescheduleForm(request.POST, doctor=doctor)
        if form.is_valid():
            new_slot = form.cleaned_data['time_slot']
            if new_slot != old_slot:
                # Free old slot
                old_slot.is_booked = False
                old_slot.save()
                # Book new slot
                new_slot.is_booked = True
                new_slot.save()
                appointment.time_slot = new_slot
                appointment.save()
                logger.info(f"Appointment rescheduled: patient={request.user.username}, doctor={doctor.user.username}, old_slot={old_slot}, new_slot={new_slot}")  # type: ignore
            return redirect('patient_dashboard')
    else:
        form = AppointmentRescheduleForm(doctor=doctor, initial={'time_slot': old_slot})
    return render(request, 'reschedule.html', {'form': form, 'appointment': appointment, 'old_slot': old_slot})

def home(request):
    if request.user.is_authenticated:
        if request.user.role == 'doctor':
            return redirect('doctor_dashboard')
        else:
            return redirect('patient_dashboard')
    # Render a visually appealing homepage for unauthenticated users
    return render(request, 'home.html') 