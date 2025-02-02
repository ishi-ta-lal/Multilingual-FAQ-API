import pytest
from faqs.models import FAQ


@pytest.mark.django_db
def test_faq_auto_translation():
    """Test that FAQs are automatically translated upon saving."""
    faq = FAQ.objects.create(
        question="What is Django?", answer="Django is a Python web framework."
    )

    assert faq.question_hi is not None  # Ensure translation exists
    assert faq.answer_hi is not None
    assert faq.question_bn is not None
    assert faq.answer_bn is not None
