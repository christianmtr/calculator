from django.conf import settings
from rest_framework import serializers

from calcs.models import Operation, Record

class OperationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ('__all__')


class RecordSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Record
        fields = ('__all__')

    def validate(self, data):
        user = data['user']
        operation = data['operation']
        user_records = Record.objects.filter(user=user)

        if user_records.count() == 0:
            data['user_balance'] = settings.DEFAULT_INITIAL_BALANCE
            return data
        else:
            last_user_record = user_records.last()

            if last_user_record.user_balance - operation.cost > 0:
                return data
            return serializers.ValidationError("You has not enought fonds.")


class OperationRequestSerializer(serializers.Serializer):
    number_one = serializers.DecimalField(max_digits=6,
                                          decimal_places=3, 
                                          required=True)
    number_two = serializers.DecimalField(max_digits=6,
                                          decimal_places=3,
                                          required=True)
    operation_type = serializers.ChoiceField(
        choices=Operation.OperationTypeChoices.choices
    )
