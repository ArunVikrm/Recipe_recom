from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe,Image
from .serializers import RecipeSerializer,ImageSerializer
import cv2
import base64
import uuid
from django.core.files.base import ContentFile

def postImages(request):
    if request.method == 'POST':
        print(request.POST.get('category'))
        print(request.FILES)
        print(request.POST)
        # serializer = ImageSerializer(data = request.body)
        # if serializer.is_valid():
        print('done')
        # else:
        #     print(serializer.errors)

        #data = request.body.decode()

        # def to_image(data):
        #     _format,str_img = data.split(';base64')
        #     decode_file = base64.b64decode(data)
        #     fname = f"{str(uuid.uuid4())[:10]}.png"
        #     decoded_data = ContentFile(decode_file,name=fname)
        #     return decoded_data

        # decoded_data = to_image(data)

    # return HttpResponse('Item is added')
    return JsonResponse('Action performed',safe=False) 

@api_view(['GET'])
def getRecomRecipe(request):
    images_result = Image.objects.values_list('result',flat=True)
    recom_recipe = []
    ing = Recipe.objects.values_list('ingredients_list',flat=True)
    for count1,i in enumerate(ing):
        i_sep = i.split(',')
        for count,j in enumerate(i_sep):
            for res in images_result:
                if j == res:
                    recom_recipe.append(Recipe.objects.get(id=count1))
    serializer = RecipeSerializer(recom_recipe,many=True)
    return Response(serializer.data)

