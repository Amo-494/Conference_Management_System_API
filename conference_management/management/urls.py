from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('conference', views.ConferenceViewSet),
router.register('speaker', views.SpeakerViewSet),
router.register('schedule', views.ScheduleViewSet) ,
router.register('attendee', views.AttendeeViewSet),
router.register('feedback', views.FeedbackViewSet),

# urlpatterns= [

# ]