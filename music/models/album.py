from django.db import models



class Album(models.Model):
    artist = models.ForeignKey('music.Artist', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=True)
    cover = models.URLField(blank=True)
    
    def __str__(self) -> str:
        return self.title