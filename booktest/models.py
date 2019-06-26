from django.db import models


# Create your models here.
class BookInfo(models.Model):
    b_title = models.CharField(max_length=20)
    b_pub_date = models.DateTimeField()

    def __str__(self):
        return self.b_title


class HeroInfo(models.Model):
    h_name = models.CharField(max_length=10)
    h_gender = models.BooleanField()
    h_content = models.CharField(max_length=1000)
    h_book = models.ForeignKey(BookInfo, on_delete=True)

    def __str__(self):
        return self.h_name
