from rest_framework.generics import ListCreateAPIView
from account.models import Account
from .serializers import AccountSerializer

class AccountListCreate(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer