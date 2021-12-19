from django.urls import path, include

from rest_framework.routers import DefaultRouter

from ..views import event_views


app_name = 'events'


router = DefaultRouter()
router.register('all', event_views.EventsViewSet)
router.register('buildings', event_views.BuildingsViewSet)
router.register('seats', event_views.SeatViewSet)
router.register('venues', event_views.VenueViewSet)
router.register('ticket-set', event_views.TicketSetView)

urlpatterns = [
    path('',include(router.urls)),
]

