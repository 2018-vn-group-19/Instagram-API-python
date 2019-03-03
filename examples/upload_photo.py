import time
from InstagramAPI import InstagramAPI

#ACA EN VEZ DE jnqov4 VA TU USARIO Y TU CONTRASEÑA
InstagramAPI = InstagramAPI("jnqov4", "MjYads9Yd22upWi")
InstagramAPI.login()  # login

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
