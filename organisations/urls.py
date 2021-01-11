from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('admin', views.admin, name='admin'),
    path('add_manager', views.add_manager, name='add_manager'),
    path('add_orgs', views.add_orgs, name='add_orgs'),
    path('add_employee', views.add_employee, name='add_employee'),
    path('add_vacation', views.add_vacation, name='add_vacation'),
    path('get_employees', views.get_employees, name='get_employees'),
    path('get_vacation', views.get_vacation, name='get_vacation'),
    path('delete_org', views.delete_org, name='delete_org'),
    path('delete_empl', views.delete_empl, name='delete_empl'),
    path('delete_vac', views.delete_vac, name='delete_vac'),
    path('delete_man', views.delete_man, name='delete_man'),

]
