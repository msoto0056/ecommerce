from django.contrib import admin
#from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.utils.translation import gettext

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import GuestEmail, User

#User = get_user_model()

#class UserAdmin(admin.ModelAdmin):
class UserAdmin(BaseUserAdmin):
    search_fields=['email']
    #class Meta:  
    #   model= User
    
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
 # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin')
    list_filter = ('admin','active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','lastname',)}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email','lastname')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

class GuestEmailAdmin(admin.ModelAdmin):
    search_fields=['email']
    class Meta:
        model= GuestEmail
admin.site.register(GuestEmail,GuestEmailAdmin)

