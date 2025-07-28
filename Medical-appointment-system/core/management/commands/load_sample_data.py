from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta, time
from core.models import User, Doctor, TimeSlot

class Command(BaseCommand):
    help = 'Load sample data for testing'

    def handle(self, *args, **options):
        # Create sample patients
        for i in range(3):
            username = f'patient{i+1}'
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(
                    username=username, 
                    password='testpass123', 
                    email=f'{username}@mail.com', 
                    role='patient',
                    first_name=f'Patient{i+1}',
                    last_name='Test'
                )
                self.stdout.write(f'Created patient: {username}')

        # Create sample doctors with different names
        doctor_names = [
            ('John', 'Doe'),
            ('Emily', 'Clark'),
            ('Michael', 'Brown'),
        ]
        specs = ['Cardiologist', 'Dermatologist', 'Pediatrician']
        for i, (first, last) in enumerate(doctor_names):
            username = f'doctor{i+1}'
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                    username=username, 
                    password='testpass123', 
                    email=f'{username}@mail.com', 
                    role='doctor', 
                    first_name=first, 
                    last_name=last
                )
                Doctor.objects.create(  # type: ignore
                    user=user, 
                    specialization=specs[i], 
                    bio=f'Experienced specialist in {specs[i]}'
                )
                self.stdout.write(f'Created doctor: {username} ({specs[i]})')

        # Create time slots for each doctor
        for doctor in Doctor.objects.all():  # type: ignore
            for d in range(3):
                slot_date = date.today() + timedelta(days=d+1)
                for h in [9, 11, 14]:
                    start = time(hour=h, minute=0)
                    end = time(hour=h+1, minute=0)
                    if not TimeSlot.objects.filter(doctor=doctor, date=slot_date, start_time=start).exists():  # type: ignore
                        TimeSlot.objects.create(  # type: ignore
                            doctor=doctor, 
                            date=slot_date, 
                            start_time=start, 
                            end_time=end
                        )
                        self.stdout.write(f'Created time slot: {doctor} - {slot_date} {start}-{end}')

        self.stdout.write(self.style.SUCCESS('Sample data loaded successfully!'))  # type: ignore 