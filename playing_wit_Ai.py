
from keras.models import model_from_json
import numpy as np
from PIL import Image
import keyboard
import time
from mss import mss
from numpy.core.defchararray import title

mon = {"top": 350, "left":700, "width":250, "height": 100}
sct = mss()

widht = 125
height = 50

# modeli içe aktarma
model = model_from_json(open("model.json","r").read())
model.load_weights("trex_weight.h5")

# etikerler
laberls = ["Down", "Right", "Up"]


# zamanı tutmak için 
framerate_time = time.time()
counter = 0
i = 0
delay = 0.5

key_down_pressed = False

# ana döngü
while True:

    # ekrandan veri alma 
    img = sct.grab(mon)
    im = Image.frombytes("RGB", img.size, img.rgb)
    im_array = np.array(im.convert("L").resize((widht, height)))
    im_array = im_array / 255

    # model için girdiyi uygun hale getirme
    x = np.array([im_array])
    x = x.reshape(x.shape[0], widht, height, 1)

    prediction = model.predict(x)
    sonuc = np.argmax(prediction)     # tahminlerden en yüksek olasılıklı olanı alma

    
    if sonuc == 0:
        keyboard.press(keyboard.KEY_DOWN)
        key_pressed = True
    
    elif sonuc == 2:

        if key_down_pressed:
            keyboard.release(keyboard.KEY_DOWN)
            time.sleep(delay)


        keyboard.press(keyboard.KEY_UP)
        
        if (i < 1700):    # 
            time.sleep(0.30)
        elif(1700 < i) and (i < 5000):
            time.sleep(0.2) 
        else:
            time.sleep(0.1)

            keyboard.press(keyboard.KEY_DOWN)
            keyboard.release(keyboard.KEY_DOWN)
    
    counter += 1

    if (time.time() - framerate_time) > 1:

        counter = 0
        framerate_time = time.time()

        if i < 1500:
            delay -= 0.003
        else:
            delay -= 0.005
        if delay < 0:
            delay = 0


        # olasılık değerlerini yazdırma
        print(" DOWN: {} \nRight: {} \nUp: {}".format(prediction[0][0], prediction[0][1], prediction[0][2]))

        i += 1







