from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

# 商品モデル作成 DBテーブルでカラム作成のイメージ
#商品（商品名、値段、カテゴリー、URLスラグ、商品説明、画像）
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=100)
    slug = models.SlugField() #文字、ハイフン、数字、アンダースコアだけを含んだ文字列　URLの一部に使用する
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

#注文商品　（ユーザー、
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #外部キー
    ordered = models.BooleanField(default = False) 
    item = models.ForeignKey(Item, on_delete=models.CASCADE) #Itemモデルと紐付け
    quantity = models.IntegerField(default=1) #注文数フィールド

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def __str__(self):
        return f'{self.item.title}:{self.quantity}'


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items =models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True) #注文日
    ordered_date = models.DateTimeField() #注文完了日
    ordered = models.BooleanField(default=False) #注文完了したかのフラグ
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total

    def __str__ (self):
        return self.user.email

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    stripe_charge_id = models.CharField(max_length=50)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

