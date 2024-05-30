from django.db import models

class Notice(models.Model):
    proposer = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"{self.proposer} - {self.content[:20]}"
