from django.db import models

# Publisher model
class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Category model
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Book model
class Book(models.Model):
    title = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

# User model
class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Borrowing model
class Borrowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_on = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.first_name} borrowed {self.book.title}"

    # Check if the book has been returned (based on availability status)
    def is_returned(self):
        return self.book.available
