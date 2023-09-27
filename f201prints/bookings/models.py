from django.db                  import models
from django.utils               import timezone

from shop.models                import PaperType

import uuid, string


def generate_unique_identifier(length: int = 3):
    last_booking = Booking.objects.order_by('-identifier').first()

    if last_booking:
        last_id = last_booking.pk
    else:
        last_id = 0

    random_string = str(uuid.uuid4().hex)[:2]
    next_id = base36_encode(last_id + 1).rjust(3, '0')

    unique_identifer = f"{next_id}{random_string}"

    return unique_identifer

def base36_encode(number: int) -> str:
    alphabet = string.digits + string.ascii_lowercase
    base36 = []
    
    while number > 0:
        number, index = divmod(number, 36)
        base36.append(alphabet[index])

    return ''.join(reversed(base36))


class Booking(models.Model):
    STATUS_CHOICES = [
            (0, 'PENDING'),
            (1, 'ACCEPTED'),
            (2, 'PRINTING'),
            (3, 'COMPLETED'),
            (4, 'DENIED'),
            ]
    METHOD_OF_PAYMENT_CHOICES = [
            (0, 'CASH'),
            (1, 'GCASH'),
            (2, 'MAYA'),
            ]
    identifier              = models.CharField(max_length=5, unique=True, default=generate_unique_identifier)
    description             = models.TextField(max_length=300, null=True, blank=True)
    original_cost           = models.IntegerField(null=True, blank=True)
    discount                = models.IntegerField(null=True, blank=True)
    amount_to_pay           = models.IntegerField(null=True, blank=True)
    status                  = models.PositiveSmallIntegerField(default=0)
    is_paid                 = models.BooleanField(default=False)
    method_of_payment       = models.PositiveSmallIntegerField(default=0)
    # checksum                = models.
    are_files_deleted       = models.BooleanField(default=False)
    date_added              = models.DateTimeField(default=timezone.now)
    date_modified           = models.DateTimeField(auto_now=True)
    date_soft_deleted       = models.DateTimeField(null=True, blank=True)
    expected_delivery_time  = models.DateTimeField(null=True, blank=True)

    def delete(self):
        """
        This flags a booking request as "deleted".
        """

        self.date_soft_deleted = timezone.now()
        self.save()

    def undelete(self):
        """
        This unflags a booking request from being deleted.
        """

        self.date_soft_deleted = None
        self.save()

    def is_deleted(self) -> bool:
        """
        Returns True if the booking request is deleted.
        """

        return self.date_soft_deleted is not None

    def save(self, *args, **kwargs):
        """
        Override the save method to update the modification date.
        """

        self.date_modified = timezone.now()
        super().save(*args, **kwargs)

class UploadedFile(models.Model):
    STATUS_CHOICES = [
            (0, 'PENDING'),
            (1, 'PRINTING'),
            (2, 'COMPLETE'),
            ]
    booking         = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="uploaded_files")
    file            = models.FileField(upload_to='uploads/')
    description     = models.TextField(max_length=300, null=True, blank=True)
    status          = models.PositiveSmallIntegerField(default=0)

class FilePage(models.Model):
    COLOR_CHOICES = [
            (0, 'STANDARD'),
            (1, 'HIGH'),
            (2, 'LOW'),
            ]
    file        = models.ForeignKey(UploadedFile, on_delete=models.CASCADE, related_name="pages_to_print")
    quantity    = models.PositiveSmallIntegerField(default=1)
    color       = models.PositiveSmallIntegerField(default=0)
    quality     = models.PositiveSmallIntegerField(default=0)
    # paper_type  = models.ForeignKey(PaperType, on_delete=models.CASCADE, related_name="paper_type")
    # paper_type  = models.ForeignKey(PaperType, on_delete=models.CASCADE, related_name="paper_type")
    paper_type  = models.CharField(max_length=16, null=True, blank=True)
    pages       = models.CharField(max_length=100, default='ALL')
    comment     = models.TextField(max_length=100, null=True, blank=True)
