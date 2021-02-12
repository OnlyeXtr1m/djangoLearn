from django.contrib import admin
from .models import Bb, Rubric


class BbAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price", "was_published", "rubric")
    list_display_links = ("title", "description")
    search_fields = ("title", "description", )

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
