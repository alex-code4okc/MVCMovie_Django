from django.db import models

# Create your models here.

class Movie(models.Model):
    # django automatically handles id, but it can be explicitly defined
    #id = models.AutoField(primary_key=True)
    title = models.TextField()
    release_date = models.DateField()
    genre = models.TextField()
    price = models.DecimalField(max_digits=18,decimal_places=2) # 18,2

    def __str__(self):
        return f"{self.title} | {self.release_date} | {self.genre} | {self.price}"