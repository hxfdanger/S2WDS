import os
import tensorflow as tf
from skimage.io import imread, imshow, imsave
import numpy as np


##################################
# system
##################################
def enable_gpu(gpu_list=[0]):
    # get all the Physical GPUs in your system as a list
    gpus = tf.config.experimental.list_physical_devices("GPU")
    list_gpus = []
    print("gpus divices", gpus)
    print(gpu_list)
    if len(gpus) == 0:
        print("there are no GPU to use")
        return -1
    else:
        for i in gpu_list:
            list_gpus.append(gpus[i])
    print(list_gpus)
    try:
        # make the list of the GPUs visible (ready to use for our process )
        tf.config.experimental.set_visible_devices(list_gpus, "GPU")

        # economically allocate GPU memory
        # which attempts to allocate only as much GPU memory as needed
        # Currently, memory growth needs to be the same across GPUs
        for gpu in list_gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
            print('gpu set memory OK for gpu {}'.format(gpu))

        logical_gpus = tf.config.experimental.list_logical_devices("GPU")
        print("{} Physical GPUs , {} Logical GPU".format(len(gpus), len(logical_gpus)))
    except RuntimeError as e:
        # Visible devices must be set before GPUs have been initialized
        print(e)
        return -1
    return 1

def is_path(path):
    if os.path.exists(path):
        return path
    else:
        raise FileNotFoundError(path)
        sys.exit("[ERROR] Path doesn't exist : {}".format(path))


        
        
##################################
# others
##################################       
        
def get_files_list(path_file_names, path_for_images_folder, extension=".png"):
    file_list = []
    with open(path_file_names, 'r') as f:
        for line in f:
            file_list.append(os.path.join(path_for_images_folder, line[:-1] + extension))
    return file_list

from skimage.color import rgb2gray

def rgb_to_binery(image):
    b_image = rgb2gray(image)
    b_image[b_image > 0] = 1.0
    return b_image

def display(display_list,title_list=None):
    plt.figure(figsize=(60,30))
    if title_list is None:
        title = ['Input Image', 'PM Mask', 'Predicted Mask']
    else :title=title_list
    for i in range(len(display_list)):
        plt.subplot(1, len(display_list), i + 1)
        plt.title(title[i],c='BLACK')
        plt.imshow(display_list[i])
        plt.axis('off')
    plt.show()

def ndarray_info(data, unique=False, count_non_zero=False):
    print("#" * 50)
    print("[INFO] type          : ", data.dtype)
    print("[INFO] shape         : ", data.shape)
    print("[INFO] max           : ", data.max())
    print("[INFO] min           : ", data.min())
    print("[INFO] moy           : ", data.mean())

    if unique:
        print("[INFO] unique    : ", np.unique(data))
    if count_non_zero:
        print("[INFO] non zeros :", np.count_nonzero(data))
    print("#" * 50)
    return


def image_read(path):
    image = imread(path)
    return image

def data_read(path):
    data = image_read(path)
    return data


