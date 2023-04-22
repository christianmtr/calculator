from django.db import models

from calcs.managers import SoftDeleteManager


class SoftDeleteModel(models.Model):
    deleted = models.BooleanField(
        default=False,
        null=False,
    )
    objects = SoftDeleteManager()

    def delete(self, using, keep_parents):
        self.deleted = True
        return self.save()


class Operation(SoftDeleteModel):

    class OperationTypeChoices(models.TextChoices):
        SUM = ''

    operation_type = models.CharField(
        max_length=2,
        choices=OperationTypeChoices.choices,
        default=OperationTypeChoices.SUM,
    )
    cost = models.DecimalField(
        max_digits=6,
        decimal_places=3,
    )


class Record(SoftDeleteModel):
    operation = models.ForeignKey(
        'Operation',
        null=False,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'auth.User',
        null=False,
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        max_digits=6,
        decimal_places=3,
    )
    user_balance = models.DecimalField(
        max_digits=7,
        decimal_places=3,
    )
    operation_response = models.CharField(
        max_length=10,
        null=True,
    )
    date = models.DateTimeField(auto_now_add=True)

