from django.db import models

class User(models.Model):

    name = models.CharField(max_length=50)
    fat = models.IntegerField(default=0)
    stupid = models.IntegerField(default=0)
    dumb = models.IntegerField(default=0)
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'