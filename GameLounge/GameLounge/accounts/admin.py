from django.contrib import admin
from django.contrib.auth.models import Group
from .models import ProfileModel


def set_users_to_staff(modeladmin, request, queryset):
    group = 'legati'
    selected_group = Group.objects.get(name=group)
    for user in queryset:
        user.groups.set([selected_group])
        user.is_staff = True
        user.save()
    modeladmin.message_user(request, f"{queryset.count()} users promoted to staff.")


def set_staff_to_users(modeladmin, request, queryset):
    group = 'citizens'
    selected_group = Group.objects.get(name=group)
    for user in queryset:
        user.groups.set([selected_group])
        user.is_staff = False
        user.save()
    modeladmin.message_user(request, f"{queryset.count()} staff members reverted to users.")


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'email', 'age', 'date_joined', 'is_staff')
    list_filter = ('is_staff', 'is_superuser')
    actions = [set_users_to_staff, set_staff_to_users]

