# Quick Start Guide

## First Time Setup

1. **Activate virtual environment**
   ```bash
   myenv\Scripts\activate  # Windows
   # or
   source myenv/bin/activate  # macOS/Linux
   ```

2. **Install dependencies** (if not already done)
   ```bash
   pip install -r requirements.txt
   cd theme/static_src
   npm install
   cd ../..
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Build TailwindCSS** (one-time build)
   ```bash
   cd theme/static_src
   npm run build
   cd ../..
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Home: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## Daily Development

1. **Activate virtual environment**
   ```bash
   myenv\Scripts\activate
   ```

2. **Start TailwindCSS watch** (in a separate terminal)
   ```bash
   cd theme/static_src
   npm run watch
   ```

3. **Start Django server** (in another terminal)
   ```bash
   python manage.py runserver
   ```

## Creating Sample Data

1. Login to admin panel: http://127.0.0.1:8000/admin/
2. Create users with different roles (Admin, Teacher, Student)
3. Create ecosystems
4. Add animals to ecosystems
5. Create educational sessions

## Testing the Application

1. **Register a new user** at http://127.0.0.1:8000/accounts/register/
2. **Browse ecosystems** at http://127.0.0.1:8000/ecosystem/
3. **View sessions** at http://127.0.0.1:8000/sessions/
4. **Login as different roles** to test permissions

