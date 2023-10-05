from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import product, datauser,buy2
from django.contrib import messages
from rest_framework import viewsets, permissions
from myapp.serializers import ProductsSerializer, DatauserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = ProductsSerializer
    # permissions_classes = [permissions.IsAuthenticated]

class DatauserViewSet(viewsets.ModelViewSet):
    queryset = datauser.objects.all()
    serializer_class = DatauserSerializer
    permissions_classes = [permissions.IsAuthenticated]

# Create your views here.
def db(request):
    all_products = product.objects.all
    all_data = datauser.objects.all
    return render(
        request,
        "db.html",
        {"all_products": all_products, "all_data": all_data},
    )

def hello(request):
    return HttpResponse("<h1>Hello montri</h1>")

def index(request):
    name = "มนตรี ชะนวนกลาง"
    age = 21
    return render(request, "index.html", {"name": name, "age": age})

def add(request):
    if request.method == "POST":
        name = request.POST["name"]
        price = request.POST["price"]
        Product = product.objects.create(name=name, price=price)
        Product.save()
        messages.success(request, "Data added sucessfully")
        return redirect("/db")
    return render(request, "form_add.html")

def adduser(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        address = request.POST["address"]
        phone = request.POST["phone"]

        user = datauser.objects.create(fname=fname, lname= lname, address= address, phone= phone)
        user.save()
        messages.success(request, "Data added sucessfully")
        return redirect("/db")
    return render(request, "form_adduser.html")

def update(request, product_id):
    if request.method == "POST":
        Product = product.objects.get(id=product_id)
        Product.name = request.POST["name"]
        Product.price = request.POST["price"]
        Product.save()
        messages.success(request, "Data updated sucessfully")
        return redirect("/db")
    Product = product.objects.get(id=product_id)
    return render(request, "form_update.html", {"product": Product})

def delete(request, product_id):
    Product = product.objects.get(id=product_id)
    Product.delete()
    messages.success(request, "Data delete sucessfully")
    return redirect("/db")

def deleteuser(request, datauser_id):
    user = datauser.objects.get(id=datauser_id)
    user.delete()
    messages.success(request, "Data delete sucessfully")
    return redirect("/db")

def updateuser(request, datauser_id):
    if request.method == "POST":
        user = datauser.objects.get(id=datauser_id)
        user.fname = request.POST["fname"]
        user.lname = request.POST["lname"]
        user.address = request.POST["address"]
        user.phone = request.POST["phone"]
        user.save()
        messages.success(request, "Data updated sucessfully")
        return redirect("/db")
    user = datauser.objects.get(id=datauser_id)
    return render(request, "form_updateuser.html", {"datauser": user})

def buyproduct(request, product_id, datauser_id = 1):
    if request.method == "POST":
        Product = product.objects.get(id=product_id)
        Product.name = request.POST["product"]
        Product.price = request.POST["price"]
        name = request.POST["name"]

        data = buy2.objects.create(product=product.name, price=product.price, name=name)
        data.save()
        messages.success(request, "Data added sucessfully")
        return redirect("/db")
    Product = product.objects.get(id=product_id)
    Datauser = datauser.objects.get(id=datauser_id)
    return render(request, "form_addbuy.html", {"product": Product , "datauser": Datauser})


