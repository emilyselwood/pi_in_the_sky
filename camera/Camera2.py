import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    camera.vflip = True
    camera.hflip = True
    time.sleep(5)
    camera.capture('/home/pi/Desktop/image-test.jpg')
    camera.stop_preview()
    camera.start_recording('/home/pi/Desktop/video-test.h264')
    camera.wait_recording(10)
    camera.stop_recording()

    
