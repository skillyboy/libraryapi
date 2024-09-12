from ninja import NinjaAPI, Schema
from books.models import Book, Borrowing, User, Publisher, Category  # Ensure models are imported from models.py
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from typing import List, Optional

api = NinjaAPI()

# Schema for listing books in Admin API (PostgreSQL)
class BookSchema(Schema):
    id: int
    title: str
    publisher: str  # Publisher name
    category: str   # Category name
    available: bool
    return_date: Optional[datetime]

# Schema for borrowing a book
class BorrowBookSchema(Schema):
    user_id: int
    book_id: int
    days: int

# Schema for creating a new user
class UserSchema(Schema):
    email: str
    first_name: str
    last_name: str

# Enroll users into the library
@api.post("/enroll-user/", response={200: str})
def enroll_user(request, data: UserSchema):
    user, created = User.objects.get_or_create(
        email=data.email,
        defaults={'first_name': data.first_name, 'last_name': data.last_name}
    )
    if created:
        return "User enrolled successfully!"
    else:
        return "User already exists!"

# List all users enrolled in the library
@api.get("/users/", response=List[UserSchema], operation_id="list_users")
def list_users(request):
    users = User.objects.all()
    return users


@api.get("/books/", response=List[BookSchema])
def list_books(request, publisher: Optional[str] = None, category: Optional[str] = None):
    books = Book.objects.filter(available=True)

    # Filter by publisher if provided
    if publisher:
        books = books.filter(publisher__name__icontains=publisher)

    # Filter by category if provided
    if category:
        books = books.filter(category__name__icontains=category)

    # Convert publisher and category to strings for the response
    return [
        {
            "id": book.id,
            "title": book.title,
            "publisher": book.publisher.name,  # Return the name of the publisher
            "category": book.category.name,    # Return the name of the category
            "available": book.available,
            "return_date": book.return_date
        }
        for book in books
    ]

# Fetch a single book by ID@api.get("/books/{book_id}", response=BookSchema)
@api.get("/books/{book_id}", response=BookSchema)
def get_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    
    return {
        "id": book.id,
        "title": book.title,
        "publisher": book.publisher.name,
        "category": book.category.name,
        "available": book.available,
        "return_date": book.return_date
    }



# Borrow a book
@api.post("/borrow/", response={200: str})
def borrow_book(request, data: BorrowBookSchema):
    user = get_object_or_404(User, id=data.user_id)
    book = get_object_or_404(Book, id=data.book_id, available=True)
    
    Borrowing.objects.create(
        user=user,
        book=book,
        return_date=datetime.now() + timedelta(days=data.days)
    )
    
    book.available = False
    book.save()
    
    return f"Book borrowed successfully for {data.days} days!"

# List all borrowed books with return dates
@api.get("/borrowed-books/", response=List[BookSchema])
def borrowed_books(request):
    # Query borrowings with related book data
    borrowings = Borrowing.objects.select_related('book').filter(book__available=False)
    
    # Return the associated book details for each borrowing
    return [
        {
            "id": borrowing.book.id,  # Get the book's ID
            "title": borrowing.book.title,  # Get the book's title
            "publisher": borrowing.book.publisher.name,  # Get the publisher's name
            "category": borrowing.book.category.name,  # Get the category's name
            "available": borrowing.book.available,  # Get availability status
            "return_date": borrowing.return_date  # Get the return date from Borrowing model
        }
        for borrowing in borrowings
    ]



# Fetch/List the books that are not available for borrowing@api.get("/unavailable-books/", response=List[BookSchema])
def list_unavailable_books(request):
    # Get all borrowings where books are unavailable (book is borrowed)
    borrowings = Borrowing.objects.select_related('book').filter(book__available=False)

    # Return the associated book details for each borrowing
    return [
        {
            "id": borrowing.book.id,  # Access the book's ID
            "title": borrowing.book.title,  # Access the book's title
            "publisher": borrowing.book.publisher.name,  # Access the publisher's name
            "category": borrowing.book.category.name,  # Access the category's name
            "available": borrowing.book.available,  # Get availability status
            "return_date": borrowing.return_date  # Get the return date from Borrowing model
        }
        for borrowing in borrowings
    ]
