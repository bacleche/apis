from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile, Badge, Level, Achievement


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'level',
        'xp',
        'is_staff',
        'is_active',
        'date_joined',
    )

    list_filter = ('is_staff', 'is_active', 'level')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)

    fieldsets = (
        ('Informations principales', {
            'fields': ('username', 'email', 'password')
        }),
        ('Progression', {
            'fields': ('xp', 'level')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    extra = 0


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('level_number', 'required_xp', 'created_at')
    ordering = ('level_number',)

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'badge',
        'date_earned',
    )
    list_filter = ('badge',)
    search_fields = ('user__username', 'badge__name')
