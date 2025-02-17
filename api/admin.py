from django.contrib import admin

from api.models.user import User
from api.models.world import World


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    UserAdmin is a ModelAdmin class that is used to customize the Django admin interface for the User model.
    This class includes a list_display attribute that specifies which fields to display in the admin interface.
    Attributes:
        list_display (tuple): A tuple of field names to display in the admin interface.
    """
    list_display = ('id', 'username', 'first_name', 'last_name',
                    'email', 'date_joined', 'last_login')


@admin.register(World)
class WorldAdmin(admin.ModelAdmin):
    """
    WorldAdmin is a ModelAdmin class that is used to customize the Django admin interface for the World model.
    This class includes a list_display attribute that specifies which fields to display in the admin interface.
    Attributes:
        list_display (tuple): A tuple of field names to display in the admin interface.
    """
    list_display = ('id', 'name', 'description')
