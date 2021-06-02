import cv2


#function for taking an image

def make_cartoon(file_path):
    img = cv2.imread(file_path)

    # Get the edges
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 165, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 1001, 51)

    # To blur the coloured version of image
    color = cv2.bilateralFilter(img, 45, 300, 300)

    # Creating the Cartoon
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon