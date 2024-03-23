from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    iin = models.CharField(max_length=12)
    udo = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)

    def __str__(self):
        return (f"{self.last_name} {self.first_name} {self.middle_name} \nIIN: {self.iin} \nPHONE: {self.phone}")
    