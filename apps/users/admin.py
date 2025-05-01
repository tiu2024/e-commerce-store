from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import EstoreUser


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = EstoreUser
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = EstoreUser
        fields = ('username', 'email', 'user_type')


@admin.register(EstoreUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ('username', 'first_name', 'last_name', 'user_type', 'date_joined')
    list_filter = ('user_type', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('-date_joined',)