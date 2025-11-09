"""
Enhanced PDF Report Generator for Virtual Zoo Project
Creates a comprehensive PDF report matching the requested format
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted, Table, TableStyle, KeepTogether
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import re
from datetime import datetime

def clean_markdown(text):
    """Clean markdown formatting"""
    # Remove markdown code blocks
    text = re.sub(r'```[\s\S]*?```', '', text)
    # Remove inline code
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # Remove bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Remove italic
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    # Remove links but keep text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    return text.strip()

def generate_pdf():
    """Generate comprehensive PDF report"""
    doc = SimpleDocTemplate(
        "Virtual_Zoo_Project_Report.pdf",
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    story = []
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=colors.HexColor('#000000'),
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading1_style = ParagraphStyle(
        'Heading1',
        parent=styles['Heading1'],
        fontSize=14,
        textColor=colors.HexColor('#000000'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold',
        keepWithNext=1
    )
    
    heading2_style = ParagraphStyle(
        'Heading2',
        parent=styles['Heading2'],
        fontSize=12,
        textColor=colors.HexColor('#000000'),
        spaceAfter=8,
        spaceBefore=10,
        fontName='Helvetica-Bold',
        leftIndent=0.5*cm
    )
    
    heading3_style = ParagraphStyle(
        'Heading3',
        parent=styles['Heading3'],
        fontSize=11,
        textColor=colors.HexColor('#000000'),
        spaceAfter=6,
        spaceBefore=8,
        fontName='Helvetica-Bold',
        leftIndent=1*cm
    )
    
    normal_style = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#000000'),
        spaceAfter=6,
        alignment=TA_JUSTIFY,
        leading=14,
        leftIndent=0,
        rightIndent=0
    )
    
    code_style = ParagraphStyle(
        'Code',
        parent=styles['Code'],
        fontSize=9,
        fontName='Courier',
        leftIndent=0.5*cm,
        rightIndent=0.5*cm,
        backColor=colors.HexColor('#f5f5f5'),
        borderColor=colors.HexColor('#cccccc'),
        borderWidth=1,
        borderPadding=5,
        spaceAfter=8
    )
    
    # Title Page
    story.append(Spacer(1, 3*inch))
    story.append(Paragraph("VIRTUAL ZOO", title_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Immersive 3D Ecosystem Exploration Platform", 
                        ParagraphStyle('Subtitle', parent=styles['Normal'], fontSize=14, alignment=TA_CENTER)))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Project Report", 
                        ParagraphStyle('Subtitle', parent=styles['Normal'], fontSize=12, alignment=TA_CENTER)))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(f"Date: {datetime.now().strftime('%B %Y')}", 
                        ParagraphStyle('Date', parent=styles['Normal'], fontSize=11, alignment=TA_CENTER)))
    story.append(PageBreak())
    
    # Table of Contents
    story.append(Paragraph("Table of Contents", heading1_style))
    story.append(Spacer(1, 0.3*inch))
    
    toc_data = [
        ["1.", "INTRODUCTION", "1"],
        ["", "1.1 PURPOSE", "1"],
        ["", "1.2 SCOPE", "1"],
        ["", "1.3 DEFINITIONS, ACRONYMS, AND ABBREVIATIONS", "2"],
        ["", "1.4 OVERVIEW", "2"],
        ["2.", "GENERAL DESCRIPTION", "3"],
        ["", "2.1 PRODUCT PERSPECTIVE", "3"],
        ["", "2.2 PRODUCT FUNCTIONS", "3"],
        ["", "2.3 USER CHARACTERISTICS", "4"],
        ["", "2.4 GENERAL CONSTRAINTS", "4"],
        ["", "2.5 ASSUMPTIONS AND DEPENDENCIES", "4"],
        ["3.", "SPECIFIC REQUIREMENTS", "5"],
        ["", "3.1 EXTERNAL INTERFACE REQUIREMENTS", "5"],
        ["", "3.2 FUNCTIONAL REQUIREMENTS", "5"],
        ["", "3.3 NON-FUNCTIONAL REQUIREMENT", "6"],
        ["", "3.4 DESIGN CONSTRAINTS", "7"],
        ["", "3.5 DJANGO AND DATABASE FEATURES", "8"],
        ["4.", "SCREENSHOTS OF WEBSITE", "9"],
        ["", "4.1 HOME PAGE", "9"],
        ["", "4.2 ECOSYSTEM EXPLORER", "9"],
        ["", "4.3 LOGIN/REGISTRATION PAGE", "10"],
        ["", "4.4 EDUCATIONAL SESSIONS", "10"],
        ["", "4.5 USER DASHBOARDS", "11"],
        ["5.", "SCREENSHOTS OF CODE", "12"],
        ["6.", "SCREENSHOTS OF DATABASE SCHEMA", "14"],
        ["7.", "PROJECT STRUCTURE AND DEPLOYMENT", "15"],
    ]
    
    toc_table = Table(toc_data, colWidths=[0.5*cm, 14*cm, 2*cm])
    toc_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('ALIGN', (2, 0), (2, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(toc_table)
    story.append(PageBreak())
    
    # Section 1: INTRODUCTION
    story.append(Paragraph("1. INTRODUCTION", heading1_style))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("1.1 PURPOSE", heading2_style))
    story.append(Paragraph(
        "This document provides a comprehensive description of the Virtual Zoo web application, "
        "an immersive educational platform designed for exploring ecosystems, learning about animals, "
        "and participating in educational sessions. The purpose of this report is to document the system's "
        "requirements, design, implementation, and functionality.",
        normal_style
    ))
    story.append(Paragraph(
        "The Virtual Zoo platform serves as an educational tool that allows students, teachers, and "
        "administrators to interact with virtual ecosystems, view detailed information about various species, "
        "and participate in structured learning sessions.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("1.2 SCOPE", heading2_style))
    story.append(Paragraph("The Virtual Zoo application encompasses the following scope:", normal_style))
    
    scope_items = [
        "<b>Ecosystem Management:</b> Creation, viewing, and management of various ecosystems (Amazon Rainforest, Sahara Desert, Arctic Tundra, etc.)",
        "<b>Animal Database:</b> Comprehensive database of existing and extinct species with detailed information",
        "<b>Educational Sessions:</b> Video-based learning sessions with quizzes, comments, and downloadable resources",
        "<b>User Management:</b> Role-based access control for Admin, Teacher, and Student users",
        "<b>Progress Tracking:</b> Student progress tracking for visited ecosystems and attended sessions",
        "<b>Content Management:</b> Admin and teacher panels for content creation and management"
    ]
    
    for item in scope_items:
        story.append(Paragraph(f"• {item}", normal_style))
        story.append(Spacer(1, 0.05*inch))
    
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("1.3 DEFINITIONS, ACRONYMS, AND ABBREVIATIONS", heading2_style))
    
    definitions = [
        ("Django", "High-level Python web framework"),
        ("PostgreSQL/SQLite", "Database management systems"),
        ("TailwindCSS", "Utility-first CSS framework"),
        ("CRUD", "Create, Read, Update, Delete operations"),
        ("ORM", "Object-Relational Mapping"),
        ("MVC", "Model-View-Controller architecture pattern"),
        ("REST", "Representational State Transfer"),
        ("API", "Application Programming Interface"),
        ("URL", "Uniform Resource Locator"),
        ("HTML", "HyperText Markup Language"),
        ("CSS", "Cascading Style Sheets"),
        ("JS", "JavaScript")
    ]
    
    def_table_data = [["<b>Term</b>", "<b>Definition</b>"]]
    for term, definition in definitions:
        def_table_data.append([term, definition])
    
    def_table = Table(def_table_data, colWidths=[4*cm, 12*cm])
    def_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.beige]),
    ]))
    story.append(def_table)
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("1.4 OVERVIEW", heading2_style))
    story.append(Paragraph(
        "This document is organized into seven main sections:",
        normal_style
    ))
    overview_items = [
        "<b>Introduction:</b> Purpose, scope, and overview",
        "<b>General Description:</b> Product perspective, functions, user characteristics",
        "<b>Specific Requirements:</b> Interface requirements, functional and non-functional requirements",
        "<b>Website Screenshots:</b> Visual documentation of the application",
        "<b>Code Screenshots:</b> Key implementation details",
        "<b>Database Schema:</b> Database structure and relationships",
        "<b>Project Structure:</b> Deployment and repository information"
    ]
    
    for item in overview_items:
        story.append(Paragraph(f"• {item}", normal_style))
        story.append(Spacer(1, 0.05*inch))
    
    story.append(PageBreak())
    
    # Section 2: GENERAL DESCRIPTION
    story.append(Paragraph("2. GENERAL DESCRIPTION", heading1_style))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("2.1 PRODUCT PERSPECTIVE", heading2_style))
    story.append(Paragraph(
        "The Virtual Zoo is a standalone web application built using Django framework. It operates as an "
        "educational platform that can be deployed on any web server supporting Python and Django. The system "
        "integrates with PostgreSQL (production) or SQLite (development) databases, TailwindCSS for styling, "
        "and local file system for media storage.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("2.2 PRODUCT FUNCTIONS", heading2_style))
    story.append(Paragraph("The Virtual Zoo platform provides the following core functions:", normal_style))
    
    functions = [
        ("Ecosystem Explorer", "Browse ecosystems by region and era, filter and search, view detailed environmental information"),
        ("Animal Database", "View comprehensive animal information, filter by species type, search functionality"),
        ("Educational Sessions", "Video-based learning, session enrollment, downloadable resources, interactive quizzes"),
        ("User Management", "Role-based authentication, user registration, profile management, progress tracking"),
        ("Content Management", "Admin panel for ecosystem/animal creation, teacher panel for session management")
    ]
    
    for func_name, func_desc in functions:
        story.append(Paragraph(f"<b>{func_name}:</b> {func_desc}", normal_style))
        story.append(Spacer(1, 0.05*inch))
    
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("2.3 USER CHARACTERISTICS", heading2_style))
    story.append(Paragraph("The system serves three distinct user roles:", normal_style))
    
    roles = [
        ("Administrators", "Full system access, can create/edit/delete ecosystems and animals, user management capabilities"),
        ("Teachers", "Create and manage educational sessions, upload resources, create quizzes, view student enrollments"),
        ("Students", "Browse ecosystems and animals, enroll in sessions, track learning progress, access resources")
    ]
    
    for role, desc in roles:
        story.append(Paragraph(f"<b>{role}:</b> {desc}", normal_style))
        story.append(Spacer(1, 0.05*inch))
    
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("2.4 GENERAL CONSTRAINTS", heading2_style))
    constraints = [
        "Browser Compatibility: Modern browsers (Chrome, Firefox, Safari, Edge)",
        "Network: Requires internet connection for video playback",
        "Storage: Local file storage for uploaded media",
        "Performance: Optimized for desktop, tablet, and mobile devices",
        "Security: Django's built-in security features (CSRF protection, SQL injection prevention)"
    ]
    
    for constraint in constraints:
        story.append(Paragraph(f"• {constraint}", normal_style))
        story.append(Spacer(1, 0.05*inch))
    
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("2.5 ASSUMPTIONS AND DEPENDENCIES", heading2_style))
    story.append(Paragraph("<b>Assumptions:</b>", normal_style))
    assumptions = [
        "Users have basic web browsing knowledge",
        "Video content hosted on external platforms (YouTube/Vimeo)",
        "Images are provided or downloaded from external sources",
        "Database server is accessible and properly configured"
    ]
    
    for assumption in assumptions:
        story.append(Paragraph(f"• {assumption}", normal_style))
        story.append(Spacer(1, 0.05*inch))
    
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Dependencies:</b>", normal_style))
    dependencies = [
        "Python 3.8+",
        "Django 4.2+",
        "PostgreSQL 12+ (production) or SQLite (development)",
        "Node.js and npm (for TailwindCSS compilation)",
        "Web server (for production deployment)"
    ]
    
    for dep in dependencies:
        story.append(Paragraph(f"• {dep}", normal_style))
        story.append(Spacer(1, 0.05*inch))
    
    story.append(PageBreak())
    
    # Section 3: SPECIFIC REQUIREMENTS
    story.append(Paragraph("3. SPECIFIC REQUIREMENTS", heading1_style))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("3.1 EXTERNAL INTERFACE REQUIREMENTS", heading2_style))
    story.append(Paragraph("3.1.1 User Interfaces", heading3_style))
    story.append(Paragraph(
        "The application provides a modern, responsive web interface with homepage hero section, navigation bar, "
        "ecosystem list with grid layout, ecosystem detail pages, session detail pages with video players, "
        "user dashboards, and TailwindCSS-styled forms for all CRUD operations.",
        normal_style
    ))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("3.1.2 Hardware Interfaces", heading3_style))
    story.append(Paragraph(
        "Server Requirements: Minimum 2GB RAM, 10GB storage space, network connectivity. "
        "Client Requirements: Modern web browser, internet connection, JavaScript enabled.",
        normal_style
    ))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("3.1.3 Software Interfaces", heading3_style))
    story.append(Paragraph(
        "Backend: Django 4.2+ framework, Python 3.8+ runtime, Database: PostgreSQL or SQLite. "
        "Frontend: TailwindCSS 3.0+, HTML5, JavaScript (vanilla). External Services: YouTube/Vimeo API for video embedding.",
        normal_style
    ))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("3.1.4 Communications Interfaces", heading3_style))
    story.append(Paragraph(
        "HTTP/HTTPS: Standard web protocols. RESTful URLs: Clean URL structure.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("3.2 FUNCTIONAL REQUIREMENTS", heading2_style))
    
    functional_reqs = [
        ("FR1: User Authentication", [
            "Users can register with username, email, password, and role",
            "Users can log in with credentials",
            "Users can log out securely",
            "Password validation and security"
        ]),
        ("FR2: Ecosystem Management", [
            "View list of all ecosystems with pagination",
            "Filter ecosystems by region, era, and search query",
            "View detailed ecosystem information",
            "Admin/Teacher can create, edit, and delete ecosystems",
            "Upload and display ecosystem images"
        ]),
        ("FR3: Animal Management", [
            "View animals associated with ecosystems",
            "Filter animals by species type (existing/extinct)",
            "View detailed animal information",
            "Admin/Teacher can create, edit, and delete animals",
            "Display animal images and conservation status"
        ]),
        ("FR4: Educational Sessions", [
            "View list of available sessions",
            "View session details with embedded video player",
            "Students can enroll/unenroll in sessions",
            "Teachers can create, edit, and delete sessions",
            "Upload and download session resources",
            "Interactive quizzes with multiple choice questions",
            "Comment system for session discussions"
        ]),
        ("FR5: Progress Tracking", [
            "Track student visits to ecosystems",
            "Track student attendance in sessions",
            "Display progress statistics in student dashboard",
            "Time spent tracking for learning analytics"
        ])
    ]
    
    for req_name, req_items in functional_reqs:
        story.append(Paragraph(f"<b>{req_name}</b>", normal_style))
        for item in req_items:
            story.append(Paragraph(f"• {item}", normal_style))
            story.append(Spacer(1, 0.03*inch))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("3.3 NON-FUNCTIONAL REQUIREMENT", heading2_style))
    
    nfr_items = [
        ("Performance", "Page load time: < 2 seconds, Database queries optimized, Image optimization, Pagination for large datasets"),
        ("Usability", "Intuitive navigation, Responsive design, Clear visual hierarchy, Accessible color schemes, User-friendly error messages"),
        ("Security", "CSRF protection enabled, SQL injection prevention, XSS protection, Secure password hashing, Role-based access control"),
        ("Reliability", "Error handling and logging, Database transaction management, Graceful degradation, Backup and recovery procedures"),
        ("Maintainability", "Clean code structure, Comprehensive documentation, Modular design, Follows Django best practices"),
        ("Scalability", "Database indexing, Efficient query optimization, Support for multiple concurrent users, Media file organization")
    ]
    
    for nfr_name, nfr_desc in nfr_items:
        story.append(Paragraph(f"<b>NFR: {nfr_name}</b>", normal_style))
        story.append(Paragraph(nfr_desc, normal_style))
        story.append(Spacer(1, 0.05*inch))
    
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("3.4 DESIGN CONSTRAINTS", heading2_style))
    story.append(Paragraph("<b>Technology Constraints:</b>", normal_style))
    story.append(Paragraph("Must use Django framework, Python 3.8+ required, PostgreSQL or SQLite database, TailwindCSS for styling", normal_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Platform Constraints:</b>", normal_style))
    story.append(Paragraph("Web-based application (no native mobile apps), Requires modern browser support, JavaScript must be enabled", normal_style))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("3.5 DJANGO AND DATABASE FEATURES", heading2_style))
    story.append(Paragraph("<b>Django Framework Features:</b>", normal_style))
    django_features = [
        "ORM (Object-Relational Mapping): Database abstraction layer",
        "Admin Interface: Built-in content management",
        "Template System: Django template language",
        "Form Handling: Django forms with validation",
        "Authentication: Built-in user authentication system",
        "Middleware: Security and session management",
        "URL Routing: Clean URL patterns",
        "Migrations: Database schema version control"
    ]
    
    for feature in django_features:
        story.append(Paragraph(f"• {feature}", normal_style))
        story.append(Spacer(1, 0.03*inch))
    
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Database Models Implemented:</b>", normal_style))
    
    models_list = [
        "User Model (Custom): Role-based user system (Admin, Teacher, Student)",
        "Ecosystem Model: Name, description, location, region, era, environmental data, image upload",
        "Animal Model: Name, scientific name, species type, conservation status, habitat, diet, image upload",
        "EducationalSession Model: Title, description, session type, teacher, scheduled date, video URL, lesson content",
        "SessionResource Model: File uploads (PDFs, documents), title and description",
        "SessionComment Model: User comments on sessions with timestamp tracking",
        "SessionQuiz Model: Multiple choice questions with options and correct answers",
        "SessionEnrollment Model: Student enrollment tracking with attendance status",
        "StudentProgress Model: Tracks ecosystem visits, session attendance, time spent tracking"
    ]
    
    for model in models_list:
        story.append(Paragraph(f"• {model}", normal_style))
        story.append(Spacer(1, 0.03*inch))
    
    story.append(PageBreak())
    
    # Section 4: SCREENSHOTS
    story.append(Paragraph("4. SCREENSHOTS OF WEBSITE", heading1_style))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("4.1 HOME PAGE", heading2_style))
    story.append(Paragraph(
        "The homepage features a modern hero section with gradient background (emerald to teal to cyan), "
        "animated floating animal icons, and three prominent purple action buttons. Below the hero section "
        "are featured ecosystems and upcoming educational sessions displayed in card layouts.",
        normal_style
    ))
    story.append(Paragraph(
        "<b>Note:</b> Screenshots should be captured showing the full hero section with gradient background, "
        "featured ecosystems grid, upcoming sessions display, and responsive design on different screen sizes.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("4.2 ECOSYSTEM EXPLORER", heading2_style))
    story.append(Paragraph(
        "The ecosystem explorer provides a comprehensive interface for browsing and filtering ecosystems. "
        "Features include filter by region and era, search functionality, grid layout with ecosystem cards. "
        "Detail pages show large ecosystem image header, environmental information, and associated animals list.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("4.3 LOGIN/REGISTRATION PAGE", heading2_style))
    story.append(Paragraph(
        "Clean, user-friendly authentication pages with TailwindCSS styling. Login page includes username and "
        "password fields, 'Remember me' option, and link to registration. Registration page includes username, "
        "email, password fields, role selection, and additional fields for first name, last name, phone, and bio.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("4.4 EDUCATIONAL SESSIONS", heading2_style))
    story.append(Paragraph(
        "Comprehensive session management and viewing interface. Session list page shows grid layout of session "
        "cards with session type badges, teacher information, enrollment status, and scheduled dates. Session "
        "detail page includes video player (YouTube/Vimeo embed), session description, enrollment button, "
        "downloadable resources section, quiz section, comments section, and lesson content display.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("4.5 USER DASHBOARDS", heading2_style))
    story.append(Paragraph(
        "<b>Student Dashboard:</b> Visited ecosystems count, enrolled sessions count, learning time statistics, "
        "list of visited ecosystems, list of enrolled sessions, progress tracking.",
        normal_style
    ))
    story.append(Paragraph(
        "<b>Teacher Dashboard:</b> Created sessions list, enrollment statistics, session management options, "
        "resource management, student engagement metrics.",
        normal_style
    ))
    story.append(PageBreak())
    
    # Section 5: CODE SCREENSHOTS
    story.append(Paragraph("5. SCREENSHOTS OF CODE", heading1_style))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("5.1 Model Definitions", heading2_style))
    story.append(Paragraph("File: ecosystem/models.py", normal_style))
    
    model_code = """class Ecosystem(models.Model):
    REGION_CHOICES = [
        ('amazon', 'Amazon Rainforest'),
        ('sahara', 'Sahara Desert'),
        ('arctic', 'Arctic Tundra'),
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
    updated_at = models.DateTimeField(auto_now=True)"""
    
    story.append(Preformatted(model_code, code_style))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("5.2 View Functions", heading2_style))
    story.append(Paragraph("File: ecosystem/views.py", normal_style))
    
    view_code = """def ecosystem_list(request):
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
    })"""
    
    story.append(Preformatted(view_code, code_style))
    story.append(PageBreak())
    
    # Section 6: DATABASE SCHEMA
    story.append(Paragraph("6. SCREENSHOTS OF DATABASE SCHEMA", heading1_style))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("6.1 Entity Relationship Diagram", heading2_style))
    story.append(Paragraph(
        "<b>Main Entities:</b> User (Admin, Teacher, Student), Ecosystem, Animal, EducationalSession, "
        "SessionResource, SessionComment, SessionQuiz, SessionEnrollment, StudentProgress",
        normal_style
    ))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Relationships:</b>", normal_style))
    
    relationships = [
        "User 1:N Ecosystem (created_by)",
        "Ecosystem 1:N Animal",
        "User 1:N EducationalSession (teacher)",
        "Ecosystem 1:N EducationalSession (optional)",
        "EducationalSession 1:N SessionResource",
        "EducationalSession 1:N SessionComment",
        "EducationalSession 1:N SessionQuiz",
        "EducationalSession 1:N SessionEnrollment",
        "User 1:N StudentProgress"
    ]
    
    for rel in relationships:
        story.append(Paragraph(f"• {rel}", normal_style))
        story.append(Spacer(1, 0.03*inch))
    
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("6.2 Database Tables", heading2_style))
    
    tables = [
        ("accounts_user", "id, username, email, password, role, phone_number, bio, created_at, updated_at"),
        ("ecosystem_ecosystem", "id, name, description, location, region, era, climate, temperature_min, temperature_max, vegetation, precipitation, image, created_by_id, created_at, updated_at"),
        ("ecosystem_animal", "id, ecosystem_id, name, scientific_name, species_type, description, habitat, diet, conservation_status, image, created_at, updated_at"),
        ("educational_sessions_educationalsession", "id, title, description, session_type, teacher_id, ecosystem_id, scheduled_date, duration_minutes, max_students, image, video_url, lesson_content, created_at, updated_at"),
        ("educational_sessions_sessionresource", "id, session_id, title, file, description, uploaded_at"),
        ("educational_sessions_sessioncomment", "id, session_id, user_id, content, created_at, updated_at"),
        ("educational_sessions_sessionquiz", "id, session_id, question, option_a, option_b, option_c, option_d, correct_answer, explanation, created_at"),
        ("educational_sessions_sessionenrollment", "id, session_id, student_id, enrolled_at, attended, notes"),
        ("accounts_studentprogress", "id, student_id, ecosystem_id, session_id, visited_at, time_spent_minutes, completed")
    ]
    
    table_data = [["<b>Table Name</b>", "<b>Columns</b>"]]
    for table_name, columns in tables:
        table_data.append([table_name, columns])
    
    db_table = Table(table_data, colWidths=[5*cm, 11*cm])
    db_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.beige]),
    ]))
    story.append(db_table)
    story.append(PageBreak())
    
    # Section 7: PROJECT STRUCTURE
    story.append(Paragraph("7. PROJECT STRUCTURE AND DEPLOYMENT", heading1_style))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("7.1 Project Structure", heading2_style))
    
    structure_code = """virtual_zoo/
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
└── manage.py            # Django management script"""
    
    story.append(Preformatted(structure_code, code_style))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("7.2 Installation and Setup", heading2_style))
    story.append(Paragraph("<b>Requirements:</b> Python 3.8+, Django 4.2+, PostgreSQL 12+ (production) or SQLite (development), Node.js and npm (for TailwindCSS)", normal_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Installation Steps:</b>", normal_style))
    
    install_steps = [
        "Create virtual environment: python -m venv myenv",
        "Install dependencies: pip install -r requirements.txt",
        "Run migrations: python manage.py migrate",
        "Create superuser: python manage.py createsuperuser",
        "Setup TailwindCSS: python manage.py tailwind install",
        "Create demo data: python manage.py create_demo_data",
        "Run development server: python manage.py runserver"
    ]
    
    for i, step in enumerate(install_steps, 1):
        story.append(Paragraph(f"{i}. {step}", normal_style))
        story.append(Spacer(1, 0.03*inch))
    
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("7.3 Deployment Considerations", heading2_style))
    story.append(Paragraph(
        "Production Database: Use PostgreSQL instead of SQLite. Static Files: Collect and serve through web server or CDN. "
        "Media Files: Store in cloud storage (AWS S3, etc.) for production. Security: Set DEBUG=False, configure ALLOWED_HOSTS. "
        "Web Server: Use Gunicorn with Nginx. HTTPS: Enable SSL certificates. Backup: Regular database backups.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("7.4 GitHub Repository", heading2_style))
    story.append(Paragraph(
        "Repository Structure: Main branch for production-ready code, Development branch for feature development, "
        "README.md with setup instructions, requirements.txt for Python dependencies, .gitignore for excluded files.",
        normal_style
    ))
    story.append(Paragraph(
        "<b>Note:</b> Include GitHub repository link in the actual PDF report.",
        normal_style
    ))
    
    # Build PDF
    doc.build(story)
    print("PDF report generated successfully: Virtual_Zoo_Project_Report.pdf")
    print("The report includes all sections as requested in your table of contents.")

if __name__ == '__main__':
    try:
        generate_pdf()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

