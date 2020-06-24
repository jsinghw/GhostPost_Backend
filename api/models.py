from django.db import models
from django.utils import timezone


class Post(models.Model):
    Boast = 'B'
    Roast = 'R'
    BOAST_OR_ROAST_CHOICES = [
        (Boast, 'Boast'),
        (Roast, 'Roast'),
    ]

    boast_or_roast = models.CharField(
        max_length=1,
        choices=BOAST_OR_ROAST_CHOICES
    )
    content = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content

    @property
    def vote_score(self):
        return (self.upvotes - self.downvotes)
