#a very simple gallery
init python:

    maxnumx = 3
    maxnumy = 3
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0
    closeup_page = 0


    class GalleryItem:
        def __init__(self, name, images, thumb, locked="lockedthumb"):
            self.name = name
            self.images = images
            self.thumb = thumb
            self.locked = locked
            self.refresh_lock()

        def num_images(self):
            return len(self.images)

        def refresh_lock(self):
            self.num_unlocked = 0
            lockme = False
            for img in self.images:
                if not renpy.seen_image(img):
                    lockme = True
                else:
                    self.num_unlocked += 1
            self.is_locked = lockme

    gallery_items = []
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["ColorCode"], "thumb51"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1SHS"], "thumb1"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1SHS2"], "thumb2"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1SHS3"], "thumb3"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1SHS4"], "thumb4"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1SHS5"], "thumb5"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1SHS6"], "thumb6"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1SHS7"], "thumb7"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1SHS8"], "thumb8"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1SHS9"], "thumb9"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1SHS10"], "thumb10"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1SHS11"], "thumb11"))

    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L2SHS"], "thumb12"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L2SHS2"], "thumb13"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L2SHS3"], "thumb14"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L2SHS4"], "thumb15"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L2SHS5"], "thumb16"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L2SHS6"], "thumb17"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L2SHS7"], "thumb18"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L2SHS8"], "thumb19"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L2SHS9"], "thumb20"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L2SHS10"], "thumb21"))

    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L3SHS"], "thumb22"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L3SHS2"], "thumb23"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L3SHS3"], "thumb24"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L3SHS4"], "thumb25"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L3SHS5"], "thumb26"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L3SHS6"], "thumb27"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L3SHS7"], "thumb28"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L3SHS8"], "thumb29"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L3SHS9"], "thumb30"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L3SHS10"], "thumb31"))

    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1College"], "thumb32"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1College2"], "thumb33"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1College3"], "thumb34"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1College4"], "thumb35"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1College5"], "thumb36"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1College6"], "thumb37"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1College7"], "thumb38"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1College8"], "thumb39"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1College9"], "thumb40"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1College10"], "thumb41"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L1College11"], "thumb42"))

    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L2College"], "thumb43"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L2College2"], "thumb44"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L2College3"], "thumb45"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L2College4"], "thumb46"))

    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L3College"], "thumb47"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L3College2"], "thumb48"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L3College3"], "thumb49"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["L3College4"], "thumb50"))




#gallery background
image gray = "#777"

#384x216 (16x9) set 1280x720p for the lock and all thumbnails
#600x338 (16x9) set 1920x1080 for the lock and thumbnails
#gallery locked image
image lockedthumb = ("images/Gallery/thumbs/tgallery0.jpg")


#gallery images
image ColorCode= ("images/ColorCode.jpg")
image L1SHS1 = ("images/SHSLessons/L1SHS.png")
image L1SHS2 = ("images/SHSLessons/L1SHS2.png")
image L1SHS3 = ("images/SHSLessons/L1SHS3.png")
image L1SHS4 = ("images/SHSLessons/L1SHS4.png")
image L1SHS5 = ("images/SHSLessons/L1SHS5.png")
image L1SHS6 = ("images/SHSLessons/L1SHS6.png")
image L1SHS7 = ("images/SHSLessons/L1SHS7.png")
image L1SHS8 = ("images/SHSLessons/L1SHS8.png")
image L1SHS9 = ("images/SHSLessons/L1SHS9.png")
image L1SHS10 = ("images/SHSLessons/L1SHS10.png")
image L1SHS11 = ("images/SHSLessons/L1SHS11.png")
image L2SHS = ("images/SHSLessons/L2SHS.jpg")
image L2SHS2 = ("images/SHSLessons/L2SHS2.png")
image L2SHS3 = ("images/SHSLessons/L2SHS3.png")
image L2SHS4 = ("images/SHSLessons/L2SHS4.png")
image L2SHS5 = ("images/SHSLessons/L2SHS5.png")
image L2SHS6 = ("images/SHSLessons/L2SHS6.png")
image L2SHS7 = ("images/SHSLessons/L2SHS7.png")
image L2SHS8 = ("images/SHSLessons/L2SHS8.png")
image L2SHS9 = ("images/SHSLessons/L2SHS9.png")
image L2SHS10 = ("images/SHSLessons/L2SHS10.png")
image L3SHS = ("images/SHSLessons/L3SHS.jpg")
image L3SHS2 = ("images/SHSLessons/L3SHS2.png")
image L3SHS3 = ("images/SHSLessons/L3SHS3.png")
image L3SHS4 = ("images/SHSLessons/L3SHS4.png")
image L3SHS5 = ("images/SHSLessons/L3SHS5.png")
image L3SHS6 = ("images/SHSLessons/L3SHS6.png")
image L3SHS7 = ("images/SHSLessons/L3SHS7.png")
image L3SHS8 = ("images/SHSLessons/L3SHS8.png")
image L3SHS9 = ("images/SHSLessons/L3SHS9.png")
image L3SHS10 = ("images/SHSLessons/L3SHS10.png")



