from django.contrib import admin
from withinstory.app.models import UserProfile, Story


class UserProfileAdmin(admin.ModelAdmin):
    fields = ('name', 'username', 'email',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Story)
