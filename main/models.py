from django.db import models


class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published')

    def __str__(self):
        return self.tutorial_title
