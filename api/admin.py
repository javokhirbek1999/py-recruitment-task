from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import events, reservation, tickets, users


# Register your models here.
class UserConfig(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'username', 'is_active', 'is_superuser', 'date_joined', 'date_updated']
    fieldsets = (
        (None, {'fields': ('email', 'username')}),
        (_('Permissions'),{'fields': ('is_active','is_staff','is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username','password1','password2')
        })
    )


admin.site.register(users.User, UserConfig)
admin.site.register(events.Event)
admin.site.register(events.Building)
admin.site.register(events.Seat)
admin.site.register(events.Venue)
admin.site.register(tickets.Ticket)
admin.site.register(reservation.Reservation)
