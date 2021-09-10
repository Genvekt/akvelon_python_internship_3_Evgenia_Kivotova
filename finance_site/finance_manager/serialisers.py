from rest_framework import serializers
from .models import User, Transaction


class UserDetailSerialiser(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email')


class UsersListSerialiser(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class TransactionDetailSerialiser(serializers.ModelSerializer):
    user_id = serializers.StringRelatedField()
    class Meta():
        model = Transaction
        fields = "__all__"

class TransactionGroupSerialiser(serializers.ModelSerializer):
    class Meta():
        model = Transaction
        fields = ("date", "amount_sum")

class TransactionCreateSerialiser(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta():
        model = Transaction
        fields = ('date','amount','user_id')

