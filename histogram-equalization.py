##############################################################
# Codeded by: Oanh Doan                               	     #
# Date      : Sep 27, 2019                                   #
# Status    : tested                                         #
# Purpose   : histogram equalization on gray and color image # 
##############################################################

'''import cv2
# apply histograme equalization on gray, and on each chanel
img = cv2.imread("oanh2.jpg")
gray = cv2.equalizeHist(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
#img_y_cr_cb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
B, G, R = cv2.split(img)

# Applying equalize Hist operation on B,G,R channel.
B_eq = cv2.equalizeHist(B)
G_eq = cv2.equalizeHist(G)
R_eq = cv2.equalizeHist(R)

img_eq = cv2.merge((B, G, R))

cv2.imwrite("B_equalizeHist.jpg", B_eq)
cv2.imwrite("G_equalizeHist.jpg ",G_eq)
cv2.imwrite("R_equalizeHist.jpg", R_eq)
cv2.imwrite("color_equalizeHist.jpg", img_rgb_eq)
cv2.imwrite("gray_equalizeHist.jpg", gray)
'''



import cv2

img = cv2.imread("oanh2.jpg")

img_y_cr_cb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
y, cr, cb = cv2.split(img_y_cr_cb)

# Applying equalize Hist operation on Y channel.
y_eq = cv2.equalizeHist(y)
cr_eq = cv2.equalizeHist(cr)
cb_eq = cv2.equalizeHist(cb)
img_eq = cv2.merge((y_eq, cr_eq, cb_eq))
img_y_eq = cv2.merge((y_eq, cr, cb))
img_cr_eq = cv2.merge((y, cr_eq, cb))
img_cb_eq = cv2.merge((y, cr, cb_eq))

img_rgb_eq = cv2.cvtColor(img_eq, cv2.COLOR_YCR_CB2BGR)
img_rgb_y = cv2.cvtColor(img_y_eq, cv2.COLOR_YCR_CB2BGR)
img_rgb_cr = cv2.cvtColor(img_cr_eq, cv2.COLOR_YCR_CB2BGR)
img_rgb_cb = cv2.cvtColor(img_cb_eq, cv2.COLOR_YCR_CB2BGR)


#img_rgb_eq = cv2.cvtColor(img_eq, cv2.COLOR_RGB2BGR)
cv2.imwrite("rgb_equalizeHist.jpg", img_rgb_eq)
cv2.imwrite("y_equalizeHist.jpg", img_rgb_y)
cv2.imwrite("cr_equalizeHist.jpg", img_rgb_cr)
cv2.imwrite("cb_equalizeHist.jpg", img_rgb_cb)


