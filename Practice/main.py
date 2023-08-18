import cv2

img = cv2.imread('Shapes/triangle.png') # Reading the image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converting it to grayscale
_, thrash = cv2.threshold(imgGray, 240, 255, cv2.THRESH_BINARY) 
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) # Searching the contours of the shapes

# cv2.imshow("img", img)
#Looping through all the contours
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)

    # Drawing contours
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)

    # Position of Caption
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    if len(approx) == 3:
        # It's a triangle
        cv2.putText(img, "House", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    

# Showing the img after detection
cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()