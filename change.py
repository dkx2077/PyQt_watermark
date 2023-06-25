from PIL import Image, ImageDraw, ImageFont


def add_watermark_fun1(img_pil):
    text = '此水印由den999生成'
    print("[INFO]PIL image info: ", img_pil.size)
    img_rgba = img_pil.convert("RGBA")

    text_img = Image.new("RGBA", img_rgba.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(text_img)

    font = ImageFont.truetype('simsun.ttc', 20)  # 字体及字体大小
    print("[INFO]Text info: ", draw.textsize(text, font=font))

    text_position = (20, 20)
    draw.text(text_position, text, font=font, fill=(128, 0, 0, 10))
    img_with_watermark = Image.alpha_composite(img_rgba, text_img)
    return img_with_watermark.convert("RGB")


def add_watermark_fun2(img_pil, text, rotate, text_size, light):
    print("[INFO]PIL image info: ", img_pil.size)
    width, height = img_pil.width, img_pil.height
    #
    new_img = Image.new('RGBA', (width * 2, height * 2), (0, 0, 0, 0))
    new_img.paste(img_pil, (width, height))
    img_rgba = new_img.convert('RGBA')

    text_img = Image.new('RGBA', img_rgba.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(text_img)
    # 添加水印
    # 文本位置, 颜色, 透明度
    font = ImageFont.truetype('simsun.ttc', text_size)
    for i in range(0, img_rgba.size[0], len(text) * 20 + 80):
        for j in range(0, img_rgba.size[1], 200):
            draw.text((i, j), text, font=font, fill=(128, 0, 0, light))
    # 旋转文字 45 度
    text_img = text_img.rotate(rotate)
    # text_img.show()
    # 合成水印图片
    img_with_watermark = Image.alpha_composite(img_rgba, text_img)
    # 原始图片尺寸
    img_with_watermark = img_with_watermark.crop((width, height, width * 2, height * 2))
    # img_with_watermark.show()
    return img_with_watermark.convert("RGB")


def work_start(old_path, pic_name_list, text, new_file, rotate=-35, text_size=30, light=50):
    print(old_path, pic_name_list, text, new_file)
    for i in range(len(pic_name_list)):
        # print(pic_name_list[i])
        old_pic_path = old_path + '/' + pic_name_list[i]
        img_pil = Image.open(old_pic_path)
        out_img1 = add_watermark_fun1(img_pil)
        out_img = add_watermark_fun2(out_img1, text, rotate, text_size, light)
        out_img.save(new_file + "/" + pic_name_list[i], 'JPEG', quality=100)
        print("[INFO]Done.")


def small_pic(old_path, pic_name_list, text, new_file, rotate=-35, text_size=30):

    pass