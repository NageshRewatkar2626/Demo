import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


im_cv = cv2.imread('C:/Users/Hp/Desktop/Class Base View/Quiz_Api/templates/nag.jpg')
# im_cv = cv2.cvtColor(im_cv,cv2.COLOR_BGR2RGB)
# img_scaled=cv2.resize(im_cv,None,fx=0.10,fy=0.10)
# cv2.imshow('Result',img_scaled)
text = pytesseract.image_to_string(im_cv, lang = 'hin')
print(len(text))
# print(pytesseract.image_to_boxes(img_scaled))
# cv2.imshow('Result',img_scaled)
# cv2.waitKey(0)
import codecs
f = codecs.open('zala.txt', encoding='utf-8', mode='w')
f.write(text)
f.close()
file1 = open("zala.txt", encoding='utf-8',mode="r+")
file1.seek(0)

print ("Output of Readline function is ")
print (file1.readline())
