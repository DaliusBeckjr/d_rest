from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.FloatField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f""" movie object
    id: {self.id}
    Title: {self.title}
    Description: {self.description}
    Release date: {self.release_date}
    Duration: {self.duration} """