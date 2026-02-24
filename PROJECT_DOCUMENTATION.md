# GenuinCode - E-Learning Platform
A Django-based e-learning platform with video lessons, live classes, quizzes, progress tracking, course certificates, and multiple payment gateway integration.

---

## 🚀 Commands to Operate the Project

### 1. Setup Virtual Environment
```
bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Mac/Linux)
source venv/bin/activate
```

### 2. Install Dependencies
```
bash
pip install -r requirements.txt
```

### 3. Database Setup
```
bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (for admin panel)
python manage.py createsuperuser
```

### 4. Run Development Server
```
bash
# Run server on localhost:8000
python manage.py runserver

# Run server on custom port
python manage.py runserver 8080
```

### 5. Collect Static Files
```
bash
python manage.py collectstatic
```

### 6. Deployment (Production)
```
bash
# Using gunicorn (as defined in Procfile)
gunicorn admin.wsgi:application
```

---

## 🛠️ Technologies Used

### Backend
| Technology | Version | Purpose |
|------------|---------|---------|
| Django | 5.1.7 | Web Framework |
| Python | 3.11.6 | Programming Language |

### Database
| Technology | Purpose |
|------------|---------|
| PostgreSQL | Production Database |
| SQLite | Local Development |

### Python Packages
| Package | Version | Purpose |
|---------|---------|---------|
| Django | 5.1.7 | Web Framework |
| python-dotenv | 1.0.0 | Environment Variables |
| Pillow | 10.2.0 | Image Processing |
| gunicorn | 21.2.0 | WSGI HTTP Server |
| psycopg2-binary | 2.9.11 | PostgreSQL Adapter |
| dj-database-url | 3.1.2 | Database URL Parser |

### Frontend
| Technology | Purpose |
|------------|---------|
| HTML5 | Markup Language |
| CSS3 | Styling |
| JavaScript | Client-side Logic |
| Bootstrap | UI Framework (implied from templates) |

### Deployment
| Service | Purpose |
|---------|---------|
| Render | Cloud Hosting |
| Gunicorn | WSGI Server |

---

## 🔗 APIs and Endpoints

### URL Routes (from GENUIN_CODE/urls.py)

| Endpoint | View Function | Purpose |
|----------|----------------|---------|
| `/` | `views.index` | Home page with signup form |
| `/blog/` | `views.blog` | Blog listing page |
| `/contact/` | `views.contact` | Contact form page |
| `/course/` | `views.course` | Course listing page |
| `/course_inner/` | `views.course_inner` | Course details page |
| `/home/` | `views.home` | Home page with lead form |
| `/post/` | `views.post` | Blog post page |
| `/about/` | `views.about` | About page |
| `/login/` | `views.login` | User login page |
| `/signup/` | `views.signup` | User registration page |
| `/base/` | `views.base` | Base layout template |
| `/learnmore_home/` | `views.learnmore_home` | Learn more page |
| `/success/` | `views.success` | Success page after form submission |
| `/my_course/` | `views.my_course` | User's enrolled courses |
| `/update-profile/` | `views.update_profile` | Profile update page (requires login) |
| `/logout/` | `views.logout_view` | User logout |

---

## 💳 Payment Integration

### Razorpay API
The project uses Razorpay for payment processing.

**Configuration (in admin/settings.py):**
```python
RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID", "")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET", "")
```

**Environment Variables Required:**
- `SECRET_KEY` - Django secret key
- `RAZORPAY_KEY_ID` - Razorpay API Key ID
- `RAZORPAY_KEY_SECRET` - Razorpay API Key Secret

---

## 🗄️ Database Models

### Models (from GENUIN_CODE/models.py)

1. **Ragister** - Lead/Registration model
   - `name`: CharField (max 100)
   - `email`: EmailField
   - `phone_number`: CharField (max 15)

2. **Contact** - Contact form submissions
   - `name`: CharField (max 100)
   - `email`: EmailField
   - `subject`: CharField (max 200)
   - `message`: TextField

3. **CustomUser** - Custom user model
   - `username`: CharField (max 100, unique)
   - `email`: EmailField (unique)
   - `password`: CharField (max 100)

