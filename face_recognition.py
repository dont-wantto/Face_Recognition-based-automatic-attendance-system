from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import openpyxl 
import re
from datetime import datetime
import tkinter.simpledialog as simpledialog

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="#A52A2A", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        img_bottom = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\FACERECOG.jpg")
        img_bottom = img_bottom.resize((1538, 790), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=45, width=1538, height=790)
        
        # Button
        b1_1 = Button(f_lbl, text="RECOGNIZE ME", cursor="hand2", command=self.face_recog, font=("times new roman", 30, "bold"), bg="#A52A2A", fg="white")
        b1_1.place(x=520, y=600, width=500, height=60)
        
    # Face recognition method
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []
            
            # Establish database connection
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="nazrana2028@",
                database="face_recognizer"
            )
            my_cursor = conn.cursor()
            
            for (x, y, w, h) in features: 
                cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w]) 
                confidence = int((100 * (1 - predict / 300)))
                
               # Fetching data from the database
                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                if n is not None:
                    n = "+".join(str(e) for e in n)  # Joining elements of n if it's not None

                
                # Fetching data from the database
                my_cursor.execute("select Passkey from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                if r is not None:
                    r = "+".join(str(e) for e in r)  # Joining elements of r if it's not None

                my_cursor.execute("select Department from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                if d is not None:
                    d = "+".join(str(e) for e in d)  # Joining elements of d if it's not None
                

                
                if confidence > 77:
                    cv2.putText(img, f"Passkey: {r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3) 
                    cv2.putText(img, f"Name: {n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    
                coord = [x, y, w, y+h]  
            
            # Close database connection
            my_cursor.close()
            conn.close()
            
            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\clf.xml")
        video_cap = cv2.VideoCapture(0) 
        
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome TO face Recognition", img)
            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
