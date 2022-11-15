import cv2 as cv
import numpy as np
import os

def process_image(img, string, num_id):
    #resize original image
    img = cv.resize(img, (640, 480))
    img_to_dilation = img.copy()
    img_to_dilation = cv.medianBlur(img_to_dilation, 9)
    #img_to_dilation = cv.GaussianBlur(img,(5,5),0)

    output = img.copy()

    #load and resize the target image (clean target)
    img_target = cv.imread('clean_target.jpg')
    #img_target = cv.imread(os.getcwd()+'\\only_test\\test1.jpg')
    #img_target = cv.imread(os.getcwd()+'\\test_clean_target.jpg')
    img_target = cv.resize(img_target, (640, 480))

    #dilation of target image
    _, mask = cv.threshold(img_target, 50, 255, cv.THRESH_BINARY_INV)

    kernal_before_resize = cv.imread('fullcircle.png', 0)
    kernal = cv.resize(kernal_before_resize, (1,1))
    img_target = cv.dilate(mask, kernal, iterations=1)

    #convert dilation of the target image from BGR to grayscale
    img_target = cv.cvtColor(img_target, cv.COLOR_BGR2GRAY)

    # convert the grayscale dilation of the target image to binary image
    ret,thresh = cv.threshold(img_target,127,255,0)

    #find contours from target image

    #******************************************************************************************#
    #important!!!! in windows::
    #target_contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    #important!!!! in raspberry::
    im2, target_contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    #******************************************************************************************#

    #draw the contours that we find at target image in the dilation of the original image
    cv.drawContours(img_to_dilation, target_contours, -1, (255,255,255), 3)
    #cv.imshow("Image", img_to_dilation)
    #cv.waitKey(0)

    #dilation of original image
    _, mask = cv.threshold(img_to_dilation, 50, 255, cv.THRESH_BINARY_INV)

    kernal_before_resize = cv.imread('fullcircle.png', 0)
    kernal = cv.resize(kernal_before_resize, (6,6))
    gray_image = cv.dilate(mask, kernal, iterations=1)

    # convert the dilation of original image to grayscale
    gray_image = cv.cvtColor(gray_image, cv.COLOR_BGR2GRAY)
    #cv.imshow("Image", gray_image)
    #cv.waitKey(0)

    # convert the grayscale dilation of the original image to binary image
    ret,thresh = cv.threshold(gray_image,127,255,0)
    
    #find contours from dilation of the original image

    #******************************************************************************************#
    #important!!!! in windows::
    #contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    #important!!!! in raspberry::
    im2, contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    #******************************************************************************************#

    cv.drawContours(output, contours, -1, (255,0,0), 6)
    path_windows = os.getcwd()+"\\Users\\"+num_id+"\\"
    path_linux = os.getcwd()+"/Users/"+num_id+"/"
    cv.imwrite(os.path.join(path_linux , string+".jpg"), output) 
    #cv.imwrite(os.path.join(path_windows , string+".jpg"), output)

    cv.drawContours(output, contours, -1, (255,0,0), 25)
    #cv.imshow("Image", output)
    #cv.imshow("Image", gray_image)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    
    path_windows = os.getcwd()+"\\Users\\"+num_id+"\\"
    path_linux = os.getcwd()+"/Users/"+num_id+"/"
    cv.imwrite(os.path.join(path_linux , string+'_to_statistics' +".jpg"), output) 
    #cv.imwrite(os.path.join(path_windows , string+'_to_statistics' +".jpg"), output)

    bullets_number = len(contours)
    return bullets_number


def show_statistics(num_id):
    path_linux1 = os.getcwd()+"/Users/"+num_id+"/output1_to_statistics.jpg"
    path_linux2 = os.getcwd()+"/Users/"+num_id+"/output2_to_statistics.jpg"
    path_linux3 = os.getcwd()+"/Users/"+num_id+"/output3_to_statistics.jpg"
    path_linux = os.getcwd()+"/Users/"+num_id+"/common_targets_of_2.jpg"
    path_linux4 = os.getcwd()+"/Users/"+num_id+"/common_targets_of_3.jpg"


    isFile1 = os.path.isfile(path_linux1)
    isFile2 = os.path.isfile(path_linux2)
    isFile3 = os.path.isfile(path_linux3)
    isFile4 = os.path.isfile(path_linux)

    if ((isFile3) and (isFile4)):
        output_1_2 = cv.imread(path_linux)
        output3 = cv.imread(path_linux3)

        cnt_col=0
        cnt_row=0
        for row in output3:
            cnt_col=0
            for col in row:
                if list(col) >= [245,0,0] and output_1_2[cnt_row][cnt_col][2] >= 245: 
                    output_1_2[cnt_row][cnt_col] = [0,255,0]
                cnt_col+=1
            cnt_row+=1

        cv.imshow('output2', output_1_2)
        cv.waitKey(0)
        #cv.destroyAllWindows()
        cv.imwrite(path_linux4, output_1_2)
        string = "common_targets_of_3"


    elif ((isFile1) and (isFile2)):
        output1 = cv.imread(path_linux1)
        output2 = cv.imread(path_linux2)

        cnt_col=0
        cnt_row=0
        for row in output1:
            cnt_col=0
            for col in row:
                if list(col) >= [245,0,0] and list(output2[cnt_row][cnt_col]) >= [245,0,0]: 
                    output2[cnt_row][cnt_col] = [0,0,255]
                cnt_col+=1
            cnt_row+=1

        #cv.imshow('output2', output2)
        #cv.waitKey(0)
        #cv.destroyAllWindows()
        cv.imwrite(path_linux, output2)
        string = "common_targets_of_2"

    else:
        string = -1


    return string

  


