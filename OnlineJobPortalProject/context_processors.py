from portal.models import Category

def get_categories(request):
    return {'categories': Category.objects.all()}