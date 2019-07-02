from django.db import models
from django.urls import reverse
from django.utils import timezone
import django.urls.resolvers



class AHU(models.Model):
    type = models.CharField(max_length=20)


    def __str__(self):
        return str(self.type)

typ = AHU(type=('Amber','KCX'))
class Check(models.Model):
    controller = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    unit_type = models.ForeignKey(AHU, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=200)
    comment = models.TextField()
    inspection_1 = models.BooleanField(default=False)
    inspection_2 = models.BooleanField(default=False)
    inspection_3 = models.BooleanField(default=False)
    objects = models.Manager()


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