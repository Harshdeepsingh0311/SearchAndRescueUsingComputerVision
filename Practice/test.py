import cv2

img = cv2.imread('Shapes/2.png')
g = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
blurred = cv2.GaussianBlur(g, (5,5), 0)
edges = cv2.Canny(blurred, threshold1=50, threshold2=150)
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
detected_triangles = []
    
for contour in contours:    
    # Approximate the contour with a polygon    
    epsilon = 0.04 * cv2.arcLength(contour, True)    
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    # Check if the polygon has exactly 3 sides (a triangle)    
    if len(approx) == 3:    
        detected_triangles.append(approx)
    
    # Draw the detected triangles on the original image    
    result_image = img.copy()    
    cv2.drawContours(result_image, detected_triangles, -1, (0, 255, 0), 2)
        
# Display the result    
cv2.imshow("Detected Triangles", result_image)    
cv2.waitKey(0)    
cv2.destroyAllWindows()
