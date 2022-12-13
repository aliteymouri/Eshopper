from Product.models import Category


def cat_list(req):
    categories = Category.objects.all()
    return {"categories": categories}


