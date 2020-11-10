from django.db import models


class User(models.Model):
    """модель таблицы пользователя сайта, делятся по роли на клиентов и менеджеров"""
    name = models.CharField(max_length=255, verbose_name="ФИО пользователя")
    address = models.CharField(max_length=255, verbose_name="Адрес доставки", unique=True, null=True, blank=True)
    email = models.EmailField(verbose_name="Email клиента", unique=True)
    password = models.CharField(verbose_name="Пароль", max_length=255)
    ROLES = [("CL", "client"), ("MGR", "manager")]
    role = models.CharField(max_length=5, choices=ROLES, default="CL")

    def __str__(self):
        return f"{self.name} - {self.role}"


class Item(models.Model):
    """модель таблицы товаров"""
    title = models.CharField(max_length=255, verbose_name="Название товара", unique=True)
    articul = models.CharField(max_length=255, verbose_name="Артикул товара", unique=True)
    price_zakup = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Закупочная цена")
    price_rozn = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Розничная цена")

    def __str__(self):
        return f"Артикул {self.articul} | Название: {self.title}"


class Position(models.Model):
    """модель таблицы позиции в корзине"""
    item = models.ForeignKey("Item", verbose_name="Товар", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Розничная цена товара на момент заказа")
    count = models.IntegerField(verbose_name="Количество товара")
    cart = models.ForeignKey("Cart", verbose_name="Корзина", on_delete=models.CASCADE, related_name="positions")

    class Meta:
        unique_together = ["item", "cart"]

    def __str__(self):
        return f"{self.item.title} - {self.price} - {self.count} - {self.price * self.count}"


class Cart(models.Model):
    """модель таблицы корзина покупателя"""
    user = models.ForeignKey("User", on_delete=models.CASCADE)

    def __str__(self):
        return f"Корзина {self.user.name}"
