
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ledger.views import UserViewSet, TransactionViewSet, SignupView, LoginView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'txs', TransactionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
