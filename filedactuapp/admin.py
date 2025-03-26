# Register your models here.
from django.contrib import admin

from .models import Messages


class MessagesAdmin(admin.ModelAdmin):
    list_display = ["contents", "users"]


admin.site.register(Messages, MessagesAdmin)
