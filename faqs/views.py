from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ
from .serializers import FAQSerializer


class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get("lang", "en")  # Default to English
        cache_key = f"faqs_{lang}"  # Unique cache key per language
        cached_faqs = cache.get(cache_key)

        if cached_faqs:
            return Response(cached_faqs, status=status.HTTP_200_OK)

        # If not cached, fetch from DB
        faqs = FAQ.objects.all()
        for faq in faqs:
            if lang == "hi":
                faq.question = faq.question_hi or faq.question
                faq.answer = faq.answer_hi or faq.answer
            elif lang == "bn":
                faq.question = faq.question_bn or faq.question
                faq.answer = faq.answer_bn or faq.answer

        serializer = FAQSerializer(faqs, many=True)
        cache.set(cache_key, serializer.data, timeout=60 * 5)  # Cache for 5 minutes

        return Response(serializer.data, status=status.HTTP_200_OK)
