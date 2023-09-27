from django.db import models

class PaperType(models.Model):
    PAPER_TYPE_CHOICE = [
            (0, 'SHORT BOND PAPER'),
            (1, 'LONG BOND PAPER'),
            (2, 'LEGAL BOND PAPER'),
            (3, 'A4'),
            (4, 'A5'),
            (5, 'A6'),
            (6, 'A4 PHOTO PAPER'),
            (7, 'A5 PHOTO PAPER'),
            (8, 'A6 PHOTO PAPER'),
            ]
    paper_type  = models.PositiveSmallIntegerField(default=0)
    dimension   = models.CharField(max_length=32, null=True, blank=True)
