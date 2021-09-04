from django.db import models


class User(models.Model):

    # We will not create id, because Django creates this attribute by default
    # id = models.IntegerField(primary_key=True)

    # First and Last names - simple Char fields. 100 characters must be anough
    #    to fit 99.999% of names.
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # Email - obvously, Email field.
    email = models.EmailField()


class Transaction(models.Model):

    # We will not create id, because Django creates this attribute by default
    # id = models.IntegerField(primary_key=True)

    # User ID - foreign key, that mask be linked to the User object. Therefore,
    #    by deleting User object service must delete all their transaction
    #    records as well.  
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # Amount - simple float field, amount is not required to be integer
    amount = models.FloatField()

    # Date - Datetime field which will by default will have value 
    #   datetime.now(). `auto_now_add` parameter enables default feature
    #   only at the moment of record addition.
    date = models.DateTimeField(auto_now_add=True)
