from django.db import models

class Projects(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField(upload_to='media',null=True,blank=True)
    description=models.TextField()
    github_url=models.URLField(max_length=200)
    
    def __str__(self):
        return self.title
    