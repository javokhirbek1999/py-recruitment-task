from django.urls import path, include

from ..views.reservation_views import ReservationViewSet, ReservationDetailView, ReservationPaymentView

app_name = 'reservations'

urlpatterns = [
    path('all/', ReservationViewSet.as_view({'get':'list', 'post':'list'}),name='all-reservations'),
    path('all/client_id=<int:client_id>/event_id=<int:event_id>/', ReservationDetailView.as_view(), name='single-reservation'),
    path('all/client_id=<int:client_id>/event_id=<int:event_id>/pay/', ReservationPaymentView.as_view())
]