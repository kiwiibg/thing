from PIL import Image, ImageOps
import requests
from io import BytesIO
import time
  
# ts stores the time in seconds
ts = time.time()

response = requests.get("https://raw.githubusercontent.com/italyplace/rplace/main/art.png?=" + str(ts))
img = Image.open(BytesIO(response.content))
img = img.resize((img.size[0] * 3, img.size[1] * 3), Image.NEAREST)

mask_url = "https://media.discordapp.net/attachments/267492253168173056/959625681141104700/mask.png"
response = requests.get(mask_url)
mask_i = Image.open(BytesIO(response.content))
#mask_i = ImageOps.invert(mask_i.convert('RGB'))
mask_i.save("mask_i.png")
mask = Image.new("1", (3000, 3000), 0)
mask.paste(mask_i)
mask.save("mask.png")

tl = (787 * 3, 254  * 3) # top left corner

final_img = Image.new('RGBA', (3000, 3000))
unmasked_img = Image.new('RGBA', (3000, 3000))
unmasked_img.paste(img, tl)
final_img = Image.composite(final_img, unmasked_img, mask)
final_img.save("template.png")