if __name__ == "__main__":

    #img1 = cv.imread(os.getcwd()+'\\only_test\\test2.jpg')
    #process_image(img1, "output1", "209403344")

    show_statistics("209403344")

    """img1 = cv.imread(os.getcwd()+'\\test1.jpg')
    process_image(img1, "output1", "209403344")"""


    """img2 = cv.imread('test1.jpg')
    process_image(img2, "output2")

    output1= cv.imread('output1.png')
    output2= cv.imread('output2.png')

    output1= cv.imread('output1.png')
    output2= cv.imread('output2.png')
    find_common_targets(output1, output2, "common_targets")"""


"""def process_image(img, string, num_id):
    #resize original image
    img = cv.resize(img, (640, 480))
    img_to_dilation = img.copy()
    #img_to_dilation = cv.medianBlur(img_to_dilation, 9)
    img_to_dilation = cv.GaussianBlur(img,(5,5),0)

    output = img.copy()

    #load and resize the target image (clean target)
    #####################################################################img_target = cv.imread('clean_target.jpg') להחזירררררררררררררררררר
    img_target = cv.imread(os.getcwd()+'\\only_test\\test1.jpg')
    #img_target = cv.imread(os.getcwd()+'\\test_clean_target.jpg')
    img_target = cv.resize(img_target, (640, 480))

    #dilation of target image
    _, mask = cv.threshold(img_target, 50, 255, cv.THRESH_BINARY_INV)

    kernal_before_resize = cv.imread('fullcircle.png', 0)
    kernal = cv.resize(kernal_before_resize, (1,1))
    img_target = cv.dilate(mask, kernal, iterations=1)

    #convert dilation of the target image from BGR to grayscale
    img_target = cv.cvtColor(img_target, cv.COLOR_BGR2GRAY)

    # convert the grayscale dilation of the target image to binary image
    ret,thresh = cv.threshold(img_target,127,255,0)

    #find contours from target image

    #******************************************************************************************#
    #important!!!! in windows::
    target_contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    #important!!!! in raspberry::
    #im2, target_contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)להחזיררררררררררררררררררררררררררררררררררררר
    #******************************************************************************************#

    #draw the contours that we find at target image in the dilation of the original image
    cv.drawContours(img_to_dilation, target_contours, -1, (255,255,255), 3)
    #cv.imshow("Image", img_to_dilation)
    #cv.waitKey(0)

    #dilation of original image
    _, mask = cv.threshold(img_to_dilation, 50, 255, cv.THRESH_BINARY_INV)

    kernal_before_resize = cv.imread('fullcircle.png', 0)
    kernal = cv.resize(kernal_before_resize, (10,10))
    gray_image = cv.dilate(mask, kernal, iterations=2)

    # convert the dilation of original image to grayscale
    gray_image = cv.cvtColor(gray_image, cv.COLOR_BGR2GRAY)
    cv.imshow("Image", gray_image)
    cv.waitKey(0)

    # convert the grayscale dilation of the original image to binary image
    ret,thresh = cv.threshold(gray_image,127,255,0)
    
    #find contours from dilation of the original image

    #******************************************************************************************#
    #important!!!! in windows::
    contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    #important!!!! in raspberry::
    #im2, contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE) להחזיררררררררררררררררררררררררררררררררררררר
    #******************************************************************************************#

    cv.drawContours(output, contours, -1, (255,0,0), 6)
    path_windows = os.getcwd()+"\\Users\\"+num_id+"\\"
    path_linux = os.getcwd()+"/Users/"+num_id+"/"
    ###############################################################cv.imwrite(os.path.join(path_linux , string+".jpg"), output) להחזירררררררררררררר
    cv.imwrite(os.path.join(path_windows , string+".jpg"), output)

    cv.drawContours(output, contours, -1, (255,0,0), 25)
    #cv.imshow("Image", output)
    #cv.imshow("Image", gray_image)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    
    path_windows = os.getcwd()+"\\Users\\"+num_id+"\\"
    path_linux = os.getcwd()+"/Users/"+num_id+"/"
    ###############################################################cv.imwrite(os.path.join(path_linux , string+".jpg"), output) להחזירררררררררררררר
    cv.imwrite(os.path.join(path_windows , string+'_to_statistics' +".jpg"), output)

    bullets_number = len(contours)
    return bullets_number"""