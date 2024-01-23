from django.db import models
class newplace (models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    address = models.TextField()
    state = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    Account1 = models.CharField(max_length=255)
    Debit = models.CharField(max_length=255)
    Credit = models.CharField(max_length=255)
    Cheque = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name