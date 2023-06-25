import os
import change

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print
        "---  new folder...  ---"
        print
        "---  OK  ---"
    else:
        print
        "---  There is this folder!  ---"

###################################################

def find_all(old_path):
    # path_imgs = 'chat'
    pic = []
    for file in os.listdir(old_path):
        if file.endswith('PNG') or file.endswith('JPG') \
                or file.endswith('jpg') or file.endswith('png') \
                or file.endswith('jpeg') or file.endswith('JPEG'):
            # src = old_path + '/' + file
            src = file
            # print(src)
            pic.append(src)
    return pic


