from django.views.generic import TemplateView
from .models import Story, MissionVision, CoreValue, Director, Stakeholder

class AboutUsView(TemplateView):
    template_name = "about/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        story_obj = Story.objects.first()
        mission_obj = MissionVision.objects.filter(type="mission").first()
        vision_obj = MissionVision.objects.filter(type="vision").first()

        context["page"] = {
            "our_story": story_obj.content if story_obj else "",
            "story_image": getattr(story_obj, "image", None) if story_obj else None,
            "mission": mission_obj.content if mission_obj else "",
            "vision": vision_obj.content if vision_obj else "",
            "core_values": CoreValue.objects.all(),
            "directors": Director.objects.all(),
            "stakeholders": Stakeholder.objects.all(),
        }

        return context
