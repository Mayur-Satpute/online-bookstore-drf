# Online Bookstore Backend — Django REST Framework

A **backend-focused e-commerce system** built using **Python, Django, and Django REST Framework**.  
This project demonstrates real-world backend engineering concepts such as authentication, role-based access control, business logic design, and REST API workflows.

The backend is **frontend-agnostic** and designed to integrate with any web or mobile client.

---

## 🚀 Project Overview

The Online Bookstore backend supports core e-commerce functionality including:

- Secure user authentication
- Product and category management
- Cart workflows
- Order lifecycle management
- Role-based access (Admin vs User)

This project was built with a **learning-while-building approach**, focusing on clean architecture, predictable APIs, and real-world problem solving.

---

## 🛠 Tech Stack

- **Language:** Python  
- **Framework:** Django, Django REST Framework  
- **Authentication:** JWT (access & refresh tokens)  
- **Database:** SQLite (development)  
- **API Testing:** Postman  
- **Version Control:** Git & GitHub  

---

## 🔐 Authentication & Authorization

- Email-based user signup and login
- JWT authentication (access & refresh tokens)
- Secure logout
- Forgot password & reset password via token
- Role-based access control:
  - **Admin:** Manage books, categories, and orders
  - **User:** Browse books, manage cart, place orders

---

## 📚 Features

### 1️⃣ Books & Categories
- Public APIs to list and view books
- Admin-only APIs to create, update, and delete books
- Category management with uniqueness constraints
- Image upload support for book covers

### 2️⃣ Cart Management
- Add books to cart
- View cart with quantity and total price
- Update and remove cart items
- Clean, frontend-friendly API responses

### 3️⃣ Order Management
- Place orders directly from cart
- Convert cart items into immutable order items
- Auto-clear cart after checkout
- User-specific order history
- Admin APIs to view, update status, and cancel orders

---

## 🧠 Key Backend Learnings

- Backend engineering is about **business logic**, not just CRUD
- Clean API design matters as much as database modeling
- Role-based permissions prevent real-world bugs
- Debugging and refactoring are part of professional development
- Separation of concerns improves scalability and maintainability

---

## 🧪 API Testing

All APIs were tested end-to-end using **Postman**, covering:
- Authentication flows
- Protected endpoints
- Cart and order workflows
- Permission and validation edge cases

---

## ▶️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/Mayur-Satpute/online-bookstore-drf.git

# Navigate into the project
cd online-bookstore-drf

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
Server will run at:

cpp
Copy code
http://127.0.0.1:8000/
📌 API Base Endpoints
Authentication: /api/auth/

Books & Categories: /api/books/

Cart: /api/cart/

Orders: /api/orders/

(Refer to code for detailed endpoints and permissions.)

📈 Project Status
✅ Backend complete
🔜 Documentation improvements & enhancements
🔜 Optional deployment

🤝 Contributions & Feedback
Feel free to explore the code, open issues, or suggest improvements.
Contributions and feedback are always welcome.

👤 Author
Mayur Satpute
Backend-focused Python Developer
Building real-world systems with Django REST Framework

🔗 GitHub: https://github.com/Mayur-Satpute

📄 License
This project is for learning and demonstration purposes.
