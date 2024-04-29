from picamera2 import Picamera2, Preview
import time

def take_picture(index):
    camera = Picamera2()

    camera_config = camera.create_still_configuration(main={"size": (420, 314)}, lores={'size': (300, 300)}, display='lores')
    camera.configure(camera_config)

    camera.start()

    camera.capture_file('/home/admin/mosquito_project/MosquitoDL/mosquitos_lab_test/' + str(index) + '.jpg')

    camera.close()
