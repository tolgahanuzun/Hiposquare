from django.contrib import admin
from .models import Square
# Register your models here.


class DateAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Square, DateAdmin)