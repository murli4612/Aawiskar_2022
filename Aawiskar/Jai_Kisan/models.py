from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
STATE_CHOICES = (
  ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
  ('Andhra Pradesh','Andhra Pradesh'),
  ('Arunachal Pradesh','Arunachal Pradesh'),
  ('Assam','Assam'),
  ('Bihar','Bihar'),
  ('Chandigarh','Chandigarh'),
  ('Chhattisgarh','Chhattisgarh'),
  ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
  ('Daman and Diu','Daman and Diu'),
  ('Delhi','Delhi'),
  ('Goa','Goa'),
  ('Gujarat','Gujarat'),
  ('Haryana','Haryana'),
  ('Himachal Pradesh','Himachal Pradesh'),
  ('Jammu & Kashmir','Jammu & Kashmir'),
  ('Jharkhand','Jharkhand'),
  ('Karnataka','Karnataka'),
  ('Kerala','Kerala'),
  ('Lakshadweep','Lakshadweep'),
  ('Madhya Pradesh','Madhya Pradesh'),
  ('Maharashtra','Maharashtra'),
  ('Manipur','Manipur'),
  ('Meghalaya','Meghalaya'),
  ('Mizoram','Mizoram'),
  ('Nagaland','Nagaland'),
  ('Odisha','Odisha'),
  ('Puducherry','Puducherry'),
  ('Punjab','Punjab'),
  ('Rajasthan','Rajasthan'),
  ('Sikkim','Sikkim'),
  ('Tamil Nadu','Tamil Nadu'),
  ('Telangana','Telangana'),
  ('Tripura','Tripura'),
  ('Uttarakhand','Uttarakhand'),
  ('Uttar Pradesh','Uttar Pradesh'),
  ('West Bengal','West Bengal'),
)
class Customer(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 name = models.CharField(max_length=200)
 locality = models.CharField(max_length=200)
 city = models.CharField(max_length=50)
 zipcode = models.IntegerField()
 state = models.CharField(choices=STATE_CHOICES, max_length=50)

 def __str__(self):
  # return self.user.username
  return str(self.id)
CATEGORY_CHOICES = (
('Tracter', 'Tracter'),
('Boring Machine', 'Boring Machine'),
('Harvestor', 'Harvestor'),
('Cultivator', 'Cultivater'),
('Drones','Drones'),
)

class Product(models.Model):
 title = models.CharField(max_length=100)
 selling_price = models.FloatField()
 discounted_price = models.FloatField()
 description = models.TextField()
 brand = models.CharField(max_length=100)
 category = models.CharField( choices=CATEGORY_CHOICES, max_length=20)
 product_image = models.ImageField(upload_to='productimg',default="")
 vendor_name = models.CharField(max_length=100,default="")
 vendor_location = models.CharField(max_length=100,default="")
 capacity = models.FloatField(max_length=4,default=0.0)
 features = models.CharField(max_length=300)
 flight_time = models.IntegerField(default="1")
 drone_range = models.FloatField(max_length=4,default=0.0)

 

 def __str__(self):
  return str(self.id)

class Item(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
 duration = models.PositiveIntegerField(default=1)

 def __str__(self):
  return str(self.id)

 @property
 def total_cost(self):
   return self.duration * self.product.discounted_price

STATUS_CHOICES = (
     ('Accepted', 'Accepted'),
     ('On The Way', 'On The Way'),
     ('Work in Progress','Work in progress'),
     ('Completed', 'Completed'),
     ('Cancel', 'Cancel')
 )
class Booked(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
    #  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
     duration = models.PositiveIntegerField(default=1)
     ordered_date = models.DateTimeField(auto_now_add=True)
     status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

     # Below Property will be used by orders.html page to show total cost
     @property
     def total_cost(self):
         return self.duration * self.product.discounted_price

class Vendor(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, primary_key=True, db_column='id',on_delete=models.CASCADE)
    User_name=models.CharField(max_length=200)
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    email =models.EmailField(max_length=50)
    phone =models.CharField(max_length=12)
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
    city = models.CharField(max_length=50)
    locality = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    password = models.CharField(max_length=20)
    conform_password =models.CharField(max_length=20)
    def __str__(self):
        # return self.user.username
        return str(self.id)

        class Meta:
            db_table = "auth_user_datum"
            verbose_name = "User Data"
            verbose_name_plural = "User Datum"


class Farmer(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, primary_key=True, db_column='id',on_delete=models.CASCADE)
    User_name=models.CharField(max_length=200)
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    email =models.EmailField(max_length=50)
    phone =models.CharField(max_length=12)
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
    city = models.CharField(max_length=50)
    locality = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    password = models.CharField(max_length=20)
    conform_password =models.CharField(max_length=20)
    def __str__(self):
        # return self.user.username
        return str(self.id)

        class Meta:
            db_table = "auth_user_datum"
            verbose_name = "User Data"
            verbose_name_plural = "User Datum"

class VendorProduct(models.Model):
# Product_name = models.CharField(max_length=100)
# user = models.OneToOneField(User, primary_key=True, db_column='id', on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  brand = models.CharField(max_length=100)
  category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
# Nproduct = models.PositiveIntegerField(default=1)
# Rent_value = models.FloatField()
# Offer = models.FloatField()
# product_image = models.ImageField(upload_to='productimg',default="")
# def __str__(self):
#     return self.product
def __str__(self):
  return str(self.id)

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.msg_id
