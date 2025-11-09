# Virtual Zoo - Project Report

**Project Title:** Virtual Zoo - Immersive 3D Ecosystem Exploration Platform

**Date:** January 2025

**Technology Stack:** Django, PostgreSQL/SQLite, TailwindCSS, Python

---

## Table of Contents

1. INTRODUCTION ...................................................................................................................................................1
   1.1 PURPOSE ...................................................................................................................................................................................................1
   1.2 SCOPE ........................................................................................................................................................................................................1
   1.3 DEFINITIONS, ACRONYMS, AND ABBREVIATIONS.......................................................................................................................2
   1.4 OVERVIEW................................................................................................................................................................................................2

2. GENERAL DESCRIPTION...................................................................................................................................3
   2.1 PRODUCT PERSPECTIVE .......................................................................................................................................................................3
   2.2 PRODUCT FUNCTIONS...........................................................................................................................................................................3
   2.3 USER CHARACTERISTICS .....................................................................................................................................................................4
   2.4 GENERAL CONSTRAINTS......................................................................................................................................................................4
   2.5 ASSUMPTIONS AND DEPENDENCIES.................................................................................................................................................4

3. SPECIFIC REQUIREMENTS...............................................................................................................................5
   3.1 EXTERNAL INTERFACE REQUIREMENTS .........................................................................................................................................5
      3.1.1 User Interfaces............................................................................................................................................5
      3.1.2 Hardware Interfaces ...................................................................................................................................5
      3.1.3 Software Interfaces......................................................................................................................................5
      3.1.4 Communications Interfaces.........................................................................................................................5
   3.2 Functional REQUIREMENTS ...............................................................................................................................................................5
   3.3 NON-FUNCTIONAL REQUIREMENT ............................................................................................................................................................................. 6
   3.4 DESIGN CONSTRAINTS .........................................................................................................................................................................7
   3.5 DJANGO AND DATABASE FEATURES.................................................................................................................................................................8

4. SCREENSHOTS OF WEBSITE............................................................................................................................9
   4.1 HOME PAGE......................................................................................................................................................9
   4.2 ECOSYSTEM EXPLORER..................................................................................................................................9
   4.3 LOGIN/REGISTRATION PAGE...................................................................................................................................................10
   4.4 EDUCATIONAL SESSIONS............................................................................................................................................10
   4.5 USER DASHBOARDS.................................................................................................................................11

5. SCREENSHOTS OF CODE.................................................................................................................................12

6. SCREENSHOTS OF DATABASE SCHEMA...........................................................................14

7. PROJECT STRUCTURE AND DEPLOYMENT..................................................................................................................................................... 15

---

## 1. INTRODUCTION

### 1.1 PURPOSE

This document provides a comprehensive description of the Virtual Zoo web application, an immersive educational platform designed for exploring ecosystems, learning about animals, and participating in educational sessions. The purpose of this report is to document the system's requirements, design, implementation, and functionality.

The Virtual Zoo platform serves as an educational tool that allows students, teachers, and administrators to interact with virtual ecosystems, view detailed information about various species, and participate in structured learning sessions.

### 1.2 SCOPE

The Virtual Zoo application encompasses the following scope:

- **Ecosystem Management**: Creation, viewing, and management of various ecosystems (Amazon Rainforest, Sahara Desert, Arctic Tundra, etc.)
- **Animal Database**: Comprehensive database of existing and extinct species with detailed information
- **Educational Sessions**: Video-based learning sessions with quizzes, comments, and downloadable resources
- **User Management**: Role-based access control for Admin, Teacher, and Student users
- **Progress Tracking**: Student progress tracking for visited ecosystems and attended sessions
- **Content Management**: Admin and teacher panels for content creation and management

**Out of Scope:**
- Real-time 3D rendering (uses placeholder/preview system)
- Payment processing
- Mobile native applications (web-responsive only)
- Social media integration

### 1.3 DEFINITIONS, ACRONYMS, AND ABBREVIATIONS

- **Django**: High-level Python web framework
- **PostgreSQL/SQLite**: Database management systems
- **TailwindCSS**: Utility-first CSS framework
- **CRUD**: Create, Read, Update, Delete operations
- **ORM**: Object-Relational Mapping
- **MVC**: Model-View-Controller architecture pattern
- **REST**: Representational State Transfer
- **API**: Application Programming Interface
- **URL**: Uniform Resource Locator
- **HTML**: HyperText Markup Language
- **CSS**: Cascading Style Sheets
- **JS**: JavaScript

