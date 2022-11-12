from django.db import models
import uuid


# Create your models here.

class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    projects = models.ManyToManyField('Project')

    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # featured_image
    tags = models.ManyToManyField(Tag, blank=True)
    demo_link = models.CharField(max_length=1000, null=True, blank=True)
    source_link = models.CharField(max_length=1000, null=True, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' ' + str(self.id)


class Review(models.Model):
    VOTE_TYPE = {
        ('up', 'up'),
        ('down', 'down')
    }
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    # owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.value
