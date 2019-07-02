from django.db import models
from django.urls import reverse
from django.utils import timezone
import django.urls.resolvers





class Amber (models.Model):

    controller = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=200)
    objects = models.Manager()
    inspection_1 = models.BooleanField(default=False)
    inspection_2 = models.BooleanField(default=False)
    inspection_3 = models.BooleanField(default=False)
    inspection_4 = models.BooleanField(default=False)
    inspection_5 = models.BooleanField(default=False)
    inspection_6 = models.BooleanField(default=False)
    comments= models.TextField(default="")

    checked_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.checked_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.serial_number)

    def get_absolute_url(self):
        return reverse('quality_control:detali_report',
                       args =[self.checked_date.year,
                              self.checked_date.strftime('%m'),
                              self.checked_date.strftimw('%d')])




class KCX (models.Model):

    controller = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=200)
    objects = models.Manager()
    inspection_1 = models.BooleanField(default=False)
    inspection_2 = models.BooleanField(default=False)
    inspection_3 = models.BooleanField(default=False)
    inspection_4 = models.BooleanField(default=False)
    inspection_5 = models.BooleanField(default=False)
    inspection_6 = models.BooleanField(default=False)
    comments= models.TextField(default="")

    checked_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.checked_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.serial_number)

    def get_absolute_url(self):
        return reverse('quality_control:detali_report',
                       args =[self.checked_date.year,
                              self.checked_date.strftime('%m'),
                              self.checked_date.strftimw('%d')])

