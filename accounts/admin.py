from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from .models import Account, UserProfile

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')

admin.site.register(Account,AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)








from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import DeliveryBoy

class DeliveryBoyAdmin(UserAdmin):
    filter_horizontal = ()
    list_display = ('name', 'email', 'phone_number', 'address', 'vehicle_no', 'license_no', 'is_active', 'is_deliveryboy')
    list_filter = ('is_active', 'is_deliveryboy')
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password')}),
        ('Contact Information', {'fields': ('phone_number', 'address')}),
        ('Delivery Information', {'fields': ('vehicle_no', 'license_no')}),
        ('Permissions', {'fields': ('is_active', 'is_deliveryboy')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'phone_number', 'address', 'vehicle_no', 'license_no', 'password1', 'password2', 'is_active', 'is_deliveryboy'),
        }),
    )

    ordering = ('email',)  # Specify the field to use for ordering

admin.site.register(DeliveryBoy, DeliveryBoyAdmin)

