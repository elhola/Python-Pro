from django.db import models


# Create your models here.

class About(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content


class WhyUs(models.Model):
    section_title = models.CharField(max_length=20)

    def __str__(self):
        return self.section_title


class Menu(models.Model):
    categories = models.CharField(max_length=20)
    dishes = models.CharField(max_length=20)

    def __str__(self):
        return self.dishes


class Specials(models.Model):
    check_filter = models.CharField(max_length=20)

    def __str__(self):
        return self.check_filter


class Events(models.Model):
    conte = models.CharField(max_length=100)

    def __str__(self):
        return self.conte
