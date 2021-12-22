from djitellopy import Tello
from time import sleep

me = tello.Tello()
me.connect()    # Connect to the Tello drone 
print(me.get_battery()))

#tello drone movement
me.takeoff()
me.send_rc_control(0,50,0,0)
sleep(2)
me.send_rc_control(0,0,0,0)
me.land()

#image capture
me.streamon()                                               

limit = 1
while me.streamon(limit):
    img = me.get_frame_read().frame
    img = cv2.resize(img, (640, 360))
    cv2.imshow('Tello', img)
    cv2.waitKey(1)