### 1.4 OVERVIEW

This document is organized into seven main sections:

1. **Introduction**: Purpose, scope, and overview
2. **General Description**: Product perspective, functions, user characteristics
3. **Specific Requirements**: Interface requirements, functional and non-functional requirements
4. **Website Screenshots**: Visual documentation of the application
5. **Code Screenshots**: Key implementation details
6. **Database Schema**: Database structure and relationships
7. **Project Structure**: Deployment and repository information

---

## 2. GENERAL DESCRIPTION

### 2.1 PRODUCT PERSPECTIVE

The Virtual Zoo is a standalone web application built using Django framework. It operates as an educational platform that can be deployed on any web server supporting Python and Django. The system integrates with:

- **Database**: PostgreSQL (production) or SQLite (development)
- **Static Files**: TailwindCSS for styling
- **Media Storage**: Local file system for images and documents
- **Video Hosting**: External services (YouTube, Vimeo) for educational videos

The application follows a three-tier architecture:
- **Presentation Layer**: Django templates with TailwindCSS
- **Business Logic Layer**: Django views and forms
- **Data Layer**: Django ORM with PostgreSQL/SQLite

### 2.2 PRODUCT FUNCTIONS

The Virtual Zoo platform provides the following core functions:

#### 2.2.1 Ecosystem Explorer
- Browse ecosystems by region (Amazon, Sahara, Arctic, etc.)
- Filter ecosystems by era (Jurassic, Cretaceous, Present Day, etc.)
- Search ecosystems by name, location, or description
- View detailed ecosystem information including:
  - Environmental data (temperature, precipitation, vegetation)
  - Associated animal species
  - High-quality images

#### 2.2.2 Animal Database
- View comprehensive animal information
- Filter by species type (Existing/Extinct)
- Search functionality
- Conservation status tracking
- Scientific classification data

#### 2.2.3 Educational Sessions
- Video-based learning sessions
- Session enrollment system
- Downloadable resources (PDFs, notes)
- Interactive quizzes
- Comment system for engagement
- Lesson content integration

#### 2.2.4 User Management
- Role-based authentication (Admin, Teacher, Student)
- User registration and login
- Profile management
- Student progress tracking
- Teacher dashboard for session management

#### 2.2.5 Content Management
- Admin panel for ecosystem/animal creation
- Teacher panel for session management
- Image upload and management
- Video URL integration

### 2.3 USER CHARACTERISTICS

The system serves three distinct user roles:

#### 2.3.1 Administrators
- Full system access
- Can create/edit/delete ecosystems and animals
- User management capabilities
- System configuration access

#### 2.3.2 Teachers
- Create and manage educational sessions
- Upload resources and create quizzes
- View student enrollments
- Moderate comments

#### 2.3.3 Students
- Browse ecosystems and animals
- Enroll in educational sessions
- Track learning progress
- Access downloadable resources
- Participate in quizzes and discussions

### 2.4 GENERAL CONSTRAINTS

- **Browser Compatibility**: Modern browsers (Chrome, Firefox, Safari, Edge)
- **Network**: Requires internet connection for video playback
- **Storage**: Local file storage for uploaded media
- **Performance**: Optimized for desktop, tablet, and mobile devices
- **Security**: Django's built-in security features (CSRF protection, SQL injection prevention)

### 2.5 ASSUMPTIONS AND DEPENDENCIES

**Assumptions:**
- Users have basic web browsing knowledge
- Video content hosted on external platforms (YouTube/Vimeo)
- Images are provided or downloaded from external sources
- Database server is accessible and properly configured

**Dependencies:**
- Python 3.8+
- Django 4.2+
- PostgreSQL 12+ (production) or SQLite (development)
- Node.js and npm (for TailwindCSS compilation)
- Web server (for production deployment)

---

## 3. SPECIFIC REQUIREMENTS

### 3.1 EXTERNAL INTERFACE REQUIREMENTS

#### 3.1.1 User Interfaces

The application provides a modern, responsive web interface with:

- **Homepage**: Hero section with gradient background, featured ecosystems, and upcoming sessions
- **Navigation Bar**: Persistent navigation with role-based menu items
- **Ecosystem List**: Grid layout with filtering and search capabilities
- **Ecosystem Detail**: Comprehensive information display with animal listings
- **Session Detail**: Video player, resources, quizzes, and comments
- **User Dashboards**: Role-specific dashboards with relevant information
- **Forms**: TailwindCSS-styled forms for all CRUD operations

