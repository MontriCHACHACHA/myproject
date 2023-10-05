from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index),
    path("hello/", views.hello),
    path("db/", views.db),
    path("add/", views.add),
    path("add_user/", views.adduser),
    path("update/<product_id>", views.update),
    path("delete/<product_id>", views.delete),
    path("deleteuser/<datauser_id>", views.deleteuser),
    path("updateuser/<datauser_id>", views.updateuser),
    path("buyuser/<product_id>", views.buyproduct),

]
