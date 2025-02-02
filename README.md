# Multilingual FAQ API (Django + DRF)

## Overview
This is a Django REST Framework (DRF) project that provides an FAQ API with multilingual support (English, Hindi, Bengali). It uses:

- **Django & DRF** for API Development
- **Redis** for caching API responses
- **Google Translate API** for automatic translations
- **django-ckeditor** for WYSIWYG answer formatting

---

## Installation Guide

### 1. Clone the Repository
```bash 
git clone https://github.com/YOUR_USERNAME/multilingual-faq-api.git
```
```bash 
cd multilingual-faq-api
```

### 2. Create and Activate a Virtual Environment
```bash 
python -m venv venv
```
```bash
venv\Scripts\activate
``` 

### 3. Install Dependencies
```bash 
pip install -r requirements.txt
```

### 4. Configure Redis for Caching
Start Redis:
```bash 
redis-server
```
(Linux/Mac)  
For Windows, install [Memurai](https://www.memurai.com/).

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser for Admin Access
```bash 
python manage.py createsuperuser
```

### 7. Start the Server
```bash 
python manage.py runserver
```

Now, open:
- **API**: http://127.0.0.1:8000/api/faqs/
- **Admin Panel**: http://127.0.0.1:8000/admin/

---

## API Usage

### 1. Get All FAQs (English - Default)
```bash 
curl http://127.0.0.1:8000/api/faqs/
```

### 2. Get FAQs in Hindi
```bash 
curl http://127.0.0.1:8000/api/faqs/?lang=hi
```

### 3. Get FAQs in Bengali
```bash 
curl http://127.0.0.1:8000/api/faqs/?lang=bn
```

---

## Tech Stack
- **Django & Django REST Framework (DRF)**
- **Redis** for caching
- **Google Translate API** for auto-translation
- **SQLite** (default)

---

## Contribution Guidelines
Want to contribute? Follow these steps:
1. Fork the repo.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "feat: Added XYZ feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a Pull Request.

---

## License
This project is MIT Licensed. Feel free to use and modify.

---

## Contact
For issues, contact: **your.email@example.com**  
GitHub: **[YourUsername](https://github.com/YourUsername)**

---

**Happy Coding!**
