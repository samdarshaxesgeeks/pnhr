from django.db import models
from crm_app.models import Customer
from contacts.models import Contact
from django_countries.fields import CountryField
from invoice1.models import Invoice
from employees.models import Employee
from organisation_details.models import Team
# from shop.models.product import BaseProductManager, BaseProduct


CONTRACT_STATUS = (
    ('Draft Contract', 'Draft Contract'),
    ('Working For Apparel', 'Working For Apparel'),
    ('Confermation', 'Confermation'),
    ('Done', 'Done'),
)
PAYMENT_MODE = (
    ('Chaque', 'Chaque'),
    ('Debit Card', 'Debit Card'),
    ('Cradit Card', 'Cradit Card'),
)

SERVICE_TYPE = (
    ('Business Visa', 'Business Visa'),
    ('Vsit Visa', 'Vsit Visa'),
    ('Investor Visa', 'Investor Visa'),
    ('Permanent Residency', 'Permanent Residency'),
    ('Work Permit', 'Work Permit'),

)

class Product(models.Model):
   

    product = models.CharField(max_length=200,null=True, blank=True,)
    price = models.IntegerField(null=True, blank=True,default=None)
    qty = models.IntegerField(null=True, blank=True,default=None)
    tax = models.IntegerField(null=True, blank=True,default=None)
    total = models.IntegerField(null=True, blank=True,default=None)
    
    def __str__(self):
        return "{} {}".format(self.product, self.total)



class Contract(models.Model):
   
    contract_no = models.CharField(max_length=200)
    create_date = models.DateField(null=True)
    contract_date = models.DateField(null=True)
    customer = models.OneToOneField(Contact, on_delete=models.CASCADE)
    apply_country = CountryField()
    sales_team = models.OneToOneField(Team, on_delete=models.CASCADE)
    salesmen = models.OneToOneField(Employee, on_delete=models.CASCADE)
    contract_status = models.CharField(max_length=200, choices=CONTRACT_STATUS)
    service_type = models.CharField(max_length=200, choices=SERVICE_TYPE)
    contract_template = models.CharField(max_length=200, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    





