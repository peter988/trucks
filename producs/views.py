from django.shortcuts import render
from .models import Product, Category
# Create your views here.

def filters(request):
    category = Category.objects.get(name='Filters')
    products = Product.objects.filter(category=category)
    return render(request, 'filters.html', {'products': products})

def bushing(request):
    category = Category.objects.get(name='BUSHING')
    products = Product.objects.filter(category=category)
    return render(request, 'bushing.html', {'products': products})

def insulator(request):
    category = Category.objects.get(name='INSULATOR')
    products = Product.objects.filter(category=category)
    return render(request, 'insulator.html', {'products': products})

def engine_mounting(request):
    category = Category.objects.get(name='ENGINE MOUTNING')
    products = Product.objects.filter(category=category)
    return render(request, 'engine_mounting.html', {'products': products})

def center_bearing(request):
    category = Category.objects.get(name='CENTER BEARING')
    products = Product.objects.filter(category=category)
    return render(request, 'center_bearing.html', {'products': products})

def torque_bushing(request):
    category = Category.objects.get(name='TORQUE BUSHING')
    products = Product.objects.filter(category=category)
    return render(request, 'torque_bushing.html', {'products': products})

def equaliser_hutch(request):
    category = Category.objects.get(name='EQUALISER HUTCH')
    products = Product.objects.filter(category=category)
    return render(request, 'equaliser_hutch.html', {'products': products})

def equaliser_bush(request):
    category = Category.objects.get(name='EQULISER BUSH')
    products = Product.objects.filter(category=category)
    return render(request, 'equaliser_bush.html', {'products': products})

def bolt_repair_kit_for_equaliser(request):
    category = Category.objects.get(name='BOLT REPAIR KIT FOR EQUALISER')
    products = Product.objects.filter(category=category)
    return render(request, 'bolt_repair_kit_for_equaliser.html', {'products': products})

def cabin_mounting(request):
    category = Category.objects.get(name='CABIN MOUNTING')
    products = Product.objects.filter(category=category)
    return render(request, 'cabin_mounting.html', {'products': products})

def radiator_mounting(request):
    category = Category.objects.get(name='RADIATOR MOUNTING')
    products = Product.objects.filter(category=category)
    return render(request, 'radiator_mounting.html', {'products': products})

def bronze_bushing_trunnion(request):
    category = Category.objects.get(name='BRONZE BUSHING TRUNNION')
    products = Product.objects.filter(category=category)
    return render(request, 'bronze_bushing_trunnion.html', {'products': products})

def brass_washer_for_trunnion(request):
    category = Category.objects.get(name='BRASS WASHER FOR TRUNNION')
    products = Product.objects.filter(category=category)
    return render(request, 'brass_washer_for_trunnion.html', {'products': products})

def trunnion(request):
    category = Category.objects.get(name='TRUNNION')
    products = Product.objects.filter(category=category)
    return render(request, 'trunnion.html', {'products': products})

def brass_washer_for_trunnion_4(request):
    category = Category.objects.get(name='BRASS WASHER FOR TRUNNION 4')
    products = Product.objects.filter(category=category)
    return render(request, 'brass_washer_for_trunnion_4.html', {'products': products})

def spring_mounting(request):
    category = Category.objects.get(name='SPRING MOUTNING')
    products = Product.objects.filter(category=category)
    return render(request, 'spring_mounting.html', {'products': products})

def torque_rod(request):
    category = Category.objects.get(name='TORQUE ROD')
    products = Product.objects.filter(category=category)
    return render(request, 'torque_rod.html', {'products': products})

def spring_bushing(request):
    category = Category.objects.get(name='SPRING BUSHING')
    products = Product.objects.filter(category=category)
    return render(request, 'spring_bushing.html', {'products': products})

def torque_rod_bush(request):
    category = Category.objects.get(name='TORQUE ROD BUSH')
    products = Product.objects.filter(category=category)
    return render(request, 'torque_rod_bush.html', {'products': products})

def king_pin(request):
    category = Category.objects.get(name='KING PIN')
    products = Product.objects.filter(category=category)
    return render(request, 'king_pin.html', {'products': products})

def torque_bush(request):
    category = Category.objects.get(name='TORQUE BUSH')
    products = Product.objects.filter(category=category)
    return render(request, 'torque_bush.html', {'products': products})

def equaliser_bush(request):
    category = Category.objects.get(name='EQUALISER BUSH')
    products = Product.objects.filter(category=category)
    return render(request, 'equaliser_bush.html', {'products': products})

def cats(request):
    return render(request, 'cats.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contact.html')

def main(request):
    return render(request, 'index.html')
