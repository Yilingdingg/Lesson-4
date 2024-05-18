import cv2

image=cv2.imread("crown.jpg")

#Draw circles

circle=cv2.circle(image, (259//2,194//2),100,( 196, 209, 169), 10)
cv2.imshow("Result n1", circle)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Drawing filled circles

image=cv2.imread("crown.jpg")

circle_v2=cv2.circle(image, (259//2,194//2), 75, ( 196, 209, 169), -1)
cv2.imshow("Result n2", circle_v2)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Rectangles

rectangle=cv2.rectangle(image,(20,20), (240,180), ( 196, 209, 169), -1)
cv2.imshow("Result n3", rectangle)

cv2.waitKey(0)
cv2.destroyAllWindows()

#line

image=cv2.imread("crown.jpg")

line=cv2.line(image, (50,50),(100,100), ( 100, 100, 169), 2)
cv2.imshow("Result n4",line)

cv2.waitKey(0)
cv2.destroyAllWindows()

#text

image=cv2.imread("crown.jpg")

text=cv2.putText(image, "The crown", (50,120), cv2.FONT_HERSHEY_SIMPLEX, 1, ( 100, 100, 169), 2)
cv2.imshow("Result n5 text", text)

cv2.waitKey(0)
cv2.destroyAllWindows()