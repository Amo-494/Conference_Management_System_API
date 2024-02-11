from django.shortcuts import render
from rest_framework import viewsets
from .models import Conference, Speaker, Schedule, Attendee, Feedback
from .serializers import ConferenceSerializer, SpeakerSerializer, ScheduleSerializer, AttendeeSerializer, FeedbackSerializer

# Create your views here.

class ConferenceViewSet(viewsets.ModelViewSet):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

# from urllib import response
# from rest_framework import generics
# from .models import Conference, Speaker, Schedule, Attendee, Feedback
# from .serializers import ConferenceSerializer, SpeakerSerializer, ScheduleSerializer, AttendeeSerializer, FeedbackSerializer

# class ConferenceListCreateView(generics.ListCreateAPIView):
#     queryset = Conference.objects.all()
#     serializer_class = ConferenceSerializer

#     def get(self, request, format=None):
#         """
#         Retrieves a list of all conferences.
#         """
#         conferences = self.get_queryset()
#         serializer = self.get_serializer(conferences, many=True)
#         return response(serializer.data)

#     def post(self, request, format=None):
#         """
#         Creates a new conference.
#         """
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SpeakerListCreateView(generics.ListCreateAPIView):
#     queryset = Speaker.objects.all()
#     serializer_class = SpeakerSerializer

# class ScheduleListCreateView(generics.ListCreateAPIView):
#     queryset = Schedule.objects.all()
#     serializer_class = ScheduleSerializer

# class AttendeeListCreateView(generics.ListCreateAPIView):
#     queryset = Attendee.objects.all()
#     serializer_class = AttendeeSerializer

# class FeedbackListCreateView(generics.ListCreateAPIView):
#     queryset = Feedback.objects.all()
#     serializer_class = FeedbackSerializer