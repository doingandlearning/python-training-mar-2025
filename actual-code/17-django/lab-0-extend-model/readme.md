# Lab: Adding a New Model to Your Django App

In this lab, you will extend your Django application by adding a new model in `models.py`, applying the necessary migrations, and configuring the Django Admin panel for better usability.

## Steps to Follow

### 1. Define a New Model in `models.py`
1. Open your Django app's `models.py` file.
2. Add a new model with at least three fields (e.g., `name`, `description`, and `created_at`).
3. Ensure `created_at` is set to `auto_now_add=True` to store the creation timestamp.

#### Example:
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

### 2. Make and Apply Migrations
1. Run the following command to generate the migration file:
   ```sh
   python manage.py makemigrations
   ```
2. Apply the migration to update the database:
   ```sh
   python manage.py migrate
   ```

### 3. Register the Model in Django Admin
1. Open `admin.py` in your Django app.
2. Import the new model and register it:
   ```python
   from django.contrib import admin
   from .models import Product

   admin.site.register(Product)
   ```

 

### 4. Improve Admin Display
1. Modify the registration to customize the admin panel:
   ```python
   class ProductAdmin(admin.ModelAdmin):
       list_display = ('name', 'description', 'created_at')
       search_fields = ('name', 'description')
       ordering = ('-created_at',)

   admin.site.register(Product, ProductAdmin)
   ```

#### Alternative: Using the Decorator Pattern

Instead of registering the model using the `admin.site.register` method, you can use the `@admin.register` decorator for a more concise and readable approach.

1. Open `admin.py` in your Django app.
2. Use the `@admin.register` decorator to register the model:

```python
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
```

### 5. Verify Your Changes
1. Start the Django development server:
   ```sh
   python manage.py runserver
   ```
2. Log in to the Django Admin panel (`http://127.0.0.1:8000/admin`).
3. Navigate to the new model and check that it appears correctly with search and ordering applied.

## Extension Points
If you have additional time, try enhancing the model:
- **Add a new field** (e.g., `price = models.DecimalField(max_digits=10, decimal_places=2)`).
- **Create a related model** (e.g., a `Category` model linked via `ForeignKey`).
- **Customize admin filters** using `list_filter`.
- **Use Django forms** to create and edit entries via a custom UI.

---
This lab helps reinforce concepts of **Django models, migrations, and admin panel customization** to enhance your database-driven applications.

