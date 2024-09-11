from django.contrib import admin
from .models import Book, Borrowing, User, Publisher, Category

# Register Publisher, Category, Book, User, Borrowing to the admin interface
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'category', 'available', 'return_date')
    search_fields = ('title', 'publisher__name', 'category__name')
    list_filter = ('available', 'category', 'publisher')

@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'borrowed_on', 'return_date', 'is_returned')
    search_fields = ('book__title', 'user__email')
    list_filter = ('return_date',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
