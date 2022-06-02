from unicodedata import category
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Q
from math import ceil
from django.http import JsonResponse
from .models import Customer, Item, Product,Booked,Vendor,Farmer,VendorProduct,Contact
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CustomerRegistrationForm, CustomerProfileForm,VenderRegistrationForm,FarmerRegistrationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

class FarmerRegistrationView(View):
	def get(self, request):
		form = FarmerRegistrationForm()
		return render(request, 'Jai_Kisan/farmerregistration.html', {'form': form})
	def post(self, request):
		form = FarmerRegistrationForm(request.POST)
		if form.is_valid():
			print("manodd")
			user = User.objects.create_user(username=form.cleaned_data.get('User_name'),email=form.cleaned_data.get('email'),password=form.cleaned_data.get('password'))
			user.is_active = True
			user.save()
			print("mudd")
			User_name=form.cleaned_data.get('User_name')
			First_name=form.cleaned_data.get('First_name')
			Last_name=form.cleaned_data.get('Last_name')
			email=form.cleaned_data.get('email')
			phone=form.cleaned_data.get('phone'),
			state=form.cleaned_data.get('state')
			city=form.cleaned_data.get('city')
			locality=form.cleaned_data.get('locality')
			zipcode=form.cleaned_data.get('zipcode')
			farmer_data=Farmer(user=user, User_name=User_name,First_name=First_name,Last_name=Last_name,email= email,phone=phone,
							   state=state,city=city,locality=locality,zipcode=zipcode)
			print("maff")
			messages.success(request, 'Congratulations!! Account Registered Successfully')
			farmer_data.save()
			
			# new_user = authenticate(username=form.cleaned_data.get('User_name'),
            #       password=form.cleaned_data.get('password'))
			# print(new_user)
			# login(request, new_user)
			# return render(request,'/services.html')
		
			# return redirect('/farmerregistration')
			return redirect('/accounts/login')

def vender_add_product(request):
   totalitem = 0
   if request.method == 'GET':
      # prod_id = request.GET['prod_id']
      if request.user.is_authenticated:
         totalitem = len(VendorProduct.objects.filter(user=request.user))
         Product_list=Product.objects.all()
         print(Product_list, "murde")
      # user=request.user
      # Vender_product_list =VendorProduct.Objects.filter(user=user)
      # c = Item.objects.get(Q(product=prod_id) & Q(user=request.user))
      # c.duration +=1
      # c.save()
      # amount = 0.0
      # shipping_amount= 70.0
         cart_product = [p for p in VendorProduct.objects.all() if p.user == request.user]
         print(cart_product)
         if cart_product:
            return render(request, 'Jai_Kisan/venderaddproduct.html',
                    {'Product_list': Product_list, 'cart_product': cart_product,'totalitem': totalitem})
         else:
            return render(request, 'Jai_Kisan/vender_empty.html', {'totalitem': totalitem})
      # for p in cart_product:
         # tempamount = (p.duration * p.product.discounted_price)
         # print("Quantity", p.quantity)
         # print("Selling Price", p.product.discounted_price)
         # print("Before", amount)
         # amount += tempamount
         # print("After", amount)
      # print("Total", amount)
      # data = {
      #  'duration':c.duration,
      #  'amount':amount,
      #  'totalamount':amount+shipping_amount
      # }
      # return JsonResponse(data)
   # else:
   #  return HttpResponse("")


   if request.method =='POST':
      print("manohar")
      if request.user.is_authenticated:
         totalitem = len(VendorProduct.objects.filter(user=request.user))
         print(totalitem)
        #  category = request.POST.get('category')
        #  brand = request.POST.get('sub_category')
         category1 = request.POST.get('select1')
         brand1 = request.POST.get('select2')
         print(category1)
         # print(sub_category1)
         # print(category)
         print(brand1)
         user = request.user
         # name = request.POST['select1']
         # print(name)
         Product_list= Product.objects.filter(brand=brand1,category=category1)
         id = 0
         for Pr in Product_list:
            id= Pr.id
         print(id)
         print(Product_list,"post")
         product = Product()
         # Product_enter_by_vender = VendorProduct.objects.create(product =1,user=user,brand=brand,category=category)
         Product_enter_by_vender= VendorProduct(product_id =id,user=user,brand=brand1,category=category1)
         Product_enter_by_vender.save()
         messages.success(request, 'Congratulations!! Product added sucessfully')
         cart = VendorProduct.objects.filter(user=user)
         cart_product = [p for p in VendorProduct.objects.all() if p.user == request.user]
         print(cart_product)
         if cart_product:
            return render(request, 'Jai_Kisan/venderaddproduct.html',
                       {'Product_list': Product_list, 'cart_product': cart_product,'totalitem': totalitem})
            # return render(request, 'Jai_Kisan/venderadd.html',
            #       {'carts': cart, 'totalitem': totalitem})
         else:
            return render(request, 'Jai_Kisan/vender_emptycart.html', {'totalitem': totalitem})
      # else:
      #  return render(request, 'Jai_Kisan/vender_emptycart.html', {'totalitem': totalitem})
   # else:
   #  return render(request, 'Jai_Kisan/vender_emptycart.html', {'totalitem': totalitem})


      # else:
      #  return render(request, 'Jai_Kisan/vender_emptycart.html', {'totalitem': totalitem})
   # else:
   #  return render(request, 'Jai_Kisan/vender_emptycart.html', {'totalitem': totalitem})



