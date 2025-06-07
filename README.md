# Little Lemon API 🍋

This is a RESTful API project developed as part of the **Meta API Development course** on Coursera. The project provides backend functionality for the fictional **Little Lemon** restaurant, allowing different user roles to interact with the system through secure API endpoints.

## 📌 Project Overview

As part of the course, this project demonstrates:

- Designing and building RESTful APIs with Django and Django REST Framework
- Role-based access control and authentication
- Endpoints for managing menu items, orders, and delivery crew
- Real-world API structuring and implementation

## 🔐 Roles and Permissions

| Role           | Permissions                                      |
|----------------|--------------------------------------------------|
| **Manager**    | Full access to menus and orders                  |
| **Delivery**   | View assigned orders and mark them as delivered  |
| **Customer**   | Browse menu, place and view orders               |

## 🚀 Features

- Menu item CRUD operations
- Order placement and assignment
- Delivery tracking
- Token-based authentication
- Role-specific access using Django permissions

## 🛠 Tech Stack

- Python 3.x
- Django
- Django REST Framework
- SQLite (for development)

## 📁 Project Structure
MetaLemonBackend/
├── LittleLemonAPI/         # App containing all core logic
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py           # Database models (Category, MenuItem, Order, etc.)
│   ├── serializers.py      # DRF serializers
│   ├── views.py            # DRF views and viewsets
│   ├── urls.py             # App-level URL routing
│   └── permissions.py      # (Optional) Custom permissions
├── MetaLemonBackend/       # Main Django project config
│   ├── __init__.py
│   ├── settings.py         # Django settings (incl. REST, Djoser config)
│   ├── urls.py             # Project-level URLs
│   └── wsgi.py
├── Pipfile / Pipfile.lock  # Pipenv dependency management
├── db.sqlite3              # SQLite database
└── manage.py               # Django CLI tool

🔗 API Endpoints (Grouped)
👤 Authentication & User
Method	Endpoint	Role	Description
POST	/api/users/	Anyone	Register new user
GET	/api/users/me/	Authenticated	Get current user details
POST	/token/login/	Anyone	Obtain JWT token

📋 Menu Items
Method	Endpoint	Role	Description
GET	/api/menu-items/	All roles	List all menu items
POST	/api/menu-items/	Manager	Create a menu item
PUT	/api/menu-items/{id}/	Manager	Update a menu item
DELETE	/api/menu-items/{id}/	Manager	Delete a menu item

🛒 Cart
Method	Endpoint	Role	Description
GET	/api/cart/menu-items/	Customer	View current cart
POST	/api/cart/menu-items/	Customer	Add item to cart
DELETE	/api/cart/menu-items/	Customer	Clear all items from cart

📦 Orders
Method	Endpoint	Role	Description
GET	/api/orders/	All roles	View own / assigned / all orders
POST	/api/orders/	Customer	Place order from cart
PATCH	/api/orders/{id}/	Manager / Crew	Update delivery or status
DELETE	/api/orders/{id}/	Manager	Delete order

👥 User Groups
Method	Endpoint	Role	Description
POST	/api/groups/manager/users/	Manager	Assign user to Manager group
DELETE	/api/groups/manager/users/{id}/	Manager	Remove user from Manager group
POST	/api/groups/delivery-crew/users/	Manager	Assign user to Delivery crew group
DELETE	/api/groups/delivery-crew/users/{id}/	Manager	Remove user from Delivery crew group



