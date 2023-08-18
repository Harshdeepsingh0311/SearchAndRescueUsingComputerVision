import cv2

img = cv2.imread('Shapes/shapes.png')
# img = img.resize(img, (img.shape[1]*2, img.shape[0]*2))
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(grayImg, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [contour], 0, (0,0,255), 5)
    pos_x = approx.ravel()[0]
    pos_y = approx.ravel()[1]-5
    b, g, r = img[pos_y+50, pos_x+10]
    b, g, r= int(b), int(g), int(r)
    shape = ''
    if len(approx)==3:
        shape = 'Triangle'
    elif len(approx)==4:
        shape = 'Quadrilateral'
    elif len(approx)==5:
        shape='Pentagon'
    elif len(approx)==6:
        shape='Hexagon'
    elif len(approx)==7:
        shape='Heptagon'
    elif len(approx)==8:
        shape='Octagon'
    elif len(approx)==9:
        shape='Nonagon'
    elif len(approx)==10:
        shape='Decagon'
    else:
        shape='Polygon'
    cv2.putText(img, shape, (pos_x,pos_y), cv2.FONT_HERSHEY_COMPLEX, 1, (b,g,r), 5)

cv2.imshow('Shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
