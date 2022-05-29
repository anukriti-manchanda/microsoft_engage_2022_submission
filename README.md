# **Drowsy Detect**
## _About The Project_
---
 Drowsiness Detection System is a web based project designed to detect if a person is drowsy or not. The more specific aim of the project is to help reduce the accidents that take place due to the little or no consciousness of the driver while driving. The project detects if the driver is drowsy or not using the face landmark detection and if yes, will make a beep noise to help the driver stay awake at all times and will also fetch the location of the car and time store it in the database.

 ## _Essentials about the project_
 ---
 - ### Django-admin(Database) Login Credentials
    - ### Username: Admin
    - ### Password: Anukriti@22
 
 ## _Built With_
 ---
 - Python
 - Django
 - HTML
 - CSS
 ## _Usage_
 ---
 This project is used to store data(car number and phone number) of the user and the driver's location if the driver gets drowsy.
 <br />
 Thus used to prevent accidents that could happen due to subconscious state of the driver. 

 ## _Roadmap/ Key Features_
 ---
 - Asks for login details and stores login details in database
 - Alarm (beep sound) is played if the driver becomes drowsy as an alert or warning
 - Fetches location details(latitude,longitude,city,state,country) and time of the user from his/her ip address and stores in the database.
 <br />
 It is also displayed on the dashboard on the webpage

 ## _Version of apps/modules being used in the project_
 ---
 - Python-3.9.12
 - Django-4.0.4
 - Opencv-4.5.5
 - Cmake-3.23.0
 - Dlib-19.24.0

 ## _Getting Started_
 ---
 ### Setting Up The Project

 ---

 ### Prerequisites
 ---
 - Python should be installed
 <br />
 - VS Code should be installed
 </br>
 - 'shape_predictor_68_face_landmark.dat' should be installed and extracted

 ### Steps to start working on the project
---
 - Create a folder on the desktop-outer folder(Folder Name-Microsoft, Location-Desktop)
 
 - Create a virtual environment
 
 python -m venv <'give path of your folder'> <'name of virtual environment'>

 ```
 python -m venv C:\Users\Hp\Desktop\Microsoft drowsiness_detection_env
 ```
 - Open vs code and then View->Command Palette->Python:Select Interpreter and then select python.exe from Scripts folder in the virtual environment folder

- Create a django project in the microsoft folder
```
django-admin startproject drowsiness_detection
```
 - Open the drowsiness_detection folder in vs code. The folder should contain a drowsiness_detection folder and a manage.py file. 

 - Install Django in this drowsiness_detection folder
 ```
 pip install django
 ```

 - Get your shape predictor files in this folder.

 - Activating the virtual environment

 ```
 &c:/Users/Hp/Desktop/Microsoft/drowsiness_detection_env/Scripts/Activate.ps1
 ```
 - You will see the name of your virtual environment written in green which means you are good to go and you can start working on your project.

 - Further create django app using

```
 python manage.py startapp home
 ```
 - Also create the templates folder and the static folder for your templates and static files and you are good to go.

### Packages to be installed
---
- Opencv-python
```
pip install opencv-python
```
- Cmake(Prerequisite for dlib)
```
pip install cmake
```
- Dlib
```
pip install dlib
```
- Imutils
```
pip install imutils
```
- Winsound
```
pip install winsound
```
- Geocoder
```
pip install geocoder
```
- Thread6(threading)
```
pip install thread6
```
## _Contact_
---
- Name: Anukriti Manchanda
- Email: manchandaanukriti5@gmail.com
- LinkedIn: www.linkedin.com/in/anukriti-manchanda-b58863220
- Instagram: @anukritimanchanda



