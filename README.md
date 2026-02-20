# 🔍 Lost & Found Portal
### A Full-Stack Django Web Application for Campus Item Tracking

This project was developed as part of my **Advance Programming** course at **Federal Urdu University (FUUAST)**. It provides a centralized platform for students and staff to report, search for, and recover lost items.

---

## 🚀 Features
- **Item Reporting:** Users can upload details of lost or found items, including descriptions and images.
- **Admin Moderation:** All posts require admin approval before becoming public to ensure safety and quality.
- **Search & Filter:** Easily filter items by status (Lost, Found, or Returned).
- **Automated Cleanup:** To keep the database clean, "Returned" items are automatically deleted after 7 days.
- **WhatsApp Integration:** Direct communication link to the finder/owner via WhatsApp.

---

## 🛠️ Tech Stack
- **Backend:** Python 3.14 & Django
- **Frontend:** HTML5, CSS3, & Bootstrap
- **Database:** SQLite (Development)
- **Image Hosting:** Cloudinary (Configured for persistent storage)

---

## 📸 Screenshots
*(Pro-tip: Once you run your app, take 2-3 screenshots and upload them here!)*

---

## ⚙️ Installation & Setup
To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Mistaqlal-Haider/LostFoundProject.git](https://github.com/Mistaqlal-Haider/LostFoundProject.git)

2. Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.  Install dependencies:
pip install -r requirements.txt

4.  Run migrations & Start server:
python manage.py migrate
python manage.py runserver

🎓 Academic Context
Institution: Federal Urdu University of Arts Science and Technology, Islamabad.

Semester: 7th Semester (BDP Computer Science).

Instructor: Mr M Aqib

