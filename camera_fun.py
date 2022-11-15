#camera librarys
import time
import os
from picamera import PiCamera
camera = PiCamera()

def take_picture(string, num_id):
    camera.resolution = (3280, 2464)
    camera.start_preview() #optional
    time.sleep(3) #: it’s important to sleep for at least two seconds before capturing an image,
                  #  because this gives the camera’s sensor time to sense the light levels.
    #camera.capture("/home/pi/Desktop/project/"+string+".jpg")
    #path_windows = os.getcwd()+"\\Users\\"+num_id+"\\"+string+".jpg"
    path_linux = os.getcwd()+"/Users/"+num_id+"/"+string+".jpg"
    camera.capture(path_linux)
    camera.stop_preview() #optional


def clean_target_picture():
    camera.resolution = (3280, 2464)
    camera.start_preview() #optional
    time.sleep(3) #: it’s important to sleep for at least two seconds before capturing an image,
                  #  because this gives the camera’s sensor time to sense the light levels.
    path_linux = os.getcwd()+"/clean_target.jpg"
    camera.capture(path_linux)
    camera.stop_preview() #optional

if __name__ == "__main__":
    pass
    #take_picture("target1")
    #take_picture("testt1")

"""def testt(string, num_id):
    path_windows = os.getcwd()+"\\Users\\"+num_id+"\\"
    path_linux = os.getcwd()+"/Users/"+num_id+"/"
    print(os.path.join(path_windows , string+".jpg"))
    print(os.path.join(path_linux , string+".jpg"))

if __name__ == "__main__":
    testt("image1", "209403344")"""