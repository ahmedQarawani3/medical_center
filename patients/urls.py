from django.urls import path

from . import views
from .views import patient_details,patient_notifications

urlpatterns = [
    path('<int:patient_id>/', patient_notifications, name='patient_notifications'),
    path('<int:patient_id>/', patient_details, name='patient_details'),
    path('create_appointment_notification/<int:appointment_id>/', views.create_appointment_notification, name='create_appointment_notification'),
    path('create_test_notification/<int:test_id>/', views.create_test_notification, name='create_test_notification'),
    path('create_medication_notification/<int:medication_id>/', views.create_medication_notification, name='create_medication_notification'),
    path('notifications/', views.get_notifications, name='get_notifications'),

]
