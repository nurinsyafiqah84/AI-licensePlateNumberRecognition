import tkinter as tk
from tkinter import *
import cv2
from PIL import ImageTk, Image
from tkinter import filedialog, Text
import imutils
import numpy as np
import pytesseract
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR\\tesseract.exe'
states = {"A": "Perak", "B": "Selangor", "C": "Pahang", "D": "Kelantan", "F": "Putrajaya", "J": "Johor", "K": "Kedah",
          "M": "Malacca", "N": "Negeri Sembilan", "P": "Penang", "R": "Perlis", "T": "Terengganu", "V": "Kuala Lumpur",
          "W": "Kuala Lumpur", "S": "Sabah", "L": "Labuan", "Q": "Sarawak", "Z": "Military", "U": "University"}

#frame gui
root = tk.Tk()
canvas = Canvas(root, width=1000, height=250)
canvas.pack()

#display pic in JPEG/JPG and PNG use ImageTk
photo = ImageTk.PhotoImage(Image.open("DP Pict.jpg"))
canvas.create_image(20, 20, anchor=NW, image=photo)
imgArr = []
photos = []
images = []


#to add command add button
def addApp():
    filename = filedialog.askopenfilename(initialdir="licensePlateNumberRecognition/Dataset", title="Select File",
                                          filetypes=(("exceutables", "*.jpg"), ("all files", "*.*")))
    #get the choosen image
    image2 = Image.open(filename)
    image = image2.resize((280, 182))
    photo = ImageTk.PhotoImage(image)
    photos.append(photo)
    newPhoto_label = Label(image=photo)
    newPhoto_label.place(x=350, y=17)



    #command process button to start process
    def processApp():
        # Read the image file
        file = open(filename)
        ispath = file.name
        img = cv2.imread(ispath, cv2.IMREAD_COLOR)
         # Resize the image file
        img = cv2.resize(img, (600, 400))

        # Convert to Grayscale Image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Removing Noise from the detected image, before sending to Tesseract
        gray = cv2.bilateralFilter(gray, 13, 15, 15)

        # Canny Edge Detection
        edged = cv2.Canny(gray, 30, 200)
        # Find contours based on Edges
        contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
        screenCnt = None

        for c in contours:

            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.018 * peri, True)
            # see whether it is a Rectangle or not
            if len(approx) == 4: #if yes
                screenCnt = approx
                break

        if screenCnt is None:
            detected = 0
            print("No contour detected")
        else:
            detected = 1

        if detected == 1:
            cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)

        mask = np.zeros(gray.shape, np.uint8)
        new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
        new_image = cv2.bitwise_and(img, img, mask=mask)

        (x, y) = np.where(mask == 255)
        (topx, topy) = (np.min(x), np.min(y))
        (bottomx, bottomy) = (np.max(x), np.max(y))
        Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]

        text = pytesseract.image_to_string(Cropped, config='--psm 11')
        stat = text[0:1]
        try:
            print("This car from : ", states[stat])
        except:
            print("This car cannot detect from where")
        print("\nprogramming_fever's License Plate Recognition\n")
        print("Detected license plate Number is:", text)
        img = cv2.resize(img, (500, 300))
        Cropped = cv2.resize(Cropped, (400, 200))

        #to print out the result on gui
        detectedNo = tk.Label(root, text=text, bg="black", fg="white")
        stateFrom = tk.Label(root, text="FROM = " + states[stat], bg="black", fg="white")
        detectedNo.place(x=700, y=210)
        stateFrom.place(x=800, y=210)


        #print photo plate
        # You may need to convert the color.
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        im_pil = Image.fromarray(img)
        #save into folder
        im_pil.save("Scanned/Print.jpg")
        print(im_pil)
        image3 = Image.open("Scanned\Print.jpg")
        image4 = image3.resize((280, 182))
        photo4 = ImageTk.PhotoImage(image4)
        images.append(photo4)
        newPhoto_label2 = tk.Label(image=photo4)
        newPhoto_label2.place(x=650, y=17)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    # create button process
    process = tk.Button(root, text="Detect License Plate", fg="white", bg="blue", command=processApp)
    process.place(x=350, y=210)

#create button Open File
openFile = tk.Button(root, text="Open File", fg="white", bg="blue", command=addApp)
openFile.place(x=125, y=210)

root.mainloop()
