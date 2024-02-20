from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(BaseModel):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    

STATUS_CHOICES = [
        ('open', 'open'),
        ('in_progress', 'in Progress'),
        ('closed', 'Closed'),
]

PRIORITY_CHOICES = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
]

class Attachment(BaseModel):
    file = models.FileField(upload_to="attachments/")
    def __str__(self):
        return self.file.name


class Issue(BaseModel):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length = 20, choices=STATUS_CHOICES, default='open')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='low')
    attachment = models.ManyToManyField(Attachment, related_name='attached_issues', null=True)

class Comments(BaseModel):
    text = models.CharField(max_length=200)
    file = models.FileField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
