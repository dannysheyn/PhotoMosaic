# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import MainPicture
import PicToMosiac
from PIL import Image





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = open('pictures.txt', "r")
    image_to_mosiac_path = input("enter the picture to mosiac path: ")
    main_image = MainPicture.MainPic(image_to_mosiac_path)
    image_arr = []
    for line in f:
        image_arr.append(PicToMosiac.PicClass(line[:-1], main_image.get_resize_values()))
    f.close()
    main_image.inset_block_pics_to_array(image_arr)
    new_mosaic_image = Image.fromarray(main_image.new_image.astype('uint8', 'K')).save('pic2.png')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
