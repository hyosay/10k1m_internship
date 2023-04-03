import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


def compare_images(imageA, imageB):
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB, full=True)

    return m, s

image1_path = "/Users/jeonhyoseong/Tagging_system/CBImageGroup/frame" + "{}".format(i).zfill(4) + ".png"
image2_path = "/Users/jeonhyoseong/Tagging_system/CBImageGroup/frame" + "{}".format(i + 1).zfill(4) + ".png"
image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
mse_value, ssim_value = compare_images(image1, image2)



