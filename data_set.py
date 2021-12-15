# trex oyunu veri seti toplama

import keyboard
import uuid
import time
from PIL import Image
from mss import mss

"""
oyunun adresi
https://www.trex-game.skipser.com/
"""

# ekrandan alınancak görüntünün sınırları
mon = {"top": 350, "left":700, "width":250, "height": 100}

# mss kütüphanesi ile ekrandan görüntü alma
sct = mss()

i = 0

def görüntü_kaydetme(kayit_id, key):
    global i
    i += 1

    img = sct.grab(mon)
    im = Image.frombytes("RGB", img.size, img.rgb)
    im.save("./img/{}_{}_{}.png".format(key, kayit_id, i))

# kayıt almayı sonlandırma fonksşyonu
is_exit = False
def exit():
    global is_exit
    is_exit = True

keyboard.add_hotkey("esc", callback=exit)

#isimlendirme için kayıt_id
kayit_id = uuid.uuid4()


while True:
        
    if is_exit: break

    try:
        if keyboard.is_pressed(keyboard.KEY_UP):        # zıplaması gereken yerler
                görüntü_kaydetme(kayit_id, "up" )
                time.sleep(0.1)
        elif keyboard.is_pressed(keyboard.KEY_DOWN):    # eğilmesi gereken yerler
                görüntü_kaydetme(kayit_id, "down" )
                time.sleep(0.1)
        elif keyboard.is_pressed("right"):         # hiçbirşey yapmaması gereken yerler
                görüntü_kaydetme(kayit_id, "right" )
                time.sleep(0.1)

    except RuntimeError: continue

# hata almamak için kod ile aynı dizinde img isimli bir klasör oluşturulmalıdır
  