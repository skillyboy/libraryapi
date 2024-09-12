USER:
http://localhost:8000/api/docs

ADMIN :
http://localhost:8000/admin

docker-compose up --build
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py runserver 0.0.0.0:8000

===================================================
CHECK OUT MY TASK HERE
---

### **3. API Endpoints**

#### **Frontend API:**

| Endpoint              | Method | Description                                      | Auth  |
|-----------------------|--------|--------------------------------------------------|-------|
| `/api/enroll-user/`    | POST   | Enroll a user into the library                   | No    |
| `/api/users/`          | GET    | List all enrolled users                          | No    |
| `/api/books/`          | GET    | List all available books with optional filters   | No    |
| `/api/books/{id}/`     | GET    | Fetch details of a single book by ID             | No    |
| `/api/borrow/`         | POST   | Borrow a book by ID and specify the number of days| No    |
| `/api/borrowed-books/` | GET    | List all borrowed books                          | No    |
| `/api/unavailable-books/` | GET | List books not available for borrowing (with return dates) | No |

#### **Backend/Admin API:**

| Endpoint                 | Method | Description                                     | Auth  |
|--------------------------|--------|-------------------------------------------------|-------|
| `/admin/books/`           | POST   | Add a new book to the catalog                   | Yes   |
| `/admin/books/{id}/`      | DELETE | Remove a book from the catalog                  | Yes   |
| `/admin/users/`           | GET    | List all users enrolled in the library          | Yes   |
| `/admin/borrowed-books/`  | GET    | List all users and the books they borrowed      | Yes   |
| `/admin/unavailable-books/` | GET  | List unavailable books showing return dates     | Yes   |

---

### **4. Authentication**

Currently, the endpoints do not require authentication for frontend operations. However, for admin-related operations, authentication is required. Admins can log in via Django’s built-in authentication system.

- **Admin Authentication:** Admin authentication is handled via Django's default authentication system (`/admin/login/`).

---

### **5. Database Structure**

The project uses PostgreSQL for the database. Below is a high-level overview of the database models:

#### **Publisher**
- `name`: The name of the publisher.

#### **Category**
- `name`: The name of the category (e.g., Fiction, Technology).

#### **Book**
- `title`: Title of the book.
- `publisher`: ForeignKey to the `Publisher` model.
- `category`: ForeignKey to the `Category` model.
- `available`: Boolean indicating if the book is available for borrowing.
- `return_date`: The date when the book will be available again (if borrowed).

#### **User**
- `email`: The user's email address.
- `first_name`: The user's first name.
- `last_name`: The user's last name.

#### **Borrowing**
- `user`: ForeignKey to the `User` model.
- `book`: ForeignKey to the `Book` model.
- `borrowed_on`: Date when the book was borrowed.
- `return_date`: Expected return date.

---

### **6. Caching and Redis**

The project leverages **Redis** for caching frequently accessed data such as book details and user information. The integration with Redis helps reduce the load on the database, ensuring faster response times.

To set up Redis, ensure the Redis server is running and update your Django settings to include:
```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

---

### **7. Testing**

Tests have been written for the core functionality of the application, including user enrollment, book listing, and borrowing actions.

To run tests:
```bash
python manage.py test
```

---

### **8. Deployment (Docker)**

The project is fully Dockerized for easy deployment. The **Docker Compose** configuration allows you to spin up the application along with PostgreSQL and Redis instances.

#### **Docker Compose Configuration:**
- **docker-compose.yml** contains configurations for the Django app, PostgreSQL, and Redis.

#### **Steps to Deploy:**
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

### **9. Future Scalability**

In the future, the project can be scaled using:
- **Auto-scaling on cloud platforms** such as AWS, with multiple instances managed behind a load balancer.
- **Database replication** for PostgreSQL to handle more reads using read replicas.
- **Horizontal scaling** using Kubernetes or Docker Swarm to add more containers as the traffic increases.
- **Use a CDN** to offload the serving of static files and media files, reducing the load on the application servers.

---

### **10. Contributing**

If you'd like to contribute to this project, feel free to fork the repository and create a pull request. Make sure to:
1. Write tests for any new features.
2. Ensure the test suite passes before submitting your pull request.
3. Follow PEP8 coding standards.

---

This documentation should provide a clear guide for developers, admins, and contributors. If you’d like to add any other sections or modify certain areas, feel free to suggest more details!
