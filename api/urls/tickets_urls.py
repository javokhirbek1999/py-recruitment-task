from django.urls import path, include

from rest_framework.routers import DefaultRouter

from ..views import ticket_views


app_name = 'tickets' 


router = DefaultRouter()
router.register('all', ticket_views.TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('all/event_id=<int:event_id>/ticket_type=<str:ticket_type>/status=<str:status>/', ticket_views.TicketViewSet.as_view({'get':'list'})),
    path('all/event_id=<int:event_id>/seat_id=<int:seat_id>/', ticket_views.TicketDetailView.as_view()),
    path('all/event_id=<int:event_id>/seat_id=<int:seat_id>/reserve', ticket_views.ReserveTicketView.as_view()),    
]