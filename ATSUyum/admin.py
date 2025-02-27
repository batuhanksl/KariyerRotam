from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_text')  # Use a custom method for text preview
    search_fields = ('short_text',)
    readonly_fields = ('file',)

    def short_text(self, obj):
        return obj.text[:200] + "..." if len(obj.text) > 200 else obj.text  # Limit to 50 chars

    short_text.short_description = "Text Preview"  # Column name in admin panel
