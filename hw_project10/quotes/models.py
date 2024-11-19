from django.db import models
import json


class Author(models.Model):
    fullname = models.CharField(unique=True, null=False, max_length=150)
    born_date = models.CharField(max_length=50)
    born_location = models.CharField(max_length=150)
    description = models.CharField()

    def __str__(self):
        return f"{self.fullname}"

class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    tags = models.CharField(max_length=300)
    quote = models.CharField()

    def set_tags(self, x):
        self.tags = json.dumps(x)

    def get_tags(self):
        return json.loads(self.tags)

    def __str__(self):
        return f"{self.quote}"
