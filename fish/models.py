from django.db import models

class capitan(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    PhoneNumber = models.IntegerField()

    class Meta:
        db_table = 'capitan'

    def __str__(self):
        return(f"{self.name} {self.surname}")

class trawler(models.Model):
    name = models.CharField(max_length=20)
    spaciousness = models.IntegerField()

    class Meta:
        db_table = 'trawler'

    def __str__(self):
        return(f"{self.name} {self.spaciousness}")


class navigation(models.Model):
    date_navigation = models.DateField()
    catch = models.IntegerField()
    capitan =models.ForeignKey(capitan,on_delete=models.CASCADE,default="none")
    trawler = models.ForeignKey(trawler,on_delete=models.CASCADE,default="none")

    class Meta:
        db_table = 'navigation'

