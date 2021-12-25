from django.db import models
from django.conf import settings
import PIL.Image
from keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import cv2,os
from keras_preprocessing import image
import numpy as np

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=200)
    diet = models.CharField(max_length=50)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    flavor_profile = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    ingredients_list = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Image(models.Model):
    pantry = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField()
    result = models.CharField(max_length=50,blank=True)

    def save(self,*args,**kwargs):
        

        img = PIL.Image.open(self.image)
        img_array = image.img_to_array(img)
        resized_image = cv2.resize(img_array,(256,256))
        final_img = np.expand_dims(resized_image,0)

        if (str(self.pantry) == "Nuts and Raisins"):
            class_names = ['Almonds','Cashew nut','Pistachio','Raisins']
            file_model = os.path.join(settings.BASE_DIR,'images_1.h5')
            model = load_model(file_model)
            self.result = class_names[np.argmax(model.predict(final_img))]
        
        if(str(self.pantry) == 'Fruits'):
            class_names = ['Banana','Lemon','Mango','Orange rind','Raw papaya']
            file_model = os.path.join(settings.BASE_DIR,'images_2.h5')
            model = load_model(file_model)
            self.result = class_names[np.argmax(model.predict(final_img))]

        if(str(self.pantry) == 'Vegetables'):
            print('done')
            class_names = ['Banana flower',
                            'Beetroot',
                            'Bell pepper',
                            'Bitter gourd',
                            'Bottle gourd',
                            'Brinjal',
                            'Cabbage',
                            'Carrot',
                            'Cauliflower',
                            'Coconut',
                            'Cucumber',
                            'Drumstick',
                            'French beans',
                            'Ladies finger',
                            'Onion',
                            'Potato',
                            'Ridge gourd',
                            'Spinach',
                            'Surti papdi',
                            'Sweet potato',
                            'Tindora',
                            'Tomato']
            file_model = os.path.join(settings.BASE_DIR,'images_3.h5')
            model = load_model(file_model)
            self.result = class_names[np.argmax(model.predict(final_img))]

        if (str(self.pantry) == 'Additionals'):
            class_names = ['Bay leaf',
                            'Black pepper',
                            'Cardamom',
                            'Chili powder',
                            'Cinnamon stick',
                            'Curry leaves',
                            'Garam masala',
                            'Garlic',
                            'Ghee',
                            'Ginger',
                            'Green chilli',
                            'Kasuri methi',
                            'Oil',
                            'Rock salt',
                            'Soy sauce',
                            'Star anise',
                            'Sugar',
                            'Turmeric']
            file_model = os.path.join(settings.BASE_DIR,'images_4.h5')
            model = load_model(file_model)
            self.result = class_names[np.argmax(model.predict(final_img))]

        if (str(self.pantry) == 'Whole grain'):
            class_names = ['Maida flour','Raw Rice','Raw vermicelli','Raw Wheat','Rice flakes','Sabudana']
            file_model = os.path.join(settings.BASE_DIR,'images_5.h5')
            model = load_model(file_model)
            self.result = class_names[np.argmax(model.predict(final_img))]

        if (str(self.pantry) == 'Dal'):
            class_names = ['Bhuna chana',
                            'Chana dal',
                            'Chickpeas',
                            'Fennel seeds',
                            'Green peas',
                            'Kala chana',
                            'Masoor dal',
                            'Moong beans',
                            'Musk melon seeds',
                            'Nigella seeds',
                            'Peanuts',
                            'Red beans',
                            'Sesame seeds']
            file_model = os.path.join(settings.BASE_DIR,'images_6.h5')
            model = load_model(file_model)
            self.result = class_names[np.argmax(model.predict(final_img))]

        if (str(self.pantry) == 'Others'):
            class_names = ['Bread','Curd','Honey','Jaggery','Milk','Paneer','Saffron']
            file_model = os.path.join(settings.BASE_DIR,'images_7.h5')
            model = load_model(file_model)
            self.result = class_names[np.argmax(model.predict(final_img))]

        if (str(self.pantry) == 'Non veg meat'):
            class_names = ['Chicken meat', 'Egg', 'Fish fillets', 'Mutton meat', 'prawns']
            file_model = os.path.join(settings.BASE_DIR,'images_8.h5')
            model = load_model(file_model)
            self.result = class_names[np.argmax(model.predict(final_img))]
    
        

        return super().save(*args,**kwargs)