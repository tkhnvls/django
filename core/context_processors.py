from .models import Stranica
def pages_nav(request): return {'pages': Stranica.objects.all()}
