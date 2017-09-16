from django.db import models

# Create your models here.

class CryptoCurrency(models.Model) :
    pszTimestamp = models.TextField(max_length=1024)
    maxMoney = models.CharField(max_length=30)
    nSubsidyHalving = models.CharField(max_length=30)
    port = models.CharField(max_length=30)
    nTime = models.CharField(max_length=30)
    nBits = models.CharField(max_length=40)
    dnsSeed = models.CharField(max_length=30)
    cAmountSubsidy = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    owner = models.ForeignKey('auth.User', related_name='cryptocurrencies', on_delete=models.CASCADE)


class FullNode(models.Model) :
    ip = models.CharField(max_length=45)
    cryptoCurrency = models.ForeignKey(CryptoCurrency, null=True)