class VenderRegistrationView(View):
	def get(self, request):
		form = VenderRegistrationForm()
		return render(request, 'Jai_Kisan/venderregistration.html', {'form': form})
	def post(self, request):
		form = VenderRegistrationForm(request.POST)
		if form.is_valid():
			print("manodd")
			user = User.objects.create_user(username=form.cleaned_data.get('User_name'),email=form.cleaned_data.get('email'),password=form.cleaned_data.get('password'))
			user.is_active = True
			user.save()
			print("mudd")
			User_name=form.cleaned_data.get('User_name')
			First_name=form.cleaned_data.get('First_name')
			Last_name=form.cleaned_data.get('Last_name')
			email=form.cleaned_data.get('email')
			phone=form.cleaned_data.get('phone'),
			state=form.cleaned_data.get('state')
			city=form.cleaned_data.get('city')
			locality=form.cleaned_data.get('locality')
			zipcode=form.cleaned_data.get('zipcode')
			vendor_data=Vendor(user=user, User_name=User_name,First_name=First_name,Last_name=Last_name,email= email,phone=phone,
							   state=state,city=city,locality=locality,zipcode=zipcode)
			print("maff")
			messages.success(request, 'Congratulations!! Registered Successfully.Proceed with adding the Products')
			vendor_data.save()
			new_user = authenticate(username=form.cleaned_data.get('User_name'),
                  password=form.cleaned_data.get('password'))
			print(new_user)
			login(request, new_user)
			print("login_newuser")
			return redirect('/venderregistration')

            # form.save()
			#return render(request,'Jai_Kisan/venderregistration.html',{'form': form})

			# return HttpResponseRedirect('Jai_Kisan/venderregistration.html',{'form': form})
        # return render(request, 'Jai_kisan/venderregistration.html', {'form': form})

def index(request):
    # allProds = []
    # catprods = Product.objects.values('category', 'id')
    # cats = {item['category'] for item in catprods}
    # for cat in cats:
    #     prod = Product.objects.filter(category=cat)
    #     n = len(prod)
    #     nSlides = n // 4 + ceil((n / 4) - (n // 4))
    #     allProds.append([prod, range(1, nSlides), nSlides])
    # params = {'allProds':allProds}
    return render(request, 'Jai_Kisan/home.html')
class ProductView(View):
	def get(self, request):
		totalitem = 0
		tracter = Product.objects.filter(category='Tracter')
		boring_machine = Product.objects.filter(category='Boring Machine')
		harvestor = Product.objects.filter(category='Harvestor')
		cultivator = Product.objects.filter(category='Cultivator')
		if request.user.is_authenticated:
			totalitem = len(Item.objects.filter(user=request.user))
		return render(request, 'Jai_Kisan/home.html', {'tracter':tracter, 'boring_machine':boring_machine, 'harvestor':harvestor, 'cultivator': cultivator, 'totalitem':totalitem})


class ProductDetailView(View):
	def get(self, request, pk):
		totalitem = 0
		product = Product.objects.get(pk=pk)
		print(product.id)
		item_already_in_cart=False
		if request.user.is_authenticated:
			totalitem = len(Item.objects.filter(user=request.user))
			item_already_in_cart = Item.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
		return render(request, 'Jai_Kisan/productdetail.html', {'product':product, 'item_already_in_cart':item_already_in_cart, 'totalitem':totalitem})

	def post(self,request,pk):
		pass


