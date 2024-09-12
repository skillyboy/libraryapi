from django.test import TestCase
from books.models import Book, Publisher, Category, User
from rest_framework.test import APITestCase  # Import APITestCase
from django.urls import reverse

# Unit Tests for Models
class BookModelTest(TestCase):
    def setUp(self):
        self.publisher = Publisher.objects.create(name="Test Publisher")
        self.category = Category.objects.create(name="Test Category")
        self.book = Book.objects.create(
            title="Test Book", publisher=self.publisher, category=self.category, available=True
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.publisher.name, "Test Publisher")
        self.assertEqual(self.book.category.name, "Test Category")
        self.assertTrue(self.book.available)

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="testuser@example.com", first_name="Test", last_name="User")

    def test_user_creation(self):
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertEqual(self.user.first_name, "Test")
        self.assertEqual(self.user.last_name, "User")


# Integration Tests for APIs
class UserAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="testuser@example.com", first_name="Test", last_name="User")

    def test_enroll_user(self):
        url = reverse('enroll_user')
        data = {
            "email": "newuser@example.com",
            "first_name": "New",
            "last_name": "User"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)

class UserAPITest(APITestCase):
    def test_list_users(self):
        url = "/api/users/"  # Directly use the full path
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
