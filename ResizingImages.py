import cv2
import os

# Given a directory return a list of the image's filename!
def getImages(directory):
    file_list = []

    for file in os.listdir(directory):
        if file.endswith('.jpg'):
            file_list.append(file)

    return file_list

# Given a list of images, resize it with the specified dimensions and write it to the given directory!
def resizeImages(file_list, dimensions, src_directory, dst_directory):
    for file in file_list:
        print('resized')
        image = cv2.imread(os.path.join(src_directory, file))
        resized_image = cv2.resize(image, dimensions)
        cv2.imwrite(os.path.join(dst_directory, file), resized_image)


if __name__ == '__main__':
    # Directories names
    images_directory = 'C:/1Faculdade/IniciacaoCientifica/download/Outros/Culex'
    resized_directory = os.path.join(images_directory, images_directory + '_resized')

    # Creating resized directory if not exists
    if not os.path.exists(resized_directory):
        os.makedirs(resized_directory)

    # Dimensions of the resized images
    width = 420
    height = 314
    dim = (width, height)

    # Image list given directory
    image_list = getImages(images_directory)

    # Resizing the images and writing it in the given directory
    resizeImages(image_list, dim, images_directory, resized_directory)
