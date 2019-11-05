from django.contrib import admin
from django.db import models
from .models import Tutorial
from tinymce.widgets import TinyMCE


class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["tutorial_title", "tutorial_published"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
    }
admin.site.register(Tutorial, TutorialAdmin)
