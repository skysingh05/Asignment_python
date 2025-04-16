# 🐍 Python Intern Assignment – Backend API with Django

This project is part of the **Python Intern Assignment**. It includes:

- ✅ A Django-based API to manage app information.
- 🗃️ SQLite database integration.
- 🔁 Endpoints to add, retrieve, and delete app details.

---

## 📁 Project Structure

```
andro/
├── appsystem/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── andro/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
├── myenv/
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository (or unzip the folder)

```bash
git clone <repo_url>
```

### 2. Navigate to the project root

```bash
cd andro
```

### 3. Activate the virtual environment

```bash
source myenv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install Django manually:

```bash
pip install django
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

---

## 🔌 API Endpoints

**Base URL:** `http://127.0.0.1:8001/app/`

---

### ▶️ `POST /add-app/`

**Description:** Add a new app to the database.  
**Request Body (JSON):**

```json
{
  "app_name": "Calculator",
  "version": "1.0",
  "description": "Simple calculator app."
}
```

---

### 📥 `GET /get-app/<id>/`

**Description:** Fetch details of a specific app by its ID.  
**Example:**

```
http://127.0.0.1:8001/app/get-app/1/
```

---

### ❌ `DELETE /delete-app/<id>/`

**Description:** Delete an app from the database by its ID.  
**Example:**

```
http://127.0.0.1:8001/app/delete-app/1/
```

---

## ✅ Testing the API

You can test the endpoints using:

- Postman
- `curl`
- HTTPie
- Your browser (for GET requests)

---

## 🧠 Notes

- The database uses **SQLite** by default.
- Auto-incremented IDs will not reuse deleted IDs.
- The project is **modular** — you can expand it for Android simulation or networking later.

---

## 👨‍💻 Author

Akash Kumar Singh
Python Intern – Assignment Submission  
📅 April 2025
