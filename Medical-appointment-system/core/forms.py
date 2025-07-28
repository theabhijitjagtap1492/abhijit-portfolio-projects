from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Appointment, TimeSlot

class PatientRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass

class AppointmentBookingForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'time_slot']
        widgets = {
            'doctor': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'doctor' in self.initial:
            self.fields['time_slot'].queryset = TimeSlot.objects.filter(doctor=self.initial['doctor'], is_booked=False)  # type: ignore
        else:
            self.fields['time_slot'].queryset = TimeSlot.objects.filter(is_booked=False)  # type: ignore

class AppointmentRescheduleForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['time_slot']

    def __init__(self, *args, **kwargs):
        doctor = kwargs.pop('doctor', None)
        super().__init__(*args, **kwargs)
        if doctor:
            self.fields['time_slot'].queryset = TimeSlot.objects.filter(doctor=doctor, is_booked=False)  # type: ignore
        else:
            self.fields['time_slot'].queryset = TimeSlot.objects.filter(is_booked=False)  # type: ignore 