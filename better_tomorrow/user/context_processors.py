from . models import User
def User(request):
    links=User.objects.all()
    return dict(links=links)