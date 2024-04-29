from picamera2 import Picamera2, Preview
import time

camera = Picamera2()

camera_config = camera.create_still_configuration(main={"size": (420, 314)}, lores={'size': (300, 300)}, display='lores')
camera.configure(camera_config)

camera.start_preview(Preview.QTGL)

camera.start()
time.sleep(300000)
camera.close()
