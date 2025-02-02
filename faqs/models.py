from django.db import models
from ckeditor.fields import RichTextField
from .utils import translate_text


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    # Translations
    question_hi = models.TextField(blank=True, null=True)  # Hindi
    question_bn = models.TextField(blank=True, null=True)  # Bengali
    answer_hi = RichTextField(blank=True, null=True)  # Hindi
    answer_bn = RichTextField(blank=True, null=True)  # Bengali

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """Auto-translate FAQs before saving."""
        if not self.question_hi:
            self.question_hi = translate_text(self.question, "hi")
        if not self.question_bn:
            self.question_bn = translate_text(self.question, "bn")

        if not self.answer_hi:
            self.answer_hi = translate_text(self.answer, "hi")
        if not self.answer_bn:
            self.answer_bn = translate_text(self.answer, "bn")

        super().save(*args, **kwargs)  # Call the original save method

    def __str__(self):
        return self.question
