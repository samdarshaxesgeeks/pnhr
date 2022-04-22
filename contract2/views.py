from pyexpat import model
from django.shortcuts import render,redirect, get_object_or_404
from crm_app.models import Customer
from .models import Contract, Product,other_info,document
import random

# Create your views here


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
    customer=Customer.objects.all()
   
    number = 'W-' + str(random.randint(10000000 , 99999999))
    print(number)
    # contract=get_object_or_404(Contract, pk=id)
    if request.method == 'POST':
        contract_no = number
        customer = request.POST['customer']
        contract_date =request.POST['contract_date'] 
        apply_company =request.POST['country']
        service_package =request.POST['service_Package']
        service_type = request.POST['services_type']
        contract_template = request.POST['contract_tamplate']
        Payment_Mode= request.POST.get('Payment_mode')
        c=Contract(contract_no=contract_no,contract_date=contract_date,customer=customer,apply_company=apply_company,service_Package=service_package,service_type=service_type,contract_template=contract_template,Payment_Mode=Payment_Mode)


        # product models here.
        # Product.contract=contracts
        product= request.POST['product[]']
        price= request.POST['price[]']
        qty= request.POST['qty[]']
        tax= request.POST.get('tax')
        print(tax)
        total= request.POST['total[]']
        product_obj =Product(contract_no=contract_no,product=product,price=price,qty=qty,tax=tax,total=total) 

        # document model here
        CV_Resum= request.POST['resume']
        Passpost_Scan_Copy= request.POST['Passpost_Scan_Copy']
        Emirates_ID= request.POST['EmiratesID']
        Ntional_ID= request.POST.get('national_id')
        Additional_Documen= request.POST.get('Additional_Documents')

        Document=document(contract=contract_no,CV_Resum=CV_Resum,Passpost_Scan_Copy=Passpost_Scan_Copy,Emirates_ID=Emirates_ID,Ntional_ID=Ntional_ID,Additional_Documen=Additional_Documen)

        # other_info model here
        Salesperson= request.POST.get('Salesperson')
        sales_team=request.POST.get('sales_team')
        company= request.POST.get('company')
        # online_signature= request.POST.get('online_signature')
        # online_payment= request.POST.get('online_payment')
        customerrefrance= request.POST['customer_refrance']
        fiscal_position= request.POST.get('Fiscal_Position')

        other=other_info(contract=contract_no,salesmen=Salesperson,sales_team=sales_team,company=company,customer_refrance=customerrefrance,fiscal_position=fiscal_position)


        c.save()
        print("saved Successfully")
        product_obj.save()
        print("product obj saved Successfully")
        Document.save()
        print("Document saved Successfully")
        other.save()
        print("other saved Successfully")
        

    context = {
        'number': number,
        "contract": "active",
        # 'contract':contract
        "customer":customer

    }
    return render(request, 'contract/create_contract.html',context)        
        


