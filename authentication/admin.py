import django.contrib.auth.admin
from django.contrib import admin

from .forms import UserCreationForm, UserChangeForm
from users.models import User

class UserAdmin(django.contrib.auth.admin.UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    
    list_display = ('username', 'is_admin', 'is_active', 'last_login')
    list_filter = ('is_admin', 'is_active')

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Profile', {
            'fields': (
                'first_name', 'last_name', 
                'email', 'address', 
                'phone_number'
            )
        }),
        ('Permissions', {
            'fields': ('is_admin', 'is_active')
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'first_name', 'last_name',
                'email', 'address', 'phone_number',
                'password1', 'password2'
            ),
        }),
    )

    filter_horizontal = ()

admin.site.register(User, UserAdmin)
