from django.views.generic import ListView
from django.db.models import Count
from .models import VulnItem


class AllVulnerabilities(ListView):
    model = VulnItem
    template_name = "vuln_man/Vulnerabilities.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get counts of each risk level
        context['critical_count'] = VulnItem.objects.filter(risk_level='Critical').count()
        context['high_count'] = VulnItem.objects.filter(risk_level='High').count()
        context['medium_count'] = VulnItem.objects.filter(risk_level='Medium').count()
        context['low_count'] = VulnItem.objects.filter(risk_level='Low').count()
        context['remediated_count'] = VulnItem.objects.filter(risk_level='Remediated').count()
        return context


class HostView(ListView):
    model = VulnItem
    template_name = "vuln_man/hosts.html"

