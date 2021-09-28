from django.db import models


class Poverka(models.Model):
    org_title = models.CharField(max_length=1024)
    mit_number = models.CharField(max_length=32)
    mit_title = models.CharField(max_length=256)
    mit_notation = models.CharField(max_length=512)
    mi_modification = models.CharField(max_length=128)
    mi_number = models.CharField(max_length=128)
    verification_date = models.CharField(max_length=32)
    valid_date = models.CharField(max_length=32)
    result_docnum = models.CharField(max_length=128)
    applicability = models.CharField(max_length=10)

    def __str__(self):
        return f'ID {self.id}: {self.mit_title}'
