from .models import Policy
from django.shortcuts import get_object_or_404
from django.shortcuts import render

def dynamic_policy(request, slug):
    policy = get_object_or_404(Policy, slug=slug)
    return render(request, 'legal/policy_page.html', {
        'title': policy.title,
        'content': policy.content
    })
