from django.contrib import admin

# Register your models here.
from .models import Dynamic,Tag,Comment

class DynamicAdmin(admin.ModelAdmin):
    style_fields = {'description': 'ueditor'}

admin.site.register(Dynamic, DynamicAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
