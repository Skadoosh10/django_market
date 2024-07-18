from django.urls import path

from . import views

app_name='item'

urlpatterns = [
    path("", views.items, name="items"),
    path('<int:id>/',views.detail,name="detail"),
    path('new/',views.new, name="new"),
    path('<int:id>/delete/',views.delete,name="delete"),
    path('<int:id>/edit',views.edit,name="edit"),
]
