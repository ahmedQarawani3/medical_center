from django.shortcuts import render
from medical.models import Medication

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Patient, Test
from .serializers import PatientSerializer
from .models import Notification
from .serializers import NotificationSerializer
from django.utils import timezone
from datetime import timedelta
from appointments.models import Appointment

@api_view(['GET'])
def patient_details(request, patient_id):
    try:
        patient = Patient.objects.get(user_id=patient_id)
        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Patient.DoesNotExist:
        return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def patient_notifications(request, patient_id):
    notifications = Notification.objects.filter(patient__user_id=patient_id)
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def create_appointment_notification(request, appointment_id):
    try:
        appointment = Appointment.objects.get(id=appointment_id)
        patient = appointment.patient 

        notification_time = appointment.date - timedelta(days=1)
        message = f"Reminder: You have an appointment scheduled with Dr. {appointment.doctor} on {appointment.date}."

        notification = Notification.objects.create(
            patient=patient,
            notification_type='appointment',
            message=message,
            notification_date=notification_time,
        )

        serializer = NotificationSerializer(notification)
        return Response(serializer.data, status=201)
    
    except Appointment.DoesNotExist:
        return Response({"error": "Appointment not found"}, status=404)
    
    
@api_view(['POST'])
def create_test_notification(request, test_id):
    try:
        test = Test.objects.get(id=test_id)
        patient = test.patient  
        
        notification_time = test.test_date - timedelta(days=1)
        message = f"Reminder: Your test {test.name} is scheduled for {test.test_date}."
        
        notification = Notification.objects.create(
            patient=patient,
            notification_type='test',
            message=message,
            notification_date=notification_time,
        )

        serializer = NotificationSerializer(notification)
        return Response(serializer.data, status=201)
    
    except Test.DoesNotExist:
        return Response({"error": "Test not found"}, status=404)

@api_view(['POST'])
def create_medication_notification(request, medication_id):
    try:
        medication = Medication.objects.get(id=medication_id)
        patient = medication.patient 

        notification_time = timezone.now()
        message = f"Reminder: It's time to take your medication {medication.name}."

        notification = Notification.objects.create(
            patient=patient,
            notification_type='medication',
            message=message,
            notification_date=notification_time,
        )

        serializer = NotificationSerializer(notification)
        return Response(serializer.data, status=201)
    
    except Medication.DoesNotExist:
        return Response({"error": "Medication not found"}, status=404)

@api_view(['GET'])
def get_notifications(request):
    patient = request.user 
    notifications = Notification.objects.filter(patient=patient).order_by('-notification_date')
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)


