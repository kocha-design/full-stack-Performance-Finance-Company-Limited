from django.shortcuts import render
from .models import Policy

from types import SimpleNamespace

def privacy_policy_page(request):
    

    policies = {}
    for policy_type, _ in Policy.POLICY_TYPES:
        try:
            policy = Policy.objects.get(policy_type=policy_type, is_active=True)
            policies[f"{policy_type}_policy"] = policy
        except Policy.DoesNotExist:
            policies[f"{policy_type}_policy"] = SimpleNamespace(
                content=f'<p>No {policy_type.replace("_", " ")} content available.</p>'
            )

    return render(request, 'policies/privacy_policy.html', policies)