#gallery thumbnails images
image thumb51 = ("images/gallery/thumbs/51.jpg")
image thumb1 = ("images/gallery/thumbs/1.jpg")
image thumb2 = ("images/gallery/thumbs/2.jpg")
image thumb3 = ("images/gallery/thumbs/3.jpg")
image thumb4 = ("images/gallery/thumbs/4.jpg")
image thumb5 = ("images/gallery/thumbs/5.jpg")
image thumb6 = ("images/gallery/thumbs/6.jpg")
image thumb7 = ("images/gallery/thumbs/7.jpg")
image thumb8 = ("images/gallery/thumbs/8.jpg")
image thumb9 = ("images/gallery/thumbs/9.jpg")
image thumb10 = ("images/gallery/thumbs/10.jpg")
image thumb11 = ("images/gallery/thumbs/11.jpg")
image thumb12 = ("images/gallery/thumbs/12.jpg")
image thumb13 = ("images/gallery/thumbs/13.jpg")
image thumb14 = ("images/gallery/thumbs/14.jpg")
image thumb15 = ("images/gallery/thumbs/15.jpg")
image thumb16 = ("images/gallery/thumbs/16.jpg")
image thumb17 = ("images/gallery/thumbs/17.jpg")
image thumb18 = ("images/gallery/thumbs/18.jpg")
image thumb19 = ("images/gallery/thumbs/19.jpg")
image thumb20 = ("images/gallery/thumbs/20.jpg")
image thumb21 = ("images/gallery/thumbs/21.jpg")
image thumb22 = ("images/gallery/thumbs/22.jpg")
image thumb23 = ("images/gallery/thumbs/23.jpg")
image thumb24 = ("images/gallery/thumbs/24.jpg")
image thumb25 = ("images/gallery/thumbs/25.jpg")
image thumb26 = ("images/gallery/thumbs/26.jpg")
image thumb27 = ("images/gallery/thumbs/27.jpg")
image thumb28 = ("images/gallery/thumbs/28.jpg")
image thumb29 = ("images/gallery/thumbs/29.jpg")
image thumb30 = ("images/gallery/thumbs/30.jpg")
image thumb31 = ("images/gallery/thumbs/31.jpg")
image thumb32 = ("images/gallery/thumbs/32.jpg")
image thumb33 = ("images/gallery/thumbs/33.jpg")
image thumb34 = ("images/gallery/thumbs/34.jpg")
image thumb35 = ("images/gallery/thumbs/35.jpg")
image thumb36 = ("images/gallery/thumbs/36.jpg")
image thumb37 = ("images/gallery/thumbs/37.jpg")
image thumb38 = ("images/gallery/thumbs/38.jpg")
image thumb39 = ("images/gallery/thumbs/39.jpg")
image thumb40 = ("images/gallery/thumbs/40.jpg")
image thumb41 = ("images/gallery/thumbs/41.jpg")
image thumb42 = ("images/gallery/thumbs/42.jpg")
image thumb43 = ("images/gallery/thumbs/43.jpg")
image thumb44 = ("images/gallery/thumbs/44.jpg")
image thumb45 = ("images/gallery/thumbs/45.jpg")
image thumb46 = ("images/gallery/thumbs/46.jpg")
image thumb47 = ("images/gallery/thumbs/47.jpg")
image thumb48 = ("images/gallery/thumbs/48.jpg")
image thumb49 = ("images/gallery/thumbs/49.jpg")
image thumb50 = ("images/gallery/thumbs/50.jpg")
