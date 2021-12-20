from django.urls import path, include

from rest_framework.routers import DefaultRouter

from ..views.reservation_views import ReservationViewSet, ReservationDetailView, PaymentApiView

app_name = 'reservations'

router = DefaultRouter()
router.register('', PaymentApiView)

urlpatterns = [
    path('', include(router.urls)),
    path('all/', ReservationViewSet.as_view({'get':'list'}),name='all-reservations'),
    path('all/event_id=<int:event_id>/', ReservationViewSet.as_view({'get':'list'})),
    path('all/reservation_id=<int:reservation_id>/', ReservationDetailView.as_view(), name='single-reservation'),
]