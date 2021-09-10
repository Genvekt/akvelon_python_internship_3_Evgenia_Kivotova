from django.urls import path
from .views import UsersListView, UserDetailView, \
    TransactionCreateView, TransactionsListView, TransactionDetailView, \
        TransactionsListGroupedView, FibonacciView


urlpatterns = [
    path('users/', UsersListView.as_view()),
    path('user/<int:pk>', UserDetailView.as_view()),
    path('transactions', TransactionsListView.as_view()),
    path('transaction/<int:pk>', TransactionDetailView.as_view()),
    path('transaction/create', TransactionCreateView.as_view()),
    path('transaction/grouped', TransactionsListGroupedView.as_view()),
    path('fibonacci/<int:n>', FibonacciView.as_view()),
]