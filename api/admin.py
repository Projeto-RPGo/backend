from django.contrib import admin

from api.models.user import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    UserAdmin is a ModelAdmin class that is used to customize the Django admin interface for the User model.
    This class includes a list_display attribute that specifies which fields to display in the admin interface.
    Attributes:
        list_display (tuple): A tuple of field names to display in the admin interface.
    """
    list_display = ('first_name', 'last_name', 'username', 'email', 'date_joined')
