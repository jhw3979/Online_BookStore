from django.db import models
from django.utils.timezone import now

class User(models.Model):
    User_id = models.CharField(default='', max_length=50)
    User_pw = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)

    def __str__(self):
        return self.User_id


class ShippingDestination(models.Model):
    User = models.ForeignKey(User, on_delete=models.PROTECT)
    SD_num = models.IntegerField(default=0)
    SD_ba = models.CharField(max_length=100)
    SD_da = models.CharField(max_length=100)

    def __id__(self):
        return self.SD_id


class Card(models.Model):
    User = models.ForeignKey(User, on_delete=models.PROTECT)
    Card_name = models.CharField(max_length=100)
    Card_num = models.IntegerField(default=0)
    Card_date = models.CharField(max_length=100)

    def __id__(self):
        return self.id


class Order(models.Model):
    User = models.ForeignKey(User, on_delete=models.PROTECT)
    Order_date = models.DateTimeField(default=now, blank=True)
    Order_totalprice = models.IntegerField(default=0)
    Order_con = models.IntegerField(default=0)  #구매완료되었을경우 1

    def __id__(self):
        return self.id


class ShoppingBasket(models.Model):
    User = models.ForeignKey(User, on_delete=models.PROTECT)

    def __id__(self):
        return self.id


class Book(models.Model):
    Book_name = models.CharField(max_length=100)
    Book_price = models.IntegerField(default=0)
    Book_stock = models.IntegerField(default=5)

    def __id__(self):
        return self.id


class BookSB(models.Model):         #책 장바구니 리스트
    Book = models.ForeignKey(Book, on_delete=models.PROTECT)
    ShoppingBasket = models.ForeignKey(ShoppingBasket, on_delete=models.PROTECT)

    def __id__(self):
        return self.id


class BookOrder(models.Model):      #책 주문내역리스트
    Book = models.ForeignKey(Book, on_delete=models.PROTECT)
    Order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    BO_count = models.IntegerField(default=0)   #책 수량
    BO_price = models.IntegerField(default=0)   #책 더한 가격
    CP_kind = models.CharField(default='', max_length=100)
    BO_DC_price = models.IntegerField(default=0)
    def __id__(self):
        return self.id


class Coupon(models.Model): #쿠폰
    User = models.ForeignKey(User, on_delete=models.PROTECT)
    CP_kind = models.CharField(max_length=100)
    CP_Used = models.BooleanField(default=0)
    CP_date = models.DateTimeField()    #사용 날짜
    CP_validity = models.CharField(max_length=100)  #유효기간

    def __id__(self):
        return self.id