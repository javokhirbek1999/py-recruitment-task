from django.urls import path, include

from rest_framework.routers import DefaultRouter

from ..views.reservation_views import ReservationViewSet

app_name = 'reservations'


router = DefaultRouter()
router.register('all', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]