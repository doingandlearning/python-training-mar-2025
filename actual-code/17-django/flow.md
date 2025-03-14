# Django Project Documentation

## 📌 1. Project Overview
This Django project is a REST API built with Django REST Framework (DRF). It includes:
- **CRUD operations** on a model.
- **Django admin support**.
- **Database-backed storage using SQLite**.
- **API endpoints for interacting with the data**.

---
## 📌 2. Installation & Setup
### **1️⃣ Install Dependencies**
Ensure you have Python installed (version 3.8+ recommended).

```sh
pip install -r requirements.txt  # If requirements.txt exists
```

### **2️⃣ Run Migrations**
```sh
python manage.py migrate
```

### **3️⃣ Create a Superuser** (for Django admin)
```sh
python manage.py createsuperuser
```

### **4️⃣ Start the Development Server**
```sh
python manage.py runserver
```
The server runs at: **http://127.0.0.1:8000/**

---
## 📌 3. API Endpoints & Usage
### **✅ Available Endpoints**
| Method | Endpoint          | Description |
|--------|------------------|-------------|
| GET    | `/api/items/`    | List all items |
| POST   | `/api/items/`    | Create a new item |
| GET    | `/api/items/{id}/` | Retrieve an item |
| PUT    | `/api/items/{id}/` | Update an item |
| DELETE | `/api/items/{id}/` | Delete an item |

### **Example API Request (Using `requests`)**
```python
import requests

response = requests.get("http://127.0.0.1:8000/api/items/")
print(response.json())
```

---
## 📌 4. How Django Processes a Request

1️⃣ **User Sends a Request** → `http://127.0.0.1:8000/api/items/`
2️⃣ **Django URL Router** (`urls.py`) matches it to a view
3️⃣ **View (`views.py`) Processes the Request**
4️⃣ **Database (`models.py`) is Queried**
5️⃣ **Serializer (`serializers.py`) Converts Data**
6️⃣ **Response is Sent Back** (JSON in this case)

### **🔹 Flow of Files When a Request is Processed**
```
Request  → urls.py → views.py → models.py → database → serializers.py → Response
```

---
## 📌 5. Common Commands & Development Workflow

| Command | Purpose |
|---------|---------|
| `python manage.py runserver` | Start the Django server |
| `python manage.py makemigrations` | Prepare database migrations |
| `python manage.py migrate` | Apply database migrations |
| `python manage.py createsuperuser` | Create an admin user |
| `python manage.py test` | Run tests |

---
### **🚀 Next Steps**
- Try extending the model (`lab-0-extend-model/`).
- Implement more complex CRUD operations (`lab-2-crud/`).
- Explore Django REST Framework features (`01-drf-notes.md`).

