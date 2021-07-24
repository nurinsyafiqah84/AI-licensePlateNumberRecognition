# AI-# Artificial-Intelligence
# LICENSE CAR PLATE RECOGNITION SYSTEM

## A. PROJECT SUMMARY



**Project Title:** License Car Plate Recognition System

![Pink Tone Restaurant Facebook Cover](https://user-images.githubusercontent.com/80866677/123492961-9aa0fe00-d64d-11eb-8ff7-b6e1df1c6c6e.png)


**Team Members:** 
- Nurin Syafiqah binti Mohd Saofi (B031910122)
- Nur Fatin binti Yazid (B031910017)
- Nor Afieqa binti Mahdi (B031910141)
- NurSyafiqah Adilla binti Mohd Syafiq @ Jackson (B031910324)


**Objectives:**
- To develop an artificial intelligence system that are able to detect Malaysia car number plate
- To develop a system that are able to recognize the character of the car number plate
- To develop an application programming interface (API) for the future ease of use as the integration module
- To use image processing to identify vehicles violating traffic by their plate numbers.


##  B. ABSTRACT 



![System Cover](https://user-images.githubusercontent.com/80866677/122080137-9b0cee00-ce30-11eb-9f67-970be4573f44.png)

[Figure 1] shows the AI output of detecting license car plate number.

Our goal is to train a custom deep learning model to detect car plate number in pictures and from that detection, we can know where the car from.

Why we want to create license car plate recognition system?

Violation of traffic legislation has been acknowledged as a major cause of road accidents in most areas of the world. Even if the rules and regulation against them are present, the number of violators is continuously growing. A system must therefore be established to help police agencies enforce these standards in order to improve road safety and reduce road accidents.


## C.  DATASET


Given the trained License Car Plate Recognition System, we’ll proceed to implement two more additional Python scripts used to:

- Detect license car plate number in images


This dataset consists of 7 images.



## D.   PROJECT STRUCTURE

The following directory is our structure of our project:
- ├── example
- │   ├── T2.jpg
- │   ├── T9.jpg
- │   ├── T10.jpg
- │   ├── T12.jpg
- │   ├── T14.jpg
- │   ├── T19.jpg
- │   └── T21.jpg
- |
- ├── DP Pict.jpg
- ├── Scanned
- ├── PlateRecognation.py
- ├── PlateRecognationGui.py
- 2 directories, 10 files


The dataset/ directory contains the picture of we will use for this project

Three image examples/ are provided so that you can test the static image license car plate detector.

We’ll be reviewing Two Python scripts in this tutorial:

- PlateRecognation.py: Performs plate car recognation in static image. It will display 5 pictures of step detection plate number
- PlateRecognationGui.py: Using GUI, this will detect license plate number by picture choosen.

In the next two sections, we will show how we use our license car plate detector.



## E   IMPLEMENTION LICENSE CAR PLATE NUMBER

The technique that we use to run the system is:

### **1. Pytesseract**
- Pytesseract or known as Python-tesseract is a tool to read and recognize the text in pictures and licence plates. It change text in picture into string.

![image](https://user-images.githubusercontent.com/80866677/123432571-1e7eca00-d5fd-11eb-9b29-a491016e97c6.png)

[Figure 2] shows the snap code for pytesseract command


### **2. Bilateral Filter**
- known as Gaussian Blur, a non-linear, edge-preserving, and noise-reducing smoothing filter for images. It replaces the intensity of each pixel with a weighted average of intensity values from nearby pixels. This weight can be based on a Gaussian distribution                            

![image](https://user-images.githubusercontent.com/80866677/123436784-93540300-d601-11eb-8baf-64f43bbf85d1.png)

 [Figure 3] shows the Original Picture we use:     

![image](https://user-images.githubusercontent.com/80866677/123436829-a070f200-d601-11eb-90d7-e7febf14837f.png)

[Figure 4] shows the picture after Bilateral filter process


### **3. Canny Edged Detection**
- a multi-stage edge detector operator that employs a vast spectrum of images to detect edges.

![image](https://user-images.githubusercontent.com/80866677/123434905-92ba6d00-d5ff-11eb-84c3-251e9cac3fa7.png)

[Figure 5] shows the snap code for Canny Edged Detection

![image](https://user-images.githubusercontent.com/80866677/123502381-7dd0ee80-d67e-11eb-9966-4620a935c883.png)

[Figure 6] shows the output of snap code in Figure 5



### **4. imageTK**
- a module contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images.

![image](https://user-images.githubusercontent.com/80866677/123435607-50ddf680-d600-11eb-8d63-1a0b527f7853.png)

[Figure 7] shows the snap code of using imageTK command


## F.  RESULT 

### Recognising the license car plate in using static image.


![image](https://user-images.githubusercontent.com/80866677/123509506-81796b00-d6a8-11eb-83e5-020964f51f7f.png)

- **[Figure 8] shows the Original image**

![image](https://user-images.githubusercontent.com/80866677/123509514-89d1a600-d6a8-11eb-8f24-9aac84449749.png)

- **[Figure 9] shows the 1st process**


![image](https://user-images.githubusercontent.com/80866677/123509469-50993600-d6a8-11eb-8bab-3f1a8f3a612d.png)

- **[Figure 10] shows the 2nd process**


![image](https://user-images.githubusercontent.com/80866677/123509526-97872b80-d6a8-11eb-8db3-cf975bb54cdd.png)

- **[Figure 11] shows the 3rd process**


![image](https://user-images.githubusercontent.com/80866677/123509573-d5844f80-d6a8-11eb-880e-9c8e6c6b07ab.png)

- **[Figure 12] shows the 4th process**


![image](https://user-images.githubusercontent.com/80866677/123509577-dddc8a80-d6a8-11eb-9d77-1cbbf550ffdd.png)

- **[Figure 13] shows the 5th process**


![image](https://user-images.githubusercontent.com/80866677/123509587-ea60e300-d6a8-11eb-95d5-5d5bad58dc37.png)

- **[Figure 14] shows the Result**


### Recognising the license car plate using GUI


![image](https://user-images.githubusercontent.com/80866677/123509601-fe0c4980-d6a8-11eb-8d64-2121adbed1df.png)

- **[Figure 15] shows the Before choose the image**


![image](https://user-images.githubusercontent.com/80866677/123510006-91467e80-d6ab-11eb-9704-37e86dd2b8e8.png)

- **[Figure 16] shows the After choose the image**


## G.   PROJECT PRESENTATION (VIDEO)

In this project, you learned how to create a license car plate recogniser using Static Image and GUI.

- **Video**

[![front slide](https://user-images.githubusercontent.com/80866677/123509346-7a9e2880-d6a7-11eb-8324-05d27c59b2a8.PNG))](https://www.youtube.com/watch?v=L_80wnOgU1w "front slide")

