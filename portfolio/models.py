from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    # the title field in here is a specific role or designation of a user .
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='userProfile/', null=True)
    summary = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250, 
                                   null=True,
                                   blank=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)

    def __str__(self):
        return f"Image for {self.project.title if self.project else 'unknown Project'}"

class Experience(models.Model):

    profile = models.ForeignKey(Profile, 
                                on_delete=models.CASCADE,
                                related_name='experiences')
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.title} at {self.company}"