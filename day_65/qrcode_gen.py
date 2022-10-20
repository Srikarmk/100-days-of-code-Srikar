import qrcode 
import cv2
qr=qrcode.make("https://github.com/Srikarmk")
qr.save("github.jpg")

img = cv2.QRCodeDetector()
val,a,b= img.detectAndDecode(cv2.imread("github.jpg"))
print(val)