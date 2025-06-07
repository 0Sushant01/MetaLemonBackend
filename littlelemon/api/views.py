from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User, Group
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import (
    CategorySerializer, MenuItemSerializer, CartSerializer,
    OrderSerializer, OrderItemSerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        menuitem = serializer.validated_data['menuitem']
        quantity = serializer.validated_data['quantity']
        unit_price = menuitem.price
        serializer.save(user=self.request.user, unit_price=unit_price)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Manager').exists():
            return Order.objects.all()
        elif user.groups.filter(name='DeliveryCrew').exists():
            return Order.objects.filter(delivery_crew=user)
        return Order.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['patch'], permission_classes=[permissions.IsAuthenticated])
    def assign_delivery_crew(self, request, pk=None):
        order = self.get_object()
        if request.user.groups.filter(name='Manager').exists():
            crew_id = request.data.get('delivery_crew_id')
            crew_user = User.objects.get(id=crew_id)
            order.delivery_crew = crew_user
            order.save()
            return Response({'status': 'delivery crew assigned'})
        return Response({'error': 'Not authorized'}, status=403)


class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return OrderItem.objects.all()


class ManagerUserViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAdminUser]

    @action(detail=False, methods=['post'])
    def assign_manager(self, request):
        user_id = request.data.get('user_id')
        user = User.objects.get(id=user_id)
        group, created = Group.objects.get_or_create(name='Manager')
        user.groups.add(group)
        return Response({'status': f'User {user.username} added to Manager group'})


class DeliveryCrewViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAdminUser | permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def assign_to_crew(self, request):
        user_id = request.data.get('user_id')
        user = User.objects.get(id=user_id)
        group, created = Group.objects.get_or_create(name='DeliveryCrew')
        user.groups.add(group)
        return Response({'status': f'User {user.username} added to DeliveryCrew group'})
