from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.forms import UserCreateForm, UserEditForm
from django.utils.translation import ugettext_lazy as _
from users.models import User
from django.contrib.auth.models import Group


class RUserAdmin(UserAdmin):
    form = UserEditForm
    add_form = UserCreateForm
    fieldsets = (
        (_('User'), {'fields': ('email', 'login', 'password', 'first_name', 'middle_name',
                                'third_name', 'avatar', 'is_admin', 'number')}),
        (_('Permissions'),  {'fields': ('is_active', 'is_admin', 'is_superuser',)}),
    )
    list_display = ('id', 'login', 'get_full_name', 'number',)
    list_filter = ('is_admin',)
    search_fields = ('email',)
    ordering = ('id',)


admin.autodiscover()
admin.site.register(User, RUserAdmin)
admin.site.unregister(Group)