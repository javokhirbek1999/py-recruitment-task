from django.urls import path, include

from rest_framework.routers import DefaultRouter

from ..views import ticket_views


app_name = 'tickets' 


router = DefaultRouter()
router.register('all', ticket_views.TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]