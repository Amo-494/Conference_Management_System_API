"""
URL configuration for conference_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # Added 'include' for router registration
from rest_framework import routers
from management.views import (  # Import all viewset classes
    ConferenceViewSet,
    SpeakerViewSet,
    ScheduleViewSet,  # Corrected indentation for ScheduleViewSet
    AttendeeViewSet,
    FeedbackViewSet,
)

router = routers.DefaultRouter()
router.register('conference', ConferenceViewSet)  # Removed extra comma
router.register('speaker', SpeakerViewSet)
router.register('schedule', ScheduleViewSet)
router.register('attendee', AttendeeViewSet)
router.register('feedback', FeedbackViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Include router URLs
]


# from .views import Confb erenceListCreateView,ScheduleListCreateView,SpeakerListCreateView,AttendeeListCreateView,FeedbackListCreateView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('conferences/', ConferenceListCreateView.as_view(), name='conference-list-create'),
#     path('speakers/', SpeakerListCreateView.as_view(), name='speaker-list-create'),
#     path('schedules/', ScheduleListCreateView.as_view(), name='schedule-list-create'),
#     path('attendees/', AttendeeListCreateView.as_view(), name='attendee-list-create'),
#     path('feedbacks/', FeedbackListCreateView.as_view(), name='feedback-list-create'),

# ]
