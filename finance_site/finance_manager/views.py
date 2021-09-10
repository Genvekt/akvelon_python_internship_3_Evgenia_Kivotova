from django.db.models import Sum
from rest_framework import generics, permissions
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response

from .models import User, Transaction
from .serialisers import UserDetailSerialiser, UsersListSerialiser
from .serialisers import TransactionDetailSerialiser, TransactionCreateSerialiser, TransactionGroupSerialiser
from .permitions import IsMeOrReadOnly, IsOwner

from .utils import fibonacci


class UsersListView(generics.ListAPIView):
    """
    Endpoint for listing all users.
    """
    serializer_class = UsersListSerialiser
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint for listing and modifying one user information.
    """
    serializer_class = UserDetailSerialiser
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsMeOrReadOnly]


class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint for listing and modifying one transaction information.
    """
    serializer_class = TransactionDetailSerialiser
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    queryset = Transaction.objects.all()


class TransactionCreateView(generics.CreateAPIView):
    """
    Endpoint for transaction creation.
    """
    serializer_class = TransactionCreateSerialiser
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):

        request.data["user_id"] = request.user
        transaction = self.serializer_class(data=request.data,
                                            context={'request': request})

        if transaction.is_valid():
            transaction.save()
        return Response(status=201)


class TransactionsListView(APIView):
    """
    Endpoint for listing all user transactions.
    Avaivable UTM parameters:
        - date = YYYY-MM-DD : Select transactions, made in specific date.
        - type = income / outcome : Select transactions based on amount sign.
        - sort_date = True / true /  : Sort result by date
        - sort_amount = True / true / : Sort result by amount

        If both sort_date and sort_amount are provided, 
        sort by date is performed first.
    """
    serializer_class = TransactionDetailSerialiser
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        GET request processor
        """
        # Filter current user transactions
        transactions = Transaction.objects.filter(user_id=request.user.id)

        # Filter by date
        date = request.GET.get('date')
        if date:
            try:
                transactions = transactions.filter(date=date)
            except:
                return Response(status=401, data={
                    'Wrong parameter':'Date parameters must be in YYYY-MM-DD format.'
                })
        
        # Filter by type
        type = request.GET.get('type')
        if type and type in ['income', 'outcome']:
            if type == 'income':
                transactions = transactions.filter(amount__gt=0.0)
            else:
                transactions = transactions.filter(amount__lt=0.0)

        # Sort by date and/or amount
        sort_date = request.GET.get('sort_date')
        sort_amount = request.GET.get('sort_amount')

        sort_date = sort_date in ['True', 'true']
        sort_amount = sort_amount in ['True', 'true']

        if sort_date and sort_amount:
            transactions = transactions.order_by('date', 'amount')

        elif sort_date:
            transactions = transactions.order_by('date')
        
        elif sort_amount:
            transactions = transactions.order_by('amount')

        # Create json response
        serialiser = self.serializer_class(transactions, many=True)
        return Response(serialiser.data)


class TransactionsListGroupedView(APIView):
    """
    Endpoint for grouping transactions by date.
    Avaivable UTM parameters:
        - start = YYYY-MM-DD : starting date of range. Default is 1000-01-01
        - end = YYYY-MM-DD: ending date of range. Default is 9999-12-31

    """
    serializer_class = TransactionGroupSerialiser
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        GET request processor
        """

        # Retrieve range UTM parameters
        start = request.GET.get('start') or "1000-01-01"
        end = request.GET.get('end') or "9999-12-31"

        # Filter data and sum groups
        try:
            transaction_groups = Transaction.objects.filter(
                    user_id=request.user.id,
                    date__range=[start, end]
            ).values('date').annotate(amount_sum=Sum('amount'))
               
        except:
            return Response(status=401, data={
                    'Wrong parameter':'Date parameters must be in YYYY-MM-DD format.'
                })

        # Generate json responce
        resp = []
        for group in transaction_groups:
            resp.append({
                'amount_sum': group['amount_sum'],
                'date': group['date']
            })
        return Response(resp)


class FibonacciView(APIView):
    """
    Endpoint for fibonacci function test
    """
    def get(self, request, n:int):
        """
        GET request processor
        """
        # Calculate fibonacci
        fibonacci_res = fibonacci(n)
        if not fibonacci_res:
            return Response(data={"Function is not defined for provided input."})
        return Response(data={"N'th fibonacci number": fibonacci_res})