**Design Principles:**
- Responsive design (mobile-first approach)
- Modern gradient color schemes
- Intuitive navigation
- Accessible color contrasts
- Smooth animations and transitions

#### 3.1.2 Hardware Interfaces

- **Server Requirements:**
  - Minimum 2GB RAM
  - 10GB storage space
  - Network connectivity

- **Client Requirements:**
  - Modern web browser
  - Internet connection
  - JavaScript enabled

#### 3.1.3 Software Interfaces

- **Backend:**
  - Django 4.2+ framework
  - Python 3.8+ runtime
  - Database: PostgreSQL or SQLite

- **Frontend:**
  - TailwindCSS 3.0+
  - HTML5
  - JavaScript (vanilla)

- **External Services:**
  - YouTube/Vimeo API (for video embedding)
  - Image hosting (Unsplash, local storage)

#### 3.1.4 Communications Interfaces

- **HTTP/HTTPS**: Standard web protocols
- **RESTful URLs**: Clean URL structure
- **AJAX**: For dynamic content loading (if implemented)

### 3.2 Functional REQUIREMENTS

#### FR1: User Authentication
- **FR1.1**: Users can register with username, email, password, and role
- **FR1.2**: Users can log in with credentials
- **FR1.3**: Users can log out securely
- **FR1.4**: Password validation and security

#### FR2: Ecosystem Management
- **FR2.1**: View list of all ecosystems with pagination
- **FR2.2**: Filter ecosystems by region, era, and search query
- **FR2.3**: View detailed ecosystem information
- **FR2.4**: Admin/Teacher can create, edit, and delete ecosystems
- **FR2.5**: Upload and display ecosystem images

#### FR3: Animal Management
- **FR3.1**: View animals associated with ecosystems
- **FR3.2**: Filter animals by species type (existing/extinct)
- **FR3.3**: View detailed animal information
- **FR3.4**: Admin/Teacher can create, edit, and delete animals
- **FR3.5**: Display animal images and conservation status

#### FR4: Educational Sessions
- **FR4.1**: View list of available sessions
- **FR4.2**: View session details with embedded video player
- **FR4.3**: Students can enroll/unenroll in sessions
- **FR4.4**: Teachers can create, edit, and delete sessions
- **FR4.5**: Upload and download session resources
- **FR4.6**: Interactive quizzes with multiple choice questions
- **FR4.7**: Comment system for session discussions

#### FR5: Progress Tracking
- **FR5.1**: Track student visits to ecosystems
- **FR5.2**: Track student attendance in sessions
- **FR5.3**: Display progress statistics in student dashboard
- **FR5.4**: Time spent tracking for learning analytics

#### FR6: Content Management
- **FR6.1**: Admin panel for system management
- **FR6.2**: Teacher dashboard for session management
- **FR6.3**: Image upload and management
- **FR6.4**: Video URL integration (YouTube/Vimeo)

### 3.3 NON-FUNCTIONAL REQUIREMENT

#### NFR1: Performance
- Page load time: < 2 seconds
- Database queries optimized with proper indexing
- Image optimization for faster loading
- Pagination for large datasets

#### NFR2: Usability
- Intuitive navigation
- Responsive design for all devices
- Clear visual hierarchy
- Accessible color schemes
- User-friendly error messages

#### NFR3: Security
- CSRF protection enabled
- SQL injection prevention (Django ORM)
- XSS protection
- Secure password hashing
- Role-based access control

#### NFR4: Reliability
- Error handling and logging
- Database transaction management
- Graceful degradation for missing media
- Backup and recovery procedures

#### NFR5: Maintainability
- Clean code structure
- Comprehensive documentation
- Modular design
- Follows Django best practices

#### NFR6: Scalability
- Database indexing for performance
- Efficient query optimization
- Support for multiple concurrent users
- Media file organization

### 3.4 DESIGN CONSTRAINTS

#### 3.4.1 Technology Constraints
- Must use Django framework
- Python 3.8+ required
- PostgreSQL or SQLite database
- TailwindCSS for styling

#### 3.4.2 Platform Constraints
- Web-based application (no native mobile apps)
- Requires modern browser support
- JavaScript must be enabled

#### 3.4.3 Development Constraints
- Follows Django project structure
- Uses Django's built-in admin interface
- Template inheritance for consistency
- Static file management through Django

