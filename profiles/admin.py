from django.contrib import admin
from profiles.models import Customer_Data
from profiles.models import Account_Data
from profiles.models import Transactions
from profiles.models import Money_Transfers
from profiles.models import ECS_Data
from profiles.models import Bills
from profiles.models import customerdetail
from profiles.models import transectiondetail

# Register your models here.
admin.site.register(Customer_Data)
admin.site.register(Account_Data)
admin.site.register(Transactions)
admin.site.register(Money_Transfers)
admin.site.register(ECS_Data)
admin.site.register(customerdetail)
admin.site.register(transectiondetail)
