from tkinter import *
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
import os



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        try:
            # Load the background image
            bg_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\bg.jpg")
            bg_img = bg_img.resize((screen_width, screen_height), Image.LANCZOS)
            self.bg_photoimg = ImageTk.PhotoImage(bg_img)
            
            # Create a Label to display the background image
            bg_lbl = Label(self.root, image=self.bg_photoimg)
            bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)  # Position the Label to cover the entire window

            # Load the logo image and resize it
            logo_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\logo.png")
            logo_img = logo_img.resize((100, 100), Image.LANCZOS)
            self.logo_photoimg = ImageTk.PhotoImage(logo_img)
            
            # Create a Label to display the logo
            logo_lbl = Label(self.root, image=self.logo_photoimg, bg="white")
            logo_lbl.place(x=0, y=45)  # Position the logo over the title label

            # Create a Label for the title
            title_lbl = Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 18, "bold"), bg="#8FBC8F", fg="navy")
            title_lbl.place(x=0, y=0, width=screen_width, height=45)

            # Load the student image
            student_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\student1.jpg")
            student_img = student_img.resize((220, 220), Image.LANCZOS)
            self.student_photoimg = ImageTk.PhotoImage(student_img)

            # Create and place the student button
            b1 = Button(self.root, image=self.student_photoimg,command=self.student_details, cursor='hand2')
            b1.place(x=200, y=100, width=220, height=220)

            b1_1 = Button(self.root, text="STUDENT DETAILS",command=self.student_details, cursor='hand2', font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b1_1.place(x=200, y=310, width=220, height=40)

            # Load the face scan image
            facescan_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\facescan.jpg")
            facescan_img = facescan_img.resize((220, 220), Image.LANCZOS)
            self.facescan_photoimg = ImageTk.PhotoImage(facescan_img)

            # Create and place the face scan button
            b2 = Button(self.root, image=self.facescan_photoimg, cursor='hand2',command=self.face_data)
            b2.place(x=500, y=100, width=220, height=220)

            b2_1 = Button(self.root, text="FACE SCAN", cursor='hand2',command=self.face_data ,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b2_1.place(x=500, y=310, width=220, height=40)

            # Load the attendance face image
            attendance_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\attendance.jpg")
            attendance_img = attendance_img.resize((220, 220), Image.LANCZOS)
            self.attendance_photoimg = ImageTk.PhotoImage(attendance_img)

            # Create and place the attendance face button
            b3 = Button(self.root, image=self.attendance_photoimg, cursor='hand2')
            b3.place(x=800, y=100, width=220, height=220)

            b3_1 = Button(self.root, text="ATTENDANCE", cursor='hand2', font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b3_1.place(x=800, y=310, width=220, height=40)
              
              
            # Load the help image
            help_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\help.jpg")
            help_img = help_img.resize((220, 220), Image.LANCZOS)
            self.help_photoimg = ImageTk.PhotoImage(help_img)

            # Create and place the help button
            b4 = Button(self.root, image=self.help_photoimg, cursor='hand2')
            b4.place(x=1100, y=100, width=220, height=220)

            b4_1 = Button(self.root, text="HELP", cursor='hand2', font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b4_1.place(x=1100, y=310, width=220, height=40)


             ########################## Load the train image
            train_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\train.jpg")
            train_img = train_img.resize((220, 220), Image.LANCZOS)
            self.train_photoimg = ImageTk.PhotoImage(train_img)

            # Create and place the help button
            b5 = Button(self.root, image=self.train_photoimg, cursor='hand2',command=self.train_data)
            b5.place(x=200, y=380, width=220, height=220)

            b5_1 = Button(self.root, text="TRAIN DATA", cursor='hand2',command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b5_1.place(x=200, y=560, width=220, height=40)

              ################  # Load the photos image
            photos_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\photos.jpg")
            photos_img = photos_img.resize((220, 220), Image.LANCZOS)
            self.photos_photoimg = ImageTk.PhotoImage(photos_img)

            # Create and place the photos button
            b6 = Button(self.root, image=self.photos_photoimg, cursor='hand2',command=self.open_img)
            b6.place(x=500, y=380, width=220, height=220)

            b6_1 = Button(self.root, text="PHOTOS", cursor='hand2',command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b6_1.place(x=500, y=560, width=220, height=40)
            
              ################  # Load the developer image
            dev_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\developer.jpg")
            dev_img = dev_img.resize((220, 220), Image.LANCZOS)
            self.dev_photoimg = ImageTk.PhotoImage(dev_img)

            # Create and place the developer button
            b7 = Button(self.root, image=self.dev_photoimg, cursor='hand2')
            b7.place(x=800, y=380, width=220, height=220)

            b7_1 = Button(self.root, text="DEVELOPER", cursor='hand2', font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b7_1.place(x=800, y=560, width=220, height=40)

             ################  # Load the exit image
            exit_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\exit.jpg")
            exit_img = exit_img.resize((220, 220), Image.LANCZOS)
            self.exit_photoimg = ImageTk.PhotoImage(exit_img)

            # Create and place the help button
            b8 = Button(self.root, image=self.exit_photoimg, cursor='hand2')
            b8.place(x=1100, y=380, width=220, height=220)

            b8_1 = Button(self.root, text="EXIT", cursor='hand2', font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b8_1.place(x=1100, y=560, width=220, height=40)
        except Exception as e:
            print("Error:", e)    
    def open_img(self):
        os.startfile(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\data")        

    #=========function buttons===================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)     
    def train_data (self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)  
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)    
      
           
           
           
           
           
           
           
            







     

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()