### 3.5 DJANGO AND DATABASE FEATURES

#### 3.5.1 Django Framework Features
- **ORM (Object-Relational Mapping)**: Database abstraction layer
- **Admin Interface**: Built-in content management
- **Template System**: Django template language
- **Form Handling**: Django forms with validation
- **Authentication**: Built-in user authentication system
- **Middleware**: Security and session management
- **URL Routing**: Clean URL patterns
- **Migrations**: Database schema version control

#### 3.5.2 Database Features

**Models Implemented:**

1. **User Model** (Custom)
   - Role-based user system (Admin, Teacher, Student)
   - Additional fields: phone_number, bio
   - Extends Django's AbstractUser

2. **Ecosystem Model**
   - Name, description, location
   - Region and era classification
   - Environmental data (temperature, precipitation, vegetation)
   - Image upload support
   - Created by tracking

3. **Animal Model**
   - Name, scientific name
   - Species type (existing/extinct)
   - Conservation status
   - Habitat and diet information
   - Image upload support
   - Foreign key to Ecosystem

4. **EducationalSession Model**
   - Title, description, session type
   - Teacher assignment
   - Scheduled date and duration
   - Video URL integration
   - Lesson content
   - Image upload support

5. **SessionResource Model**
   - File uploads (PDFs, documents)
   - Title and description
   - Associated with sessions

6. **SessionComment Model**
   - User comments on sessions
   - Timestamp tracking

7. **SessionQuiz Model**
   - Multiple choice questions
   - Options and correct answers
   - Explanations

8. **SessionEnrollment Model**
   - Student enrollment tracking
   - Attendance status

9. **StudentProgress Model**
   - Tracks ecosystem visits
   - Tracks session attendance
   - Time spent tracking

**Database Relationships:**
- User → Ecosystem (created_by)
- Ecosystem → Animal (one-to-many)
- User → EducationalSession (teacher)
- Ecosystem → EducationalSession (optional)
- EducationalSession → SessionResource (one-to-many)
- EducationalSession → SessionComment (one-to-many)
- EducationalSession → SessionQuiz (one-to-many)
- EducationalSession → SessionEnrollment (one-to-many)
- User → StudentProgress (one-to-many)

---

## 4. SCREENSHOTS OF WEBSITE

### 4.1 HOME PAGE

**Description:** The homepage features a modern hero section with gradient background (emerald to teal to cyan), animated floating animal icons, and three prominent action buttons. Below the hero section are featured ecosystems and upcoming educational sessions displayed in card layouts.

**Key Elements:**
- Welcome message with "Virtual Zoo" branding
- Three purple action buttons: "Explore Ecosystems", "View Sessions", and "My Dashboard/Teacher Panel"
- Featured Ecosystems section with image cards
- Upcoming Sessions section with session cards
- Responsive navigation bar

**Note:** Screenshots should be captured showing:
- Full hero section with gradient background
- Featured ecosystems grid
- Upcoming sessions display
- Responsive design on different screen sizes

### 4.2 ECOSYSTEM EXPLORER

**Description:** The ecosystem explorer provides a comprehensive interface for browsing and filtering ecosystems.

**Key Features:**
- Filter by region (Amazon, Sahara, Arctic, etc.)
- Filter by era (Jurassic, Cretaceous, Present Day, etc.)
- Search functionality
- Grid layout with ecosystem cards
- Each card shows: image, name, region, era, description preview

**Detail Page Features:**
- Large ecosystem image header
- Environmental information (temperature, precipitation, vegetation)
- Associated animals list with filtering
- Animal cards with images and details

**Note:** Screenshots should show:
- Ecosystem list page with filters
- Ecosystem detail page
- Animal listings
- Filter functionality in action

### 4.3 LOGIN/REGISTRATION PAGE

**Description:** Clean, user-friendly authentication pages with TailwindCSS styling.

**Login Page:**
- Username and password fields
- "Remember me" option
- Link to registration page
- Error message display

**Registration Page:**
- Username, email, password fields
- Role selection (Admin, Teacher, Student)
- Additional fields: first name, last name, phone, bio
- Form validation

**Note:** Screenshots should capture:
- Login form
- Registration form
- Success/error messages
- Form validation states

### 4.4 EDUCATIONAL SESSIONS

**Description:** Comprehensive session management and viewing interface.

**Session List Page:**
- Grid layout of session cards
- Session type badges
- Teacher information
- Enrollment status
- Scheduled dates

