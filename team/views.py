from django.shortcuts import render
from .models import TeamMember

def team_page(request):
    members = TeamMember.objects.all()
    return render(request, 'team/team.html', {'members': members})
