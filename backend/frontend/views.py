from os import name
from cv2 import imshow
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from recipe.models import Image,Category

# Create your views here.
def homePage(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        category = request.POST.get('category')
        category_final = Category.objects.filter(name=category)
        print(category_final)
        for image in images:
            #print(image)
            Image.objects.create(pantry=category_final, image=image)
            return HttpResponse('done')
    category = Category.objects.all()
    context = {'category':category}
    return render(request,'homepage.html',context)

def recipe(request):
    context = {}
    return render(request,'recipes.html',context)