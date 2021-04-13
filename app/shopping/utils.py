import math
from io import BytesIO
from django.core.files import File
from PIL import Image

def make_thumbnail(image, size=(155, 240)):
    img = Image.open(image)
    img.convert('RGB')
    img.thumbnail(size)
    thumb_io = BytesIO()
    img.save(thumb_io, 'JPEG', quality=85)
    thumbnail = File(thumb_io, name=image.name)
    return thumbnail

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(float(n) * multiplier + 0.5) / multiplier