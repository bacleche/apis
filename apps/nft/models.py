from django.db import models
from apps.users.models import User
from apps.core.models import BaseModel

class Collection(BaseModel):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="nft/collections/", null=True, blank=True)


class NFT(BaseModel):
    name = models.CharField(max_length=255)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="nfts")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="nft/items/")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    is_listed = models.BooleanField(default=False)


class Wallet(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, unique=True)
    balance = models.DecimalField(max_digits=20, decimal_places=4, default=0)


class Trade(BaseModel):
    nft = models.ForeignKey(NFT, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name="sales", on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, related_name="purchases", on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=4)
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("completed", "Completed"), ("cancelled", "Cancelled")], default="pending")
