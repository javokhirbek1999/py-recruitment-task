from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.models import events

from ..views import event_views


app_name = 'events'


router = DefaultRouter()
router.register('all', event_views.EventsViewSet, basename='all')
router.register('buildings', event_views.BuildingsViewSet, basename='buildings')
router.register('venues', event_views.VenueViewSet, basename='venues')
router.register('ticket-set', event_views.TicketSetView, basename='ticket-set')

urlpatterns = [
    path('',include(router.urls)),
    path('seats/building_id=<int:building_id>/', event_views.SeatViewSet.as_view({'get':'list'})),
    path('seats/building_id=<int:building_id>/seat_id=<int:seat_id>/', event_views.SeatViewSet.as_view({'get':'retrieve'})),
    path('ticket-set/event_id=<int:event_id>/ticket_type=<str:ticket_type>/', event_views.DetailTicketSetView.as_view()),
]

