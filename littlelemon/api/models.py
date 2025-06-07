from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    slug = models.SlugField(unique=True)  # Slug should be unique for URLs
    title = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='menu_items')
    title = models.CharField(max_length=100, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(default=False, db_index=True)  # Default value added

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()  # use PositiveSmallIntegerField for quantity
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('user', 'menuitem')  # order of fields fixed

    def __str__(self):
        return f"{self.quantity} x {self.menuitem.title} for {self.user.username}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='deliveries', null=True, blank=True)
    status = models.BooleanField(default=False, db_index=True)  # False = not delivered, True = delivered
    total = models.DecimalField(max_digits=8, decimal_places=2)  # max_digits increased for safety
    date = models.DateField(auto_now_add=True, db_index=True)  # auto_now_add for order creation date

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')  # Fixed FK target to Order model!
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)  # Fixed typo: unity_price -> unit_price
    price = models.DecimalField(max_digits=8, decimal_places=2)  # total price = unit_price * quantity

    class Meta:
        unique_together = ('order', 'menuitem')

    def __str__(self):
        return f"{self.quantity} x {self.menuitem.title} in Order {self.order.id}"
