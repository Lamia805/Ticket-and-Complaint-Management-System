from django.urls import path
from . import views


urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    
    path('create-ticket/', views.create_ticket, name='create_ticket'),
    path('view-tickets/', views.view_tickets, name='view_tickets'),
    path('update-ticket/<int:ticket_id>/', views.update_ticket, name='update_ticket'), 
    path('delete-ticket/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),
]

