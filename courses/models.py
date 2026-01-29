from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

User = get_user_model()

class Course(models.Model):
    title = models.CharField(max_length=200)
    description	 =models.TextField(blank=True, null=True)
    duration_weeks = models.PositiveIntegerField(
         validators=[MinValueValidator(1)]
         )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

