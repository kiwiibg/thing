from PIL import Image, ImageOps
import requests
from io import BytesIO
import time
canvasX = 6000
canvasY = 6000

x1 = 782
y1 = 198
x2 = 903 #new one 975
y2 = 1073 #new one 1017
# ts stores the time in seconds
ts = time.time()

response = requests.get("https://raw.githubusercontent.com/italyplace/rplace/main/art.png?=" + str(ts))
img = Image.open(BytesIO(response.content))
img_orig  = Image.open(BytesIO(response.content))
img = img.resize((img.size[0] * 3, img.size[1] * 3), Image.NEAREST)

response2 = requests.get("https://raw.githubusercontent.com/italyplace/rplace/main/art-2.png?=" + str(ts))
img2 = Image.open(BytesIO(response2.content))
img2 = img2.resize((img2.size[0] * 3, img2.size[1] * 3), Image.NEAREST)

mask_url = "https://github.com/italyplace/thing/raw/main/mask2x.png"
response = requests.get(mask_url)
mask_i = Image.open(BytesIO(response.content))
#mask_i = ImageOps.invert(mask_i.convert('RGB'))
mask_i.save("mask_i.png")
mask = Image.new("1", (canvasX, canvasY), 0)
mask.paste(mask_i)
mask.save("mask.png")

tl = (x1 * 3, y1  * 3) # top left corner
tl2 = (x2 * 3, y2  * 3) # top left corner

final_img2 = Image.new('RGBA', (canvasX, canvasY))
unmasked_img2 = Image.new('RGBA', (canvasX, canvasY))
unmasked_img2.paste(img, tl)
unmasked_img2.paste(img2, tl2)

final_img2 = Image.composite(final_img2, unmasked_img2, mask)

final_img2.save("template.png")

fill_color = (69,42,0) 

img_orig = img_orig.convert("RGBA")   # it had mode P after DL it from OP
if img_orig.mode in ('RGBA', 'LA'):
    background = Image.new(img_orig.mode[:-1], img_orig.size, fill_color)
    background.paste(img_orig, img_orig.split()[-1]) # omit transparency
    img_orig = background

img_orig.save("art-botready.png")
