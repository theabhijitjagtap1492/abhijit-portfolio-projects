# Medical-appointment-system


A comprehensive web-based clinic management system built with Django that allows patients to book appointments with doctors and enables doctors to manage their schedules efficiently.

## 🏥 Features

### For Patients
- **User Registration & Authentication**: Secure patient registration and login system
- **Doctor Discovery**: Browse available doctors with their specializations and bios
- **Appointment Booking**: Book appointments with available time slots
- **Appointment Management**: View, reschedule, and manage existing appointments
- **Dashboard**: Personalized dashboard showing appointment history and upcoming visits

### For Doctors
- **Doctor Dashboard**: View all scheduled appointments and patient information
- **Schedule Management**: Manage available time slots and appointments
- **Patient Information**: Access patient details for scheduled appointments
- **Professional Profile**: Maintain specialization and bio information

### System Features
- **Role-Based Access Control**: Separate interfaces for patients, doctor
- **Responsive Design**: Modern, user-friendly interface
- **Security**: CSRF protection, authentication, and authorization

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite development
- **Frontend**: HTML, CSS, Bootstrap
- **Authentication**: Django's built-in authentication system


## 📋 Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- Git

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-clinic-management.git
   cd django-clinic-management
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 📁 Project Structure

```
django-clinic-management/
├── config/                 # Django project settings
│   ├── settings.py        # Main settings file
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── core/                  # Main application
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   ├── forms.py          # Form definitions
│   ├── urls.py           # URL routing
│   ├── admin.py          # Admin interface configuration
│   └── templates/        # HTML templates
├── manage.py             # Django management script
├── db.sqlite3           # SQLite database
├── clinic.log           # Application logs
├──requirements.txt
```

## 🗄️ Database Models

### User
- Custom user model extending Django's AbstractUser
- Role-based system (patient, doctor, admin)
- Authentication and authorization

### Doctor
- One-to-one relationship with User
- Specialization and bio information
- Professional profile management

### TimeSlot
- Available appointment slots for doctors
- Date, start time, end time, and booking status
- Flexible scheduling system

### Appointment
- Links patients with doctors and time slots
- Booking timestamp and confirmation system
- Appointment history tracking


## 👥 User Roles

### Patient
- Register and create account
- Browse available doctors
- Book appointments
- Manage existing appointments
- View appointment history

### Doctor
- Access doctor dashboard
- View scheduled appointments
- Manage time slots
- Update professional profile




## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



