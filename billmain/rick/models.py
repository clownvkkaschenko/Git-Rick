from django.db import models


class Profile(models.Model):
    url_profile = models.CharField(max_length=200)
    rick_name = models.CharField(max_length=70)
    rick_image = models.CharField(max_length=70)
    rick_species = models.CharField(max_length=70)
    rick_status = models.CharField(max_length=70)
    rick_location = models.CharField(max_length=70)
    rick_first_episode = models.CharField(max_length=70)

    def __str__(self):
        return self.url_profile
