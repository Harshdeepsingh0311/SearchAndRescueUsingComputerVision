import cv2
import numpy as np

def colorize_grounds(image_path):
    image = cv2.imread(image_path)

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    lower_brown = np.array([1, 50, 50])
    upper_brown = np.array([119, 255, 255])
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])
    
    mask_brown = cv2.inRange(hsv_image, lower_brown, upper_brown)
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)
    
    result_image = image.copy()
    result_image[mask_brown > 0] = (0, 255, 255)  
    result_image[mask_green > 0] = (255, 255, 0)  
    
    cv2.imshow("Colorized Grounds", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "Shapes/3.png"
    colorize_grounds(image_path)
