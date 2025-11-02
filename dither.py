import cv2
import numpy as np

def genBayer(n):
    if n==0:
        return np.array([[0]])
    elif n==1:
        return np.array([[0,2],[3,1]])
    else:
        smallerBayer=genBayer(n-1)
        tileSize=2**(n-1)
        top=np.hstack((4*smallerBayer,4*smallerBayer+2))
        bottom=np.hstack((4*smallerBayer+3,4*smallerBayer+1))
        return np.vstack((top,bottom))


image = cv2.imread('path_of_the_image', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image,(512,512))

bayermatrix=genBayer(4)
bayermatrix=(bayermatrix+0.5)/(256)

#print(bayermatrix.shape)

#print(image[:4, :4]/255)

bayermatrix=np.tile(bayermatrix,(32,32))
#print(bayermatrix.shape)
norm_img = image/255
dith_image = np.where(norm_img > bayermatrix, 255, 0).astype(np.uint8)



cv2.imshow('Dithered Image',dith_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
