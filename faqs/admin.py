from django.contrib import admin
from .models import FAQ


class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "created_at")  # Display columns in list view
    search_fields = ("question", "answer")  # Enable search
    list_filter = ("created_at",)  # Add a filter sidebar
    readonly_fields = (
        "question_hi",
        "answer_hi",
        "question_bn",
        "answer_bn",
    )  # Prevent manual translation edits


admin.site.register(FAQ, FAQAdmin)
