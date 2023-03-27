import time
import cv2
import numpy as np
import imagezmq
from serverDef import globalVars, cameraSender, cameraServers
from picamera2 import Picamera2  


def nothing(*arg):
    pass    # Initial HSV GUI slider values to load on program start.

def maviAlgila():
    

    icol = (100, 168, 40, 145, 255, 255, 5, 5)
    lowHue = icol[0]
    lowSat = icol[1]
    lowVal = icol[2]
    highHue = icol[3]
    highSat = icol[4]
    highVal = icol[5]
    kernalSzMrph = icol[6]
    kernalSzGsn = icol[7]
    oPayi = 80

    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
    picam2.start()

    while True:
        frame = picam2.capture_array()

        # kernal = np.ones((5, 5), "uint8")
        if(globalVars.isNew):
            if(globalVars.oHueL != 0 and (not(lowHue == globalVars.oHueL))):
                lowHue = int(globalVars.oHueL)
                print("{}: {}".format("lowHue", lowHue))
            if(globalVars.oSatL != 0 and (not(lowSat == globalVars.oSatL))):
                lowSat = int(globalVars.oSatL)
                print("{}: {}".format("lowSat", lowSat))
            if(globalVars.oValL != 0 and (not(lowVal == globalVars.oValL))):
                lowVal = int(globalVars.oValL)
                print("{}: {}".format("lowVal", lowVal))
            if(globalVars.oHueH != 0 and (not(highHue == globalVars.oHueH))):
                highHue = int(globalVars.oHueH)
                print("{}: {}".format("highHue", highHue))
            if(globalVars.oSatH != 0 and (not(highSat == globalVars.oSatH))):
                highSat = int(globalVars.oSatH)
                print("{}: {}".format("highSat", highSat))
            if(globalVars.oValH != 0 and (not(highVal == globalVars.oValH))):
                highVal = int(globalVars.oValH)
                print("{}: {}".format("highVal", highVal))
            if(globalVars.oMker != 0 and (not(kernalSzMrph == globalVars.oMker))):
                kernalSzMrph = int(globalVars.oMker)
                print("{}: {}".format("kernalSzMrph", kernalSzMrph))
            if(globalVars.oGker != 0 and (not(kernalSzGsn == globalVars.oGker))):
                kernalSzGsn = int(globalVars.oGker)
                print("{}: {}".format("kernalSzGsn", kernalSzGsn))
            if(globalVars.oOpay != 0 and (not(oPayi == globalVars.oOpay))):
                oPayi = int(globalVars.oOpay)
                print("{}: {}".format("kernalSzGsn", kernalSzGsn))
            globalVars.isNew = False


        if(kernalSzMrph%2==1):
            kernalSizeMrph = (kernalSzMrph, kernalSzMrph)
        if(kernalSzGsn%2==1):
            kernalSizeGsn = (kernalSzGsn, kernalSzGsn)       
        # cv2.imshow('Raw Image', frame)
        cameraSender.send_image(cameraServers[0], frame)
        frameBGR = cv2.GaussianBlur(frame, kernalSizeGsn, 0)
        hsv = cv2.cvtColor(frameBGR, cv2.COLOR_BGR2HSV)
        colorLow = np.array([lowHue,lowSat,lowVal])      
        colorHigh = np.array([highHue,highSat,highVal])      
        mask = cv2.inRange(hsv, colorLow, colorHigh)    
        # cv2.imshow('mask-plain', mask)    

        kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernalSizeMrph)      
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)      
        # cv2.imshow('mask', mask)

        # Put mask over top of the original image.      
        result = cv2.bitwise_and(frame, frame, mask = mask)        
        # cv2.imshow('Final Image', result)
        cameraSender.send_image(cameraServers[1], result)
        contours_bl, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # contours = contours_bl[0] if len(contours_bl) == 2 else contours_bl[1]
        for pic, contour in enumerate(contours_bl):
            area = cv2.contourArea(contour)
            # print("x,y,w,h:",x,y,w,h)
            if(area>10000):
                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(result, (x, y), (x+w, y+h), (0, 0, 255), 2)
                centerX = x + (w // 2)
                centerY = y + (h // 2)
                komut = ortala(centerX=centerX, centerY=centerY, width=w, height=h, ortalamapayi=oPayi)
                print("area:{}\tx:{},y:{},w:{},h:{},k:{}".format(area,x,y,w,h,komut))

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
  
    cv2.destroyAllWindows()
    camera.release()


def ortala(centerX, centerY, width, height, ortalamapayi):
    if centerX < 320 - ortalamapayi:
        # print("Solda")
        return goBATI(1)

    if centerX > 320 + ortalamapayi:
        # print("Sagda")
        return goDOGU(1)

    if centerY > 240 + ortalamapayi:
        # print("Aşağıda")
        return goGUNEY(1)

    if centerY < 240 - ortalamapayi:
        # print("Yukarda")
        return goKUZEY(1)

    if centerX >= 320 - ortalamapayi and centerX <= 320 + ortalamapayi and centerY <= 240 + ortalamapayi and centerY >= 240 - ortalamapayi:
        return("ortalandı")

def goDOGU(süre):
    ##send_velocity(0, 0.35, 0, süre)
    return("Doguya gitmen gerekiyor.")


def goBATI(süre):
    ##send_velocity(0, -0.35, 0, süre)
    return("Batiya gitmen gerekiyor.")


def goKUZEY(süre):
    ##send_velocity(0.35, 0, 0, süre)
    return("Kuzeye gitmen gerekiyor.")


def goGUNEY(süre):
   ## send_velocity(-0.35, 0, 0, süre)
    return("Guneye gitmen gerekiyor.")

if __name__=="__main__":
   while True:
       maviAlgila()