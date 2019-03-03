# coding: utf-8
import time
from PIL import Image
from InstagramAPI import InstagramAPI

#ACA EN VEZ DE jnqov4 VA TU USARIO Y TU CONTRASEÑA
InstagramAPI = InstagramAPI("dankentina", "quickstart")
InstagramAPI.login()  # login



basewidth = 300
img = Image.open('dank/0001.jpg')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('dank/0001.jpg') 

basewidth = 300
img = Image.open('dank/0002.jpg')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('dank/0002.jpg') 

basewidth = 300
img = Image.open('dank/0003.jpg')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('dank/0003.jpg') 

basewidth = 300
img = Image.open('dank/0004.jpg')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('dank/0004.jpg') 

basewidth = 300
img = Image.open('dank/0005.jpg')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('dank/0005.jpg') 

photo_path = 'dank/0001.jpg'
caption = "#dank #dankmeme #dankest #dankmemesargentina #dankentina"
InstagramAPI.uploadPhoto(photo_path, caption=caption)

time.sleep(60*30)

photo_path = 'dank/0002.jpg'
caption = "#dank #dankmeme #dankest #dankmemesargentina #dankentina"
InstagramAPI.uploadPhoto(photo_path, caption=caption)

time.sleep(60*30)

photo_path = 'dank/0003.jpg'
caption = "#dank #dankmeme #dankest #dankmemesargentina #dankentina"
InstagramAPI.uploadPhoto(photo_path, caption=caption)

time.sleep(60*30)

photo_path = 'dank/0004.jpg'
caption = "#dank #dankmeme #dankest #dankmemesargentina #dankentina"
InstagramAPI.uploadPhoto(photo_path, caption=caption)

time.sleep(60*30)

photo_path = 'dank/0005.jpg'
caption = "#dank #dankmeme #dankest #dankmemesargentina #dankentina"
InstagramAPI.uploadPhoto(photo_path, caption=caption)
