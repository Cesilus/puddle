from django.http import JsonResponse
from .models import FAQ

def chatbot_response(request):
    user_message = request.GET.get('message', '')
    if not user_message:
        return JsonResponse({'response': 'Please ask a question.'})
    
    faqs = FAQ.objects.all()
    for faq in faqs:
        if user_message.lower() in faq.question.lower():
            return JsonResponse({'response': faq.answer})

    return JsonResponse({'response': "I'm sorry, I don't understand your question. Please rephrase or ask something else."})
