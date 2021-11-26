from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import *
from .forms import CustomerForm, OrderForm
# Create your views here.

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()
    context = {'orders':orders, 'customers':customers,'total_customers':total_customers, 
    'total_orders':total_orders,'delivered':delivered, 'pending':pending }
    return render(request, "accounts/dashboard.html", context)

def products(request):
    products = Product.objects.all()
    return render(request, "accounts/products.html", {'products':products})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()
    context = {'customer':customer, 'orders':orders, 'total_orders':total_orders}
    return render(request, "accounts/customer.html", context)

def create_order(request):
    form = OrderForm()
    if request.method == 'POST':
        print('Printing Post', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form':form}
    return render(request, "accounts/create_order.html", context)

def UpdateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        print('Printing Post', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")
        
    context = {'form':form}
    return render(request, "accounts/create_order.html", context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect("/")
    
    context = {'order':order}
    return render(request, "accounts/delete_order.html", context)
    
def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            print("SAVED")
            return redirect("/")

    context = {'form':form}
    return render(request, "accounts/create_customer.html", context)

def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid:
            form.save()            
            return redirect("customer", pk=pk)

    context = {'form':form}
    return render(request, "accounts/create_customer.html", context)

def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    
    if request.method == 'POST':
        customer.delete()
        return redirect("/")

    context = {'customer':customer}
    return render(request, "accounts/delete_customer.html", context)
