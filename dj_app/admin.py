from django.contrib import admin

from .models import User, Request

class User_admin(admin.ModelAdmin):
    readonly_fields = ('user_id',)

class Request_admin(admin.ModelAdmin):
    readonly_fields = ('request_id',)

admin.site.register(User, User_admin)
admin.site.register(Request, Request_admin)