from django.db import models
from apps.users.models import User
from apps.core.models import BaseModel


class Report(BaseModel):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports_made")
    content_type = models.CharField(max_length=50)
    reason = models.TextField()
    status = models.CharField(max_length=20, default="pending")

    def __str__(self):
        return f"Report {self.id} by {self.reporter.username}"


class Flag(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="flags")
    content_type = models.CharField(max_length=50)
    reason = models.TextField()
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Flag {self.id} by {self.user.username}"


class Ban(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bans")
    reason = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Ban {self.id} - {self.user.username}"


class Warning(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="warnings")
    reason = models.TextField()
    acknowledged = models.BooleanField(default=False)

    def __str__(self):
        return f"Warning {self.id} - {self.user.username}"
