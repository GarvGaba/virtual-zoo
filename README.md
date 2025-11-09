# Virtual Zoo - Django Web Application

A comprehensive Django web application for exploring virtual ecosystems, learning about animals, and participating in educational sessions with immersive 3D hologram previews.

## Features

- **Role-Based Authentication**: Admin, Teacher, and Student roles with different permissions
- **Ecosystem Explorer**: Browse and explore different ecosystems with detailed information
- **Animal Database**: View animals within ecosystems with scientific information
- **Educational Sessions**: Create and enroll in educational sessions
- **3D Hologram Previews**: Support for hologram preview URLs
- **Responsive Design**: Built with TailwindCSS for modern, mobile-friendly UI
- **CRUD Operations**: Full Create, Read, Update, Delete functionality
- **Admin Interface**: Django admin panel for managing all data

## Technology Stack

- **Backend**: Django 5.2.8
- **Frontend**: TailwindCSS 3.4
- **Database**: SQLite (development) / PostgreSQL (production)
- **Image Handling**: Pillow

## Project Structure

```
virtual_zoo/
├── accounts/          # User authentication and profiles
├── ecosystem/      # Ecosystem and animal models/views
├── educational_sessions/  # Educational session management
├── theme/           # TailwindCSS configuration
└── virtual_zoo/     # Main project settings
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Node.js and npm (for TailwindCSS compilation)

### Installation Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd django
   ```

2. **Create and activate a virtual environment** (if not already created)
   ```bash
   python -m venv myenv
   # On Windows:
   myenv\Scripts\activate
   # On macOS/Linux:
   source myenv/bin/activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install TailwindCSS dependencies**
   ```bash
   cd theme/static_src
   npm install
   cd ../..
   ```

5. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin user.

7. **Build TailwindCSS** (for production)
   ```bash
   cd theme/static_src
   npm run build
   cd ../..
   ```
   
   Or run in watch mode (for development):
   ```bash
   cd theme/static_src
   npm run watch
   ```
   Keep this terminal running while developing.

8. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

9. **Run the development server**
   ```bash
   python manage.py runserver
   ```

10. **Access the application**
    - Main site: http://127.0.0.1:8000/
    - Admin panel: http://127.0.0.1:8000/admin/

## User Roles

### Admin
- Full access to all features
- Can create, edit, and delete ecosystems, animals, and sessions
- Access to Django admin panel

### Teacher
- Can create and manage educational sessions
- Can create and edit ecosystems and animals
- Can view enrolled students in their sessions

### Student
- Can browse ecosystems and view animals
- Can view and enroll in educational sessions
- Can view their profile and enrollment history

## Creating Sample Data

1. **Access the admin panel** at http://127.0.0.1:8000/admin/
2. **Login** with your superuser credentials
3. **Create users** with different roles:
   - Go to Accounts > Users
   - Add users and assign roles (Admin, Teacher, or Student)

4. **Create ecosystems**:
   - Go to Ecosystem > Ecosystems
   - Add ecosystems with descriptions, locations, and climate information
   - Optionally add hologram preview URLs

5. **Add animals**:
   - Go to Ecosystem > Animals
   - Link animals to ecosystems
   - Add scientific names, habitats, and diet information

6. **Create educational sessions**:
   - Go to Educational Sessions > Educational Sessions
   - Assign a teacher
   - Set scheduled date and time
   - Link to an ecosystem (optional)

## Development Notes

### TailwindCSS Development
- For development, run `npm run watch` in `theme/static_src/` to automatically rebuild CSS on changes
- The CSS file is output to `theme/static/css/dist/styles.css`

### Database
- Development uses SQLite by default (no configuration needed)
- For production, update `settings.py` to use PostgreSQL:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'your_db_name',
          'USER': 'your_db_user',
          'PASSWORD': 'your_db_password',
          'HOST': 'localhost',
          'PORT': '5432',
      }
  }
  ```

### Media Files
- Uploaded images are stored in the `media/` directory
- Make sure this directory exists and is writable

## Features Overview

### Ecosystem Explorer
- Browse all available ecosystems
- View detailed ecosystem information
- See animals within each ecosystem
- 3D hologram preview links (when available)

### Educational Sessions
- View upcoming educational sessions
- Filter by session type (Workshop, Lecture, Interactive, Virtual Field Trip)
- Enroll/unenroll in sessions (students)
- View enrollment status and capacity

### User Profiles
- View personal information
- See activity statistics (sessions created/enrolled, ecosystems created)

## Troubleshooting

### Common Issues

1. **TailwindCSS not working**
   - Make sure you've run `npm install` in `theme/static_src/`
   - Run `npm run build` to generate CSS
   - Check that `theme/static/css/dist/styles.css` exists

2. **Static files not loading**
   - Run `python manage.py collectstatic`
   - Check `STATIC_URL` and `STATICFILES_DIRS` in settings.py

3. **Database errors**
   - Run `python manage.py migrate` to apply migrations
   - Check database permissions

4. **Image upload errors**
   - Ensure `media/` directory exists
   - Check file permissions

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please check the Django documentation or create an issue in the project repository.

