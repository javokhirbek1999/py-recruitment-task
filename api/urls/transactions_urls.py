from django.urls import path, include

from rest_framework.routers import DefaultRouter


from ..views.transaction_views import TransactionViewSet,


app_name = 'transactions'

router = DefaultRouter()
router.register('all', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('all/reservation_id=<int:reservation_id>/pay/', TransactionViewSet.as_view({'post':'list'}), name='pay'),
]