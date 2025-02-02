import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from faqs.models import FAQ


@pytest.mark.django_db
def test_get_faqs():
    """Test API returns FAQs in English by default."""
    FAQ.objects.create(
        question="What is Django?", answer="Django is a Python framework."
    )

    client = APIClient()
    response = client.get(reverse("faq-list"))  # Assuming 'faq-list' is your URL name

    assert response.status_code == 200
    assert "What is Django?" in response.data[0]["question"]
