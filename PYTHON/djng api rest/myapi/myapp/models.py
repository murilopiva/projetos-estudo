from django.db import models

# Create your models here.


class Music(models.Model):

    class Meta:

        db_table = 'music'

    title = models.CharField(max_length=200)
    seconds = models.IntegerField()


    def __str__(self):
        return self.title
    
class Lista(models.Model):

    class Meta:

        db_table = 'lista'

    id_Compra = models.IntegerField()
    wppnmr = models.IntegerField()
    ds_compra = models.CharField(max_length=200)


    def __str__(self):
        return self.wppnmr
