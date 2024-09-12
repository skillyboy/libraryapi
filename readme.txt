Here's the updated README reflecting your current setup with PostgreSQL, Docker, and Django Admin for performing CRUD operations.

---

# Library API

This project is a Library Management System that allows users to enroll in the library, borrow books, and view available books. Admins can perform CRUD operations via the Django Admin interface, and the entire project is dockerized for easy deployment.

## **1. Project Overview**

This API provides two sets of operations:
- **Frontend API:** For users to enroll, view books, and borrow books.
- **Backend/Admin API:** For admins to manage the library's catalog, users, and borrowing records via the Django Admin panel.

## **2. Running the Project**

To get the project up and running locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/skillyboy/libraryapi.git
   cd libraryapi
   ```

2. **Run the project using Docker Compose:**

   ```bash
   docker-compose up --build
   ```

3. **Create an admin user:**

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

4. **Access the application:**
   - User API Docs: `http://localhost:8000/api/docs`
   - Admin Dashboard: `http://localhost:8000/admin`

---

## **3. API Endpoints**

### **Frontend API:**

| Endpoint              | Method | Description                                      | Auth  |
|-----------------------|--------|--------------------------------------------------|-------|
| `/api/enroll-user/`    | POST   | Enroll a user into the library                   | No    |
| `/api/users/`          | GET    | List all enrolled users                          | No    |
| `/api/books/`          | GET    | List all available books with optional filters   | No    |
| `/api/books/{id}/`     | GET    | Fetch details of a single book by ID             | No    |
| `/api/borrow/`         | POST   | Borrow a book by ID and specify the number of days| No    |
| `/api/borrowed-books/` | GET    | List all borrowed books                          | No    |
| `/api/unavailable-books/` | GET | List books not available for borrowing (with return dates) | No |

### **Backend/Admin API:**

Backend/Admin API:

/admin/books/book/	POST	Add a new book to the catalog	Yes
/admin/books/book/{id}/delete/	DELETE	Remove a book from the catalog	Yes
/admin/books/user/	GET	List all users enrolled in the library	Yes
/admin/books/borrowing/	GET	List all users and the books they borrowed	Yes
/admin/books/	GET	List unavailable books showing return dates	Yes


## **4. Admin Access**

For all admin-related operations, the Django Admin interface is used. Admin authentication is handled via Django's default login system.

- **Admin Login:** `http://localhost:8000/admin`
- **Admin Operations:** Create, update, and delete books, manage users, and monitor borrowed books via the admin panel.

---

## **5. Database Structure**

The project uses **PostgreSQL** as the database. Below is a high-level overview of the database models:

### **Publisher**
- `name`: The name of the publisher.

### **Category**
- `name`: The name of the category (e.g., Fiction, Technology).

### **Book**
- `title`: Title of the book.
- `publisher`: ForeignKey to the `Publisher` model.
- `category`: ForeignKey to the `Category` model.
- `available`: Boolean indicating if the book is available for borrowing.
- `return_date`: The date when the book will be available again (if borrowed).

### **User**
- `email`: The user's email address.
- `first_name`: The user's first name.
- `last_name`: The user's last name.

### **Borrowing**
- `user`: ForeignKey to the `User` model.
- `book`: ForeignKey to the `Book` model.
- `borrowed_on`: Date when the book was borrowed.
- `return_date`: Expected return date.

---


## **6. Running Tests**

Tests have been written for the core functionality of the application, including user enrollment, book listing, and borrowing actions.

To run the tests:
```bash
docker-compose exec web python manage.py test
```

---

## **7. Deployment with Docker**

The project is fully Dockerized for easy deployment. The **Docker Compose** configuration allows you to spin up the application along with PostgreSQL.

### **Docker Compose Configuration:**
- **docker-compose.yml** contains configurations for the Django app and PostgreSQL.

### **Steps to Deploy:**
1. Build the Docker containers:
   ```bash
   docker-compose build
   ```
2. Run the containers:
   ```bash
   docker-compose up
   ```
3. The application will be accessible at `http://localhost:8000`.

---

This README file provides a comprehensive guide for running, testing, and contributing to the project.