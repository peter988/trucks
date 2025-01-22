from django.shortcuts import render
from .models import Product, Category
# Create your views here.
        
        
def filters(request):
    category = Category.objects.get(name='Filters')
    products = Product.objects.filter(category=category)
    return render(request, 'filters.html', {'products': products})

def pressuresensors(request):
    category = Category.objects.get(name='Pressure Sensors')
    products = Product.objects.filter(category=category)
    return render(request, 'pressuresensors.html', {'products': products})

def temperaturesensors(request):
    category = Category.objects.get(name='Temperature Sensors')
    products = Product.objects.filter(category=category)
    return render(request, 'temperaturesensors.html', {'products': products})

def positionandspeedsensors(request):
    category = Category.objects.get(name='Position and Speed Sensors')
    products = Product.objects.filter(category=category)
    return render(request, 'positionandspeedsensors.html', {'products': products})

def specialtysensors(request):
    category = Category.objects.get(name='Specialty Sensors')
    products = Product.objects.filter(category=category)
    return render(request, 'specialtysensors.html', {'products': products})

def mechanicalparts(request):
    category = Category.objects.get(name='Mechanical Parts')
    products = Product.objects.filter(category=category)
    return render(request, 'mechanicalparts.html', {'products': products})


def cats(request):
    return render(request, 'cats.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contact.html')

def main(request):
    # try:
    #     filters_category = Category.objects.get(name="Filters")
    # except Category.DoesNotExist:
    #     print("The 'filters' category does not exist.")
    #     filters_category = None

    # if filters_category:
    #     # Step 2: Delete all other categories and their associated products
    #     Category.objects.exclude(id=filters_category.id).delete()
        
    #     print("All categories except 'filters' and their associated products have been deleted.")
    # import_products_from_excel('C:/Users/farag/trucks-main/media/pcat.xlsx')
    # update_product_categories()
    # assign_empty_photo_to_products()
    return render(request, 'index.html')
