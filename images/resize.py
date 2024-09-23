from PIL import Image
import sys

filename = sys.argv[1]
name, extension = filename.split(".")


img = Image.open(filename)
cw, ch = img.size
max_height = cw/3
banner = None
pleased = False
while(pleased == False):
  if(max_height > ch):
    max_width = 3*ch
    center = cw/2
    cr = (cw-max_width)/2
    shift = int(input(f"Center shift (-{cr}, {cr}): "))
    center += shift
    banner = img.crop((center-max_width/2, 0, center+max_width/2, ch))
  else:
    center = ch/2
    cr = (ch-max_height)/2
    shift = int(input(f"Center shift (-{cr}, {cr}): "))
    center += shift
    banner = img.crop((0, center-max_height/2, cw, center+max_height/2))
  banner.show()
  pleased = (input("Enter 'y' if you are happy with this image: ").lower() == 'y')
banner.save(f"banners/{filename}")

bw, bh = banner.size
width = bh*16/9
thumbnail = None
pleased = False
while(pleased == False):
  center = bw/2
  cr = (bw-width)/2
  shift = int(input(f"Center shift (-{cr}, {cr}): "))
  center += shift
  thumbnail = banner.crop((center-width/2, 0, center+width/2, bh))
  thumbnail.show()
  pleased = (input("Enter 'y' if you are happy with this image: ").lower() == 'y')
thumbnail.save(f"thumbnails/{filename}")