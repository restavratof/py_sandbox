import cv2 as cv


def image_show(image):
    """
    Show image _in a pop-up window
    """
    # print(f'image_show - IN: {image}')
    cv.imshow('image', image)
    cv.waitKey(0)  # Will wait infinitely until any key pressed
    cv.destroyAllWindows()


def turn_to_grayscale(image):
    """
    Transform image to gray scale
    """
    # print(f'turn_to_grayscale - IN: {image}')
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)


def image_save(image, img_name):
    """
    Save image on disk
    :param image: Image
    :type image: Image
    :param img_name: Image name to save
    :type img_name: str
    """
    # print(f'image_save - IN: {image}')
    cv.imwrite(img_name, image)
    print(f'OUT: Image saved as {img_name}')
