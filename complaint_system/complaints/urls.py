from django.urls import path
from . import views

urlpatterns = [
    path('complaints/', views.view_complaints, name='view_complaints'),
    path('complaint/<int:complaint_id>/', views.complaint_detail, name='complaint_detail'),
    path('create-complaint/', views.create_complaint, name='create_complaint'),
    path('update-complaint/<int:complaint_id>/', views.update_complaint, name='update_complaint'),
    path('delete-complaint/<int:complaint_id>/', views.delete_complaint, name='delete_complaint'),
    path('update-complaint-satisfaction/<int:complaint_id>/', views.update_complaint_satisfaction, name='update_complaint_satisfaction'),
]

