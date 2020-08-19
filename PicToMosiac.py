from PIL import Image
import numpy as np
from numpy import asarray

class PicClass:
    def __init__(self, file_path, resize_value: (int, int)):
        self.originalImage = Image.open(file_path)
        self.image_sequence = asarray(self.originalImage)
        self.resized_image = self.originalImage.resize((resize_value[0], resize_value[1]), Image.LANCZOS)
        self.image_array = np.array(self.image_sequence)
        self.image_array_resized = np.array(asarray(self.resized_image))
        array_org = np.array(self.image_sequence)
        self.image_mean_original = array_org.mean(axis=1).mean(axis=0)
        self.image_mean_resized = self.image_array.mean(axis=1).mean(axis=0)

