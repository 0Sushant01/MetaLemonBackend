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

---

## 🔗 API Endpoints (Grouped)

### 👤 Authentication & User

| Method | Endpoint           | Role         | Description              |
|--------|--------------------|--------------|--------------------------|
| POST   | `/api/users/`      | Anyone       | Register new user        |
| GET    | `/api/users/me/`   | Authenticated| Get current user details |
| POST   | `/token/login/`    | Anyone       | Obtain JWT token         |

---

### 📋 Menu Items

| Method | Endpoint                   | Role    | Description             |
|--------|----------------------------|---------|-------------------------|
| GET    | `/api/menu-items/`         | All     | List all menu items     |
| POST   | `/api/menu-items/`         | Manager | Create a menu item      |
| PUT    | `/api/menu-items/{id}/`    | Manager | Update a menu item      |
| DELETE | `/api/menu-items/{id}/`    | Manager | Delete a menu item      |

---

### 🛒 Cart

| Method | Endpoint                      | Role     | Description            |
|--------|-------------------------------|----------|------------------------|
| GET    | `/api/cart/menu-items/`       | Customer | View current cart      |
| POST   | `/api/cart/menu-items/`       | Customer | Add item to cart       |
| DELETE | `/api/cart/menu-items/`       | Customer | Clear all items in cart|

---

### 📦 Orders

| Method | Endpoint              | Role             | Description                       |
|--------|-----------------------|------------------|-----------------------------------|
| GET    | `/api/orders/`        | All              | View own/assigned/all orders      |
| POST   | `/api/orders/`        | Customer         | Place order from cart             |
| PATCH  | `/api/orders/{id}/`   | Manager / Crew   | Update delivery or status         |
| DELETE | `/api/orders/{id}/`   | Manager          | Delete order                      |

---

### 👥 User Groups

| Method | Endpoint                                 | Role    | Description                        |
|--------|------------------------------------------|---------|------------------------------------|
| POST   | `/api/groups/manager/users/`             | Manager | Assign user to Manager group       |
| DELETE | `/api/groups/manager/users/{id}/`        | Manager | Remove user from Manager group     |
| POST   | `/api/groups/delivery-crew/users/`       | Manager | Assign user to Delivery Crew group |
| DELETE | `/api/groups/delivery-crew/users/{id}/`  | Manager | Remove user from Delivery Crew     |

---

## ✅ Features

- Token authentication using Djoser
- Role-based access control
- CRUD operations for menu, cart, orders
- Pagination, filtering, and permissions

## 📦 Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- Djoser
- SQLite (default DB)
- Pipenv for environment management

---

## 🚀 Running Locally

```bash
git clone https://github.com/yourusername/LittleLemonAPI.git
cd LittleLemonAPI
pipenv install
pipenv shell
python manage.py migrate
python manage.py runserver




