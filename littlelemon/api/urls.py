
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    MenuItemViewSet,
    CartView,
    OrderViewSet,
    OrderItemViewSet,
    ManagerUserViewSet,
    DeliveryCrewViewSet,
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'menu-items', MenuItemViewSet, basename='menuitem')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'order-items', OrderItemViewSet, basename='orderitem')
router.register(r'groups/manager/users', ManagerUserViewSet, basename='managerusers')
router.register(r'groups/delivery-crew/users', DeliveryCrewViewSet, basename='deliverycrewusers')

urlpatterns = [
    path('cart/menu-items/', CartView.as_view(), name='cart-menuitems'),
    path('', include(router.urls)),
]
