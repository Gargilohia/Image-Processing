#!/usr/bin/env python
# coding: utf-8

# In[1]:


import imutils
import cv2


# In[2]:


image = cv2.imread("jp.png")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))


# In[3]:


cv2.imshow("Image", image)
cv2.waitKey(0)


# In[4]:


(B,G,R) = image[100,50]


# In[5]:


print("R={}, G={}, B={}".format(R,G,B))


# In[11]:


roi = image[100:300,650:850]
cv2.imshow("ROI", roi)
cv2.waitKey(0) #https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/


# In[12]:


resized = cv2.resize(image,(200,200))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)


# In[13]:


#Manual Resizing maintaining aspect ratio


r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)


# In[14]:


#Resizing while maintaining aspect ratio easily using imutils

resized= imutils.resize(image, width=300)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)


# In[16]:


##Rotating the image 


center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M , (w,h))
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)


# In[18]:


#Rotating using imutils 

rotated =  imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)


# In[19]:


#rotating without clipping the image

rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated )
cv2.waitKey(0)


# In[20]:


#Smoothing the immage 

blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)


# In[25]:


#Drawing on an image

output = image.copy()
cv2.rectangle(output, (658, 82), (850, 333), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)


# In[26]:


output = image.copy()
cv2.circle(output, (711, 385), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(0)


# In[27]:


output = image.copy()
cv2.line(output, (31, 21), (768, 505), (0, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)


# In[28]:


#Writing text 

output = image.copy()
cv2.putText(output, "OpenCV + Jurassic Park!!!", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)


# In[ ]:




