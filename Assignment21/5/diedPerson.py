import cv2

person = cv2.imread('5/person.jpg', 0)
# print(person.shape)

for i in range(43):
    if i <= 30:
        for j in range(30-i, 43-i):
            if (j >= 0):
                person[i, j] = 0
    else:
        for j in range(0, 43-i):
            if (j >= 0):
                person[i, j] = 0
    
cv2.imwrite('5/diedPerson.jpg', person)
# cv2.imshow('m', person)
cv2.waitKey()