from django.db import models
from django.utils import timezone


class VulnItem(models.Model):
    vuln_name = models.CharField(max_length=100)
    risk_level = models.CharField(max_length=100)
    affected_assets = models.CharField(max_length=100)
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.vuln_name}"