@login_required()
def add_to_cart(request):
	user = request.user
	item_already_in_cart1 = False
	product = request.GET.get('prod_id')
	item_already_in_cart1 = Item.objects.filter(Q(product=product) & Q(user=request.user)).exists()
	if item_already_in_cart1 == False:
		product_title = Product.objects.get(id=product)
		Item(user=user, product=product_title).save()
		messages.success(request, 'Product Added to Cart Successfully !!' )
		return redirect('/cart')
	else:
		return redirect('/cart')

@login_required
def show_cart(request):
	totalitem = 0
	if request.user.is_authenticated:
		totalitem = len(Item.objects.filter(user=request.user))
		user = request.user
		cart = Item.objects.filter(user=user)
		amount = 0.0
		shipping_amount = 70.0
		# food charge = 100.0
		totalamount=0.0
		cart_product = [p for p in Item.objects.all() if p.user == request.user]
		print(cart_product)
		if cart_product:
			for p in cart_product:
				tempamount = (p.duration * p.product.discounted_price)
				amount += tempamount
			totalamount = amount+shipping_amount
			return render(request, 'Jai_Kisan/addtocart.html', {'carts':cart, 'amount':amount, 'totalamount':totalamount, 'totalitem':totalitem})
		else:
			return render(request, 'Jai_Kisan/emptycart.html', {'totalitem':totalitem})
	else:
		return render(request, 'Jai_Kisan/emptycart.html', {'totalitem':totalitem})

def plus_cart(request):
	if request.method == 'GET':
		prod_id = request.GET['prod_id']
		c = Item.objects.get(Q(product=prod_id) & Q(user=request.user))
		c.duration +=1
		c.save()
		amount = 0.0
		shipping_amount= 70.0
		cart_product = [p for p in Item.objects.all() if p.user == request.user]
		for p in cart_product:
			tempamount = (p.duration * p.product.discounted_price)
			# print("Quantity", p.quantity)
			# print("Selling Price", p.product.discounted_price)
			# print("Before", amount)
			amount += tempamount
			# print("After", amount)
		# print("Total", amount)
		data = {
			'duration':c.duration,
			'amount':amount,
			'totalamount':amount+shipping_amount
		}
		return JsonResponse(data)
	else:
		return HttpResponse("")

def minus_cart(request):
	if request.method == 'GET':
		prod_id = request.GET['prod_id']
		c = Item.objects.get(Q(product=prod_id) & Q(user=request.user))
		c.duration-=1
		c.save()
		amount = 0.0
		shipping_amount= 70.0
		cart_product = [p for p in Item.objects.all() if p.user == request.user]
		for p in cart_product:
			tempamount = (p.duration * p.product.discounted_price)
			# print("Quantity", p.quantity)
			# print("Selling Price", p.product.discounted_price)
			# print("Before", amount)
			amount += tempamount
			# print("After", amount)
		# print("Total", amount)
		data = {
			'duration':c.duration,
			'amount':amount,
			'totalamount':amount+shipping_amount
		}
		return JsonResponse(data)
	else:
		return HttpResponse("")

@login_required
def checkout(request):
	user = request.user
	# fadd = Farmer.objects.filter(user=user)
	cart_items = Item.objects.filter(user=request.user)
	# uname = Booked.objects.filter(user=user)
	amount = 0.0
	shipping_amount = 70.0
	totalamount=0.0
	cart_product = [p for p in Item.objects.all() if p.user == request.user]

	print("Hey")
	if cart_product:
		for p in cart_product:
			tempamount = (p.duration * p.product.discounted_price)
			amount += tempamount
		totalamount = amount+shipping_amount
	return render(request, 'Jai_Kisan/checkout.html', {'cart_items':cart_items, 'totalcost':totalamount})

@login_required
def Booked_placed(request):
	op = Booked.objects.filter(user=request.user)
	return render(request, 'Jai_Kisan/booked.html', {'Booked':op})

@login_required
def farmer(request,data=None):
	return render(request,'farmerpage.html')

def farmserv(request,data=None):
	return render(request,'services.html')