**Session Detail Page:**
- Video player (YouTube/Vimeo embed)
- Session description and details
- Enrollment button
- Downloadable resources section
- Quiz section
- Comments section
- Lesson content display

**Note:** Screenshots should show:
- Session list with cards
- Video player in action
- Resources download section
- Quiz interface
- Comments section

### 4.5 USER DASHBOARDS

**Student Dashboard:**
- Visited ecosystems count
- Enrolled sessions count
- Learning time statistics
- List of visited ecosystems
- List of enrolled sessions
- Progress tracking

**Teacher Dashboard:**
- Created sessions list
- Enrollment statistics
- Session management options
- Resource management
- Student engagement metrics

**Note:** Screenshots should capture:
- Student dashboard layout
- Teacher dashboard layout
- Progress statistics
- Session management interface

---

## 5. SCREENSHOTS OF CODE

### 5.1 Model Definitions

**File:** `ecosystem/models.py`

```python
class Ecosystem(models.Model):
    REGION_CHOICES = [
        ('amazon', 'Amazon Rainforest'),
        ('sahara', 'Sahara Desert'),
        ('arctic', 'Arctic Tundra'),
        # ... more choices
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    region = models.CharField(max_length=50, choices=REGION_CHOICES)
    era = models.CharField(max_length=50, choices=ERA_CHOICES)
    temperature_min = models.DecimalField(max_digits=5, decimal_places=2)
    temperature_max = models.DecimalField(max_digits=5, decimal_places=2)
    vegetation = models.TextField(blank=True)
    precipitation = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='ecosystems/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### 5.2 View Functions

**File:** `ecosystem/views.py`

```python
def ecosystem_list(request):
    ecosystems = Ecosystem.objects.all()
    
    # Filtering logic
    region_filter = request.GET.get('region')
    era_filter = request.GET.get('era')
    search_query = request.GET.get('search')
    
    if region_filter:
        ecosystems = ecosystems.filter(region=region_filter)
    if era_filter:
        ecosystems = ecosystems.filter(era=era_filter)
    if search_query:
        ecosystems = ecosystems.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    paginator = Paginator(ecosystems, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'ecosystem/list.html', {
        'page_obj': page_obj,
        'region_filter': region_filter,
        'era_filter': era_filter,
        'search_query': search_query,
    })
```

### 5.3 Form Definitions

**File:** `ecosystem/forms.py`

```python
class EcosystemForm(forms.ModelForm):
    class Meta:
        model = Ecosystem
        fields = ['name', 'description', 'location', 'region', 'era', 
                  'climate', 'temperature_min', 'temperature_max', 
                  'vegetation', 'precipitation', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg'
            }),
            # ... more widgets
        }
```

### 5.4 URL Configuration

**File:** `virtual_zoo/urls.py`

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('ecosystem/', include('ecosystem.urls')),
    path('sessions/', include('educational_sessions.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

### 5.5 Template Example

**File:** `ecosystem/templates/ecosystem/list.html`

```django
{% extends 'base.html' %}

{% block content %}
<div class="max-w-7xl mx-auto">
    <h1 class="text-4xl font-bold mb-6">Ecosystems</h1>
    
    <!-- Filter Form -->
    <form method="get" class="mb-6">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <select name="region" class="...">
                <option value="">All Regions</option>
                {% for value, label in region_choices %}
                    <option value="{{ value }}">{{ label }}</option>
                {% endfor %}
            </select>
            <!-- More filters -->
        </div>
    </form>
    
    <!-- Ecosystem Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        {% for ecosystem in page_obj %}
            <div class="bg-white rounded-lg shadow-lg">
                <!-- Ecosystem card content -->
            </div>
        {% endfor %}
    </div>
