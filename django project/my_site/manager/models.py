from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class UserReservations(models.Model):
    mobile_re = RegexValidator(regex=r'^(\d{3}(- .)?{2}\d{4}$', message='Wrong phone number')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, validators=[mobile_re])
    message = models.TextField(max_length=500)

    is_processed = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-data', )

    def __str__(self):
        return f'{self.name}: {self.phone}: {self.message[:20]}'