4. **LoginAttempt** - Login attempt tracking
   - `email`: EmailField
   - `password`: CharField (max 100)
   - `timestamp`: DateTimeField (auto_now_add)

5. **Profile** - Extended user profile
   - `user`: OneToOneField to User model
   - `bio`: TextField
   - `image`: ImageField

---

## 📝 Forms

### Forms (from GENUIN_CODE/forms.py)

1. **RagisterForm** - Lead registration form
   - Fields: name, email, phone_number

2. **ContactForm** - Contact form
   - Fields: name, email, subject, message

3. **CustomUserForm** - User signup form
   - Fields: username, email, password1, password2

4. **LoginForm** - User login form
   - Fields: email, password

5. **ProfileUpdateForm** - Profile update form
   - Fields: image, bio

---

## 📁 Project Structure

```
Genuincode-main/
├── admin/                    # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           # Main settings file
│   ├── urls.py               # Main URL configuration
│   ├── wsgi.py
│   └── payment.env           # Payment environment variables
├── GENUIN_CODE/              # Main Django app
│   ├── __init__.py
│   ├── admin.py              # Admin configuration
│   ├── apps.py
│   ├── forms.py              # Django forms
│   ├── models.py             # Database models
│   ├── urls.py               # App URL patterns
│   ├── views.py              # View functions
│   ├── tests.py
│   └── migrations/           # Database migrations
├── static/                   # Static files
│   ├── css/
│   │   └── style.css
│   └── image/                # Image assets
├── template/                  # HTML templates
│   ├── about.html
│   ├── base.html
│   ├── blog.html
│   ├── contact.html
│   ├── course.html
│   ├── course_inner.html
│   ├── index.html
│   ├── learnmore_home.html
│   ├── login.html
│   ├── my_course.html
│   ├── payment_checkout.html
│   ├── post.html
│   ├── signup.html
│   ├── partials/
│   │   └── footer.html
│   └── ...
├── .gitignore
├── manage.py                 # Django management script
├── Procfile                  # Render deployment config
├── README.md
├── requirements.txt          # Python dependencies
└── runtime.txt               # Python runtime version
```

---

## 🔧 Configuration

### Django Settings (admin/settings.py)

- **DEBUG**: False (Production mode)
- **ALLOWED_HOSTS**: ['.onrender.com', 'localhost', '127.0.0.1']
- **DATABASE**: PostgreSQL (via dj-database-url)
- **STATIC_URL**: /static/
- **TEMPLATE_DIR**: template/

---

## 🏃 How to Run Locally

1. **Clone the repository**
2. **Create virtual environment**: `python -m venv venv`
3. **Activate**: `venv\Scripts\activate` (Windows)
4. **Install requirements**: `pip install -r requirements.txt`
5. **Setup environment variables** (create .env file):
   
```
   SECRET_KEY=your_secret_key
   RAZORPAY_KEY_ID=your_razorpay_key
   RAZORPAY_KEY_SECRET=your_razorpay_secret
   
```
6. **Run migrations**: `python manage.py migrate`
7. **Start server**: `python manage.py runserver`
8. **Visit**: http://localhost:8000

---

## 🌐 Deployment (Render)

The project is configured for deployment on Render:

1. **Procfile**: `web: gunicorn admin.wsgi:application`
2. **Runtime**: Python 3.11.6
3. **Build Command**: `pip install -r requirements.txt`
4. **Start Command**: `gunicorn admin.wsgi:application`

---

## 📌 Summary

| Category | Details |
|----------|---------|
| **Framework** | Django 5.1.7 |
| **Python Version** | 3.11.6 |
| **Database** | PostgreSQL (Production), SQLite (Local) |
| **Authentication** | Django Built-in Auth |
| **Payment Gateway** | Razorpay |
| **Deployment** | Render |
| **Static Files** | CSS, Images |
| **Templates** | 15+ HTML templates |
| **Forms** | 5 Django Forms |
| **Models** | 5 Database Models |
| **URL Endpoints** | 16 Routes |
