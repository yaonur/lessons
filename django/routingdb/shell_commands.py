from mongo_app.models import Account, Proxy

ss = Account.objects.all()
Proxy.objects.create(proxy='proxy_3')
proxy = Proxy.objects.filter(proxy='proxy_3')[0]
proxy.save()
Account.objects.create(name='a', proxy=proxy)
