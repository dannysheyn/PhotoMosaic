from PIL import Image
import numpy as np
from numpy import asarray


class MainPic:
    def __init__(self, file_path):
        self.org_image = Image.open(file_path)
        data = asarray(self.org_image.resize((800, 800), Image.LANCZOS))
        self.org_image_array = np.array(data)
        self.mean_block_arr = []
        self.new_image = [[[]]]

    def get_resize_values(self):
        org_size = self.org_image_array.shape
        height = org_size[0]
        width = org_size[1]
        resize_couple = [(i, j) for i in range(5, height) if mod_function(height, i) for j in range(5, width)
                         if mod_function(width, j)]
        return resize_couple[0]

    def inset_block_pics_to_array(self, picture_blocks: []):
        self.mean_block_arr = [i.image_mean_resized for i in picture_blocks]
        block_height_couple = self.get_resize_values()
        block_height = block_height_couple[0]
        block_width = block_height_couple[1]
        org_arr_height = self.org_image_array.shape[0]
        org_arr_width = self.org_image_array.shape[1]
        self.new_image = np.zeros(self.org_image_array.shape)
        height_count = block_height
        width_count = block_width
        index = 0
        temp_sub_matrix = []
        for i in range(0, org_arr_height, block_height):
            for j in range(0, org_arr_width, block_width):
                temp_sub_matrix = self.org_image_array[i:height_count, j:width_count]
                index = get_closest_color_picture(self, temp_sub_matrix, picture_blocks)
                self.new_image[i:height_count, j:width_count] = picture_blocks[index].image_array_resized
                width_count += block_height
            height_count += block_height
            width_count = block_width


def create_sub_matrix(self, i_start, i_count, j_start, j_count):
    return self.org_image_array[i_start:i_count, j_start:j_count]


def get_closest_color_picture(self, submatrix, picture_blocks: []):
    mean_matrix = submatrix.mean(axis=1).mean(axis=0)
    mean_matrix_arr = [(i - mean_matrix) for i in self.mean_block_arr]
    mean_matrix_arr = list(map(abs, mean_matrix_arr))
    mean_matrix_arr = list(map(sum, mean_matrix_arr))
    return mean_matrix_arr.index(min(mean_matrix_arr))


def mod_function(divisor, divided):
    return divisor % divided == 0