</div>
{% endblock %}
```

---

## 6. SCREENSHOTS OF DATABASE SCHEMA

### 6.1 Entity Relationship Diagram

**Main Entities:**
- User (Admin, Teacher, Student)
- Ecosystem
- Animal
- EducationalSession
- SessionResource
- SessionComment
- SessionQuiz
- SessionEnrollment
- StudentProgress

**Relationships:**
- User 1:N Ecosystem (created_by)
- Ecosystem 1:N Animal
- User 1:N EducationalSession (teacher)
- Ecosystem 1:N EducationalSession (optional)
- EducationalSession 1:N SessionResource
- EducationalSession 1:N SessionComment
- EducationalSession 1:N SessionQuiz
- EducationalSession 1:N SessionEnrollment
- User 1:N StudentProgress

### 6.2 Database Tables

**accounts_user:**
- id, username, email, password, role, phone_number, bio, created_at, updated_at

**ecosystem_ecosystem:**
- id, name, description, location, region, era, climate, temperature_min, temperature_max, vegetation, precipitation, image, created_by_id, created_at, updated_at

**ecosystem_animal:**
- id, ecosystem_id, name, scientific_name, species_type, description, habitat, diet, conservation_status, image, created_at, updated_at

**educational_sessions_educationalsession:**
- id, title, description, session_type, teacher_id, ecosystem_id, scheduled_date, duration_minutes, max_students, image, video_url, lesson_content, created_at, updated_at

**educational_sessions_sessionresource:**
- id, session_id, title, file, description, uploaded_at

**educational_sessions_sessioncomment:**
- id, session_id, user_id, content, created_at, updated_at

**educational_sessions_sessionquiz:**
- id, session_id, question, option_a, option_b, option_c, option_d, correct_answer, explanation, created_at

**educational_sessions_sessionenrollment:**
- id, session_id, student_id, enrolled_at, attended, notes

**accounts_studentprogress:**
- id, student_id, ecosystem_id, session_id, visited_at, time_spent_minutes, completed

**Note:** Screenshots should show:
- Database schema diagram
- Table structures
- Foreign key relationships
- Index definitions

---

## 7. PROJECT STRUCTURE AND DEPLOYMENT

### 7.1 Project Structure

```
virtual_zoo/
├── accounts/              # User management app
│   ├── models.py         # User and StudentProgress models
│   ├── views.py          # Authentication and dashboard views
│   ├── forms.py          # Registration form
│   └── templates/        # User-related templates
├── ecosystem/            # Ecosystem management app
│   ├── models.py         # Ecosystem and Animal models
│   ├── views.py          # CRUD operations for ecosystems
│   ├── forms.py          # Ecosystem and Animal forms
│   ├── templates/        # Ecosystem templates
│   └── management/       # Management commands
├── educational_sessions/ # Educational sessions app
│   ├── models.py         # Session, Resource, Comment, Quiz models
│   ├── views.py          # Session management views
│   ├── forms.py          # Session forms
│   └── templates/        # Session templates
├── virtual_zoo/          # Main project directory
│   ├── settings.py       # Django settings
│   ├── urls.py           # Main URL configuration
│   └── templates/        # Base templates
├── theme/                # TailwindCSS theme
├── media/                # Uploaded media files
├── static/               # Static files
└── manage.py            # Django management script
```

### 7.2 Installation and Setup

**Requirements:**
- Python 3.8+
- Django 4.2+
- PostgreSQL 12+ (production) or SQLite (development)
- Node.js and npm (for TailwindCSS)

**Installation Steps:**

1. Create virtual environment:
```bash
python -m venv myenv
myenv\Scripts\activate  # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create superuser:
```bash
python manage.py createsuperuser
```

5. Setup TailwindCSS:
```bash
python manage.py tailwind install
python manage.py tailwind build
```

6. Create demo data:
```bash
python manage.py create_demo_data
```

7. Run development server:
```bash
python manage.py runserver
```

### 7.3 Deployment Considerations

- **Production Database**: Use PostgreSQL instead of SQLite
- **Static Files**: Collect and serve through web server or CDN
- **Media Files**: Store in cloud storage (AWS S3, etc.) for production
- **Security**: Set DEBUG=False, configure ALLOWED_HOSTS
- **Web Server**: Use Gunicorn with Nginx
- **HTTPS**: Enable SSL certificates
- **Backup**: Regular database backups

### 7.4 GitHub Repository

**Repository Structure:**
- Main branch: Production-ready code
- Development branch: Feature development
- README.md: Setup instructions
- requirements.txt: Python dependencies
- .gitignore: Excluded files (media, __pycache__, etc.)

**Note:** Include GitHub repository link in the actual PDF report.

---

## APPENDIX

### A. Technology Versions
- Python: 3.8+
- Django: 4.2+
- TailwindCSS: 3.0+
- PostgreSQL: 12+ (production)
- SQLite: 3.x (development)

### B. Key Dependencies
- django: Web framework
- django-tailwind: TailwindCSS integration
- django-browser-reload: Development hot reload
- psycopg2-binary: PostgreSQL adapter
- Pillow: Image processing
- requests: HTTP library

### C. Browser Support
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

---

**End of Report**

