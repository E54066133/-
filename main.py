import cv2
import numpy as np
from numpy import empty


if __name__ == '__main__':
    img = cv2.imread('logo.png')
    img = cv2.resize(img, (50, 50), interpolation=cv2.INTER_NEAREST)
    
    ## TODO
    ## convert your color pixels to characters here
    '''
    Rule : 紅 -> “R”
           綠 -> “G”
           藍 -> “B”
           黑 -> “@”
           白 -> " " (空白)
    '''
    ## cv2.imread 會將圖片存成一個 NumPy 的陣列
    ## 此範例為 [50,50,3]
    
    outtxt = [['f']*50 for i in range(50)]
    
    for i in range(0,50):
        for j in range(0,50):
            if img[i][j][0] ==255 and img[i][j][1] ==0 and  img[i][j][2] ==0  :#(待填數字)
                outtxt[i][j] = "B"
            if img[i][j][0] ==0 and img[i][j][1] ==0 and  img[i][j][2] ==255  :#(待填數字)
                outtxt[i][j] = "R"
            if img[i][j][0] ==0 and img[i][j][1] ==255 and  img[i][j][2] ==0  :#(待填數字)
                outtxt[i][j] = "G"
            if img[i][j][0] ==255 and img[i][j][1] ==255 and  img[i][j][2] ==255:#(待填數字)
                outtxt[i][j] = " "
            if img[i][j][0] ==0 and img[i][j][1] ==0 and  img[i][j][2] ==0  :#(待填數字)
                outtxt[i][j] = "@"
            print(outtxt[i][j],end='')
            if j ==  49:
                print("\t")

    
    
    '''
    (測試數值)
    print(img.shape)
    print(img[0][0][0])
    print(img[24,9,0])
    print(img[24,9,1])
    print(img[24,9,2])
    print(outtxt)
    print(img[:,:,0])
    print(img[:,:,1])
    print(img[:,:,2])
    '''
    
    #方法二 讀成灰階 -> 資料陣列變成[50,50]
    '''
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(img_gray)

    txt = []
    txt = img_gray
    
    
    for i in range(0,50):
        for j in range(0,50):
            if txt[i][j] ==  10  :#(待填數字)
                outtxt[i][j] = "R"
            if txt[i][j] ==  20  :#(待填數字)
                outtxt[i][j] = "G"
            if txt[i][j] ==  30  :#(待填數字)
                outtxt[i][j] = "B"
            if txt[i][j] ==  255 :#(待填數字)
                #outtxt[i][j] = " "
            if txt[i][j] ==  0   :#(待填數字)
                outtxt[i][j] = " "
            print(txt[i][j],end='')
            if j ==  49:
                print("\t")     
    
    '''
