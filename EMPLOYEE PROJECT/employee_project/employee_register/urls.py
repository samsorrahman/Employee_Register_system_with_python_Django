
from django.urls import path, include
from . import views

urlpatterns = [
    # get andpost for insert
    path('', views.employee_form, name='employee_insert'),
    # get and psot for update
    path('<int:id>/', views.employee_form, name='employee_update'),
    # deleting path
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    # get request to retrive and siaplay
    path('list/', views.employee_list, name='employee_list')
]