def drones(request,data=None):
	# totalitem = 0
	# if request.user.is_authenticated:
	# 	totalitem = len(VendorProduct.objects.filter(user=request.user))
	# 	print(totalitem,'Karthik')
	# if data==None :
	# 	drones = Product.objects.filter(category='Drones')
	# elif data == 'Mahindra' or data == 'Tata':
	# 	drones = Product.objects.filter(category='Drones').filter(brand=data)
	products = Product.objects.filter(category='Drones')

	data = {
		'products': products
	}
	# return render(request, 'Jai_Kisan/drones.html', {'drones':drones, 'totalitem':totalitem})
	return render(request, 'Jai_Kisan/drones.html',data)

def booking(request,data=None):
	return render(request,'booking.html')


@login_required
def vendor(request, data=None):
	return render(request,'vendorpage.html')

@login_required
def amigo(request,data=None):
	return render(request,'amigopage.html')

def transport(request, data=None):
	return render(request,'transport.html')

def tracter(request, data=None):
   totalitem = 0
   if request.user.is_authenticated:
      totalitem = len(Item.objects.filter(user=request.user))
   if data==None :
         tracter = Product.objects.filter(category='Tracter')
   elif data == 'Mahindra' or data == 'Tata':
         tracter = Product.objects.filter(category='Tracter').filter(brand=data)
   return render(request, 'Jai_Kisan/tracter.html', {'tracter':tracter, 'totalitem':totalitem})


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'Jai_kisan/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully.')
            form.save()
        return render(request, 'Jai_kisan/customerregistration.html', {'form': form})

@login_required
def address(request):
	totalitem = 0
	if request.user.is_authenticated:
		totalitem = len(Item.objects.filter(user=request.user))
	add = Customer.objects.filter(user=request.user)
	return render(request, 'Jai_Kisan/address.html', {'add':add, 'active':'btn-primary', 'totalitem':totalitem})


def remove_cart(request):
	if request.method == 'GET':
		prod_id = request.GET['prod_id']
		c = Item.objects.get(Q(product=prod_id) & Q(user=request.user))
		c.delete()
		amount = 0.0
		shipping_amount= 70.0
		cart_product = [p for p in Item.objects.all() if p.user == request.user]
		for p in cart_product:
			tempamount = (p.duration * p.product.discounted_price)
			# print("Quantity", p.quantity)
			# print("Selling Price", p.product.discounted_price)
			# print("Before", amount)
			amount += tempamount
			# print("After", amount)
		# print("Total", amount)
		data = {
			'amount':amount,
			'totalamount':amount+shipping_amount
		}
		return JsonResponse(data)
	else:
		return HttpResponse("")

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Item.objects.filter(user=request.user))
        form = CustomerProfileForm()
        return render(request, 'Jai_Kisan/profile.html', {'form': form, 'active': 'btn-primary', 'totalitem': totalitem})

    def post(self, request):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Item.objects.filter(user=request.user))
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations!! Profile Updated Successfully.')
        return render(request, 'Jai_Kisan/profile.html', {'form': form, 'active': 'btn-primary', 'totalitem': totalitem})

@login_required
def payment_done(request):
   # print("murli")
   custid = request.GET.get('custid')
   print("Customer ID", custid)
   user = request.user
   cartid = Item.objects.filter(user = user)
   print(cartid,"Karthikid")
   print(user,"UserKarthik")
   cdata = Customer.objects.all()
   custdata = {
	   	'cdata' : cdata
   }
   

   # customer = Customer.objects.get(id=custid)
   # print(customer)
   for cid in cartid:
      print(cid.product,"kdproduct")
      Booked(user=user,product=cid.product).save()
   #  print("Order Saved")
   #  cid.delete()
   #  print("Cart Item Deleted")
   return render(request, 'Jai_Kisan/payment_conformation.html',custdata)

   
def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query.lower() in item.desc.lower() or query.lower()  in item.product_name.lower() or query.lower()  in item.category.lower():
        print(query)
        print("murli manohar1")
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    # print(query)
    allProds = []
    # print(allProds)
    # print("me1111")
    catprods = Product.objects.values('category', 'id')
    # print(catprods)
    # print("me2222")
    cats = {item['category'] for item in catprods}
    # print(cats)
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        # print("me333")
        # print(prodtemp)
        # print("me4444")
        # for item in prodtemp:
        #     if query in searchMatch(query, item)
        # prod = [item for item in prodtemp if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower()]
        print("i am boss")
        print(cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        print("murli")
        print(prod)

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)
def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'shop/contact.html', {'thank': thank})




