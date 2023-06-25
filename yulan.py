import os
from PIL import Image, ImageDraw, ImageFont


def small_pic(text, rotate=0, text_size=30*3, light=50):
    width, height = 200, 70
    new_img = Image.new('RGBA', (width * 3, height * 3), (0, 0, 0, 0))
    img_rgba = new_img.convert('RGBA')
    text_img = Image.new('RGBA', img_rgba.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(text_img)
    # 文本位置, 颜色, 透明度
    font = ImageFont.truetype('simsun.ttc', text_size)
    draw.text((80, 40), text, font=font, fill=(0, 0, 0, light))
    text_img = text_img.rotate(rotate)
    return text_img

def big_pic(text, rotate=0, text_size=15, light=50):
    width, height = 330, 110
    new_img = Image.new('RGBA', (width * 2, height * 2), (0, 0, 0, 0))
    img_rgba = new_img.convert('RGBA')

    text_img = Image.new('RGBA', img_rgba.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(text_img)
    font = ImageFont.truetype('simsun.ttc', text_size)
    for i in range(0, img_rgba.size[0], len(text) * text_size + 50):
        for j in range(0, img_rgba.size[1], text_size*3):
            draw.text((i, j), text, font=font, fill=(0, 0, 0, light))
    # 旋转文字 45 度
    text_img2 = text_img.rotate(rotate)
    # text_img.show()
    return text_img2



