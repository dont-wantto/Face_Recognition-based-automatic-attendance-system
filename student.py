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



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        #===========variables=============================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_passkey = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()





        
        # Load the background image
        bg_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\bg.jpg")
        bg_img = bg_img.resize((1530, 790), Image.LANCZOS)
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
        logo_lbl.place(x=0, y=0)  # Position the logo over the title label

        # Load the logoside image and resize it
        logoside_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\logoside.jpg")
        logoside_img = logoside_img.resize((1440, 100), Image.LANCZOS)
        self.logoside_photoimg = ImageTk.PhotoImage(logoside_img)
        
        # Create a Label to display the logoside
        logoside_lbl = Label(self.root, image=self.logoside_photoimg, bg="white")
        logoside_lbl.place(x=100, y=0)  # Position the logo over the title label

        # Create a Label for the title
        title_lbl = Label(self.root, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 18, "bold"), bg="#A52A2A", fg="#DEB887")
        title_lbl.place(x=0, y=100, width=1530, height=45)

        # Create the main frame
        self.main_frame = Frame(self.root, bg="white", bd=2)
        self.main_frame.place(x=20, y=150, width=1480, height=620)
        
        # Left label frame
        Left_frame = LabelFrame(self.main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 20, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        # Right label frame
        Right_frame = LabelFrame(self.main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 20, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)
        
        # Current course frame
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current course information", font=("times new roman", 13, "bold"))
        current_course_frame.place(x=5, y=10, width=720, height=150)

        # Department label and combobox
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 13, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department", "CSE", "IT", "Civil", "Mechanical", "PHARMACY", "QURAN AND HADITH", "CCE", "QURANIC SCIENCE", "ELL", "BBA", "LAW", "ETE")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course label and combobox
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times new roman", 13, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year label and combobox
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman", 13, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester label and combobox
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)
        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times new roman", 13, "bold"), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6", "Semester-7", "Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # CLASS STUDENT INFORMATION frame
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="CLASS STUDENT INFORMATION", font=("times new roman", 13, "bold"))
        class_student_frame.place(x=5, y=150, width=720, height=300)

        # Student ID label and entry
        studentId_label = Label(class_student_frame, text="Student ID:", font=("times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)
        studentID_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id, width=20, font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # Class Division label and entry
        class_div_label = Label(class_student_frame, text="Class Division:", font=("times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
       
        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=("times new roman", 13, "bold"), state="readonly", width=18)
        div_combo["values"] = ("A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=10, sticky=W)
        
                # Roll No label and entry
        passkey_label = Label(
            class_student_frame,
            text="PASSKEY:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        passkey_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        passkey_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_passkey,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        passkey_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender label and entry
        gender_label = Label(
            class_student_frame,
            text="Gender:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(
            class_student_frame,
            textvariable=self.var_gender,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=18,
        )
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB label and entry
        dob_label = Label(
            class_student_frame,
            text="DOB:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        dob_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_dob,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email label and entry
        email_label = Label(
            class_student_frame,
            text="Email:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        email_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_email,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone No label and entry
        phone_label = Label(
            class_student_frame,
            text="Phone No:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        phone_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_phone,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address label and entry
        address_label = Label(
            class_student_frame,
            text="Address:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        address_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_address,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name label and entry
        teacher_label = Label(
            class_student_frame,
            text="Teacher Name:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        teacher_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_teacher,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)
        # student name
        studentName_label = Label(
            class_student_frame,
            text="Student Name:",
            font=("times new roman", 13, "bold"),
        )
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        studentName_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_std_name,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        # Radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            class_student_frame,
            variable=self.var_radio1,
            text="Take Photo Sample",
            value="Yes",
        )
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(
            class_student_frame,
            variable=self.var_radio1,
            text="No Photo Sample",
            value="No",
        )
        radiobtn2.grid(row=6, column=1)

        # Buttons frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=205 , width=715, height=70)

        # Save button with command to add data
        save_btn = Button(
            btn_frame,
            text="Save",
            command=self.add_data,
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        save_btn.grid(row=0, column=0)

        # Update button
        update_btn = Button(
            btn_frame,
            text="Update",
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
            command=self.update_data 
        )
        update_btn.grid(row=0, column=1)

        # Delete button
        delete_btn = Button(
            btn_frame,
            text="Delete",command=self.delete_data,
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        delete_btn.grid(row=0, column=2)

        # Reset button
        reset_btn = Button(
            btn_frame,
            text="Reset",command=self.reset_data,
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        reset_btn.grid(row=0, column=3)

        # Button frame
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=715, height=35)

        # Take Photo Sample button
        take_photo_btn = Button(
            btn_frame1,command=self.generate_dataset,
            text="Take Photo Sample",
            width=35,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        take_photo_btn.grid(row=0, column=0)

        # Update Photo Sample button
        update_photo_btn = Button(
            btn_frame1,
            text="Update Photo Sample",
            width=35,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        update_photo_btn.grid(row=0, column=1)

        # Right label frame
        Right_frame = LabelFrame(
            self.main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 12, "bold"),
        )
        Right_frame.place(x=750, y=10, width=720, height=580)

        # =======Search System===========
        Search_frame = LabelFrame(
            Right_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Search System",
            font=("times new roman", 12, "bold"),
        )
        Search_frame.place(x=5, y=10, width=700, height=70)
        search_label = Label(
            Search_frame,
            text="Search By:",
            font=("times new roman", 15, "bold"),
            bg="red",
        )
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(
            Search_frame,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=12,
        )
        search_combo["values"] = ("Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(
            Search_frame, width=15, font=("times new roman", 13, "bold")
        )
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(
            Search_frame,
            text="Search",
            width=12,
            font=("times new roman", 12, "bold"),
            bg="blue",
        )
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(
            Search_frame,
            text="Show All",
            width=12,
            font=("times new roman", 12, "bold"),
            bg="blue",
        )
        showAll_btn.grid(row=0, column=4, padx=4)
        # ===============table frame================
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(
            table_frame,
            column=(
                "dep",
                "course",
                "year",
                "sem",
                "id",
                "name",
                "div",
                "passkey",
                "gender",
                "dob",
                "email",
                "phone",
                "address",
                "teacher",
                "photo",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("passkey", text="Passkey")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("passkey", width=100)
        self.student_table.column("gender", width=100)

        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # Function to add data
    def add_data(self):
           
        
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="nazrana2028@",
                    database="face_recognizer",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_passkey.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student added successfully", parent=self.root
                )
                self.show_data()  # Call a method to refresh or display the updated data
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Error due to: {str(e)}", parent=self.root
                )
     

    # Function to show data in the treeview
    def show_data(self):
        # Add code here to fetch data from the database and display it in the treeview
        pass

    # =======fetch data==============================
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="nazrana2028@",
            database="face_recognizer",
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
        conn.commit()
        conn.close()

    # ============get cursor=========
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_passkey.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

        # =========update function============
    def update_data(self):
     print("Update data function called")  # Debugging message
     if (
        self.var_dep.get() == "Select Department"
        or self.var_std_name.get() == ""
        or self.var_std_id.get() == ""
     ):
        messagebox.showerror("Error", "All Fields are required", parent=self.root)
     else:
        try:
            # Asking for confirmation
            update_confirmation = messagebox.askyesno(
                "Update", "Do you want to update this student details", parent=self.root
            )
            print("Confirmation:", update_confirmation)  # Debugging message
            if update_confirmation:
                print("Updating data...")  # Debugging message
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="nazrana2028@",
                    database="face_recognizer",
                )
                my_cursor = conn.cursor()
                query = "update student set Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Passkey=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, Photosample=%s where Student_id=%s"
                values = (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_passkey.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get(),
                )
                print("Query:", query % values)  # Debugging message
                my_cursor.execute(query, values)
                messagebox.showinfo(
                    "Success",
                    "Student details successfully updated",
                    parent=self.root,
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                print("Data updated successfully")  # Debugging message
            else:
                print("Update cancelled")  # Debugging message
                return
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due To:{str(es)}", parent=self.root
            )
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page", "Do you want to delete this student", parent=self.root
                )
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="nazrana2028@",
                        database="face_recognizer",
                    )
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                    conn.commit()
                    self.fetch_data()  
                    conn.close()
                    messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
     
               messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
      
      # reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_passkey.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")     
    
    def generate_dataset(self):
    # Define face_cropped function here
        def face_cropped(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            # scaling factor-1.3
            # Minimum neighbor =5
            for (x, y, w, h) in faces:
                face_cropped = img[y:y+h, x:x+w]
                return face_cropped

        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="nazrana2028@",
                    database="face_recognizer",
                )
                my_cursor = conn.cursor()
                
                # Fetch student data by student ID
                student_id = self.var_std_id.get()
                my_cursor.execute("SELECT * FROM student WHERE Student_id = %s", (student_id,))
                student_data = my_cursor.fetchone()
                
                if student_data:
                    # Update student information in the database
                    update_query = """
                        UPDATE student SET 
                        Department = %s, 
                        Course = %s, 
                        Year = %s, 
                        Semester = %s, 
                        Name = %s, 
                        Division = %s, 
                        Passkey = %s, 
                        Gender = %s, 
                        DOB = %s, 
                        Email = %s, 
                        Phone = %s, 
                        Address = %s, 
                        Teacher = %s, 
                        Photosample = %s 
                        WHERE Student_id = %s
                    """
                    update_data = (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_passkey.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        student_id,
                    )
                    my_cursor.execute(update_query, update_data)
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    
                    # Capture student's images for dataset
                    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                    cap = cv2.VideoCapture(0)
                    user_id = student_id  # Use student ID as user ID
                    img_id = self.get_last_img_id(user_id) + 0  # Get the last image ID for this user and increment
                    img_count = 0  # Initialize image count for this user
                    while True:
                        ret, my_frame = cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id += 1
                            img_count += 1
                            
                            face = cv2.resize(face_cropped(my_frame), (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            # Use the desired naming convention for saving images
                            file_name_path = f"data/user.{user_id}.{img_id}.jpg"
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255), 2)
                            cv2.imshow("Cropped Face", face)
                            
                            if img_count == 100:
                                break  # Break after capturing 100 photos
                                
                        if cv2.waitKey(1) == 13 or img_count == 100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Generating data sets completed!!!!")
                else:
                    messagebox.showerror("Error", "Student not found in the database", parent=self.root)
                    
            except Exception as e:
                messagebox.showerror("Error", f"Database error: {str(e)}", parent=self.root)

    def get_last_img_id(self, user_id):
            # Function to get the last image ID for a given user ID
            last_img_id = 0
            # You need to implement this function to query the database and retrieve the last image ID
            # Here is just a placeholder
            return last_img_id


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()


       