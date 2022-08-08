from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200, null=False, blank=True)
    picture = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.name






