from django.urls import path

from . import views

app_name = "saidia_app"

urlpatterns = [
    path("", views.index, name = "index"),
    path("login", views.login, name = "login"),
    path("mn", views.manage, name = "manage"),
    path("mn/add", views.add_orphanage, name = "add_orphanage"),
    path("op/<str:orph_id>", views.orphanage, name = "orphanage"),
    path("ad/nd/<str:oph>", views.add_need, name = "add_need"),
    path("rm/nd/<str:orph_id>/<str:need_id>", views.remove_need, name = "remove_need"),
    path("rm/op/<int:orph_id>", views.remove_orphanage, name="remove_orphanage"),
    path("register", views.register, name="register"),
    path("get_coord", views.get_coord, name="get_coord"),
    path("logout", views.logout, name="logout"),
    path("error/<str:error_id>", views.error, name="error")
]
