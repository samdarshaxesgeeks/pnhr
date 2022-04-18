from django.shortcuts import render
from employees.models import Contacts
from .selevtors import get_contract
from crm_app.models import Customer
from crm_app.selectors import get_customer

# Create your views here.
from invoice1.models import Invoice,Product
# from crm_app.models import Customer
from .models import Contract
from uuid import uuid4
import random


def contractlist(request):
    

    context={
    
        "cotract": "active",
        'contract':Contract.objects.all(),
        'customer': Customer.objects.all(),

    }

    return render(request, 'contract/contract-table-list.html',context)


def add_new_contract(request):
    if request.method == 'POST':
        customer = CreateContract(request)
        context = {
            "crm_app": "active",
            "success_msg": "You have successfully added %s to the customer" % customer.first_name,
            "customer": customer
        }

        return render(request, 'success.html', context)

    else:
        context = {
            "crm_app": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "employees/failed.html", context)


def CreateContract(request):
    # import pdb
    # pdb.set_trace()
    number = 'W-' + str(random.randint(10000000 , 99999999))
    # contract = Contract.objects.get()

    if request.method == 'POST':
        name = request.POST['name1']
        email = request.POST['email']
        State = request.POST['state1']
        Address = request.POST['address1']
        bill = BillTo(name=name,email=email,state=State,address=Address,)
        bill.save()
        name = request.POST['name2']
        email = request.POST['gmail1']
        State = request.POST['state2']
        Address = request.POST['address2']
        ship = ShipTo(name=name, email=email, State=State, Address=Address,billto=bill)
        ship.save()
        Address = request.POST['address3']
        place_obj = PlaceOfSupply(Address=Address, billto=bill,shipto=ship)
        place_obj.save()
        date = request.POST['date']
        invoice_obj = Invoice(invoice_no=number,invoice_date=date,
                              billto=bill,shipto=ship,placeofsupply=place_obj)
        invoice_obj.save()
        product = request.POST['product[]']
        price = request.POST['price[]']
        qty = request.POST['qty[]']
        tax = request.POST['tax1']
        total = request.POST['total[]']
        sub_total = request.POST['sub_total']
        tax_amount = request.POST['tax_amount']
        grand_total = request.POST['total_amount']
        amountdeposit = request.POST['amount_deposit']
        amountdue = request.POST['amount_due']
        product_obj = Product(amount_due=amountdue,amount_deposit=amountdeposit,
                              sub_total=sub_total,product=product,
                              price=price,qty=qty,tax=tax,total=total,tax_amount=tax_amount,
                              grand_total=grand_total,billto=bill,shipto=ship,
                              placeofsupply=place_obj,invoice=invoice_obj)
        product_obj.save()
    context = {
        'number': number,
        "contract": "active",
        # 'contract':contract
    }
    return render(request, 'contract/create_contract.html',context)