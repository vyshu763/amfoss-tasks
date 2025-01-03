from PIL import Image, ImageDraw, ImageFont
# this line generates white background and these numbers are pixels
img = Image.new('RGB', (200, 50), color=(255, 255, 255))
# this line is to intilize drawing
d = ImageDraw.Draw(img)
# for giving the font
font = ImageFont.truetype("DejaVuSans-Bold.ttf", 40) 
# to draw 2+2 text on the image 
d.text((50, 5), "2 + 2", fill=(0, 0, 0), font=font)
# to save the image
img.save("/home/vyshnavi/Documents/2+2.png")

