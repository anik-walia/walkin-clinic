import sqlite3
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib

user_entry = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
system_convert = ('T', 'I', 'M', 'E', 'O', 'D', 'A', 'N', 'S', 'F', 'R', 'B', 'C', 'G', 'H', 'J', 'K', 'L', 'P', 'Q',
                  'U', 'V', 'W', 'X', 'Y', 'Z', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0')


class Table:
   def __init__(self, root):
      # code for creating table
      for i in range(total_rows):
         for j in range(total_columns):
            self.e = Entry(root, width=20, fg='blue',
                           font=('Arial', 16, 'bold'))

            self.e.grid(row=i, column=j)
            self.e.insert(END, lst[i][j])

def encrypt_psw(psw):
   encrypted_psw = ''
   psw = psw.upper()
   for character in psw:
      try:
         index = user_entry.index(character)
      except:
         return "not_found"
      converted_character = system_convert[index]
      encrypted_psw = encrypted_psw + converted_character
   return encrypted_psw


conn = sqlite3.connect('C:/Users/Aniket/Desktop/DB Browser for SQLite/walkin_clinic.db')


print("****************************************************************************")
print("*                                                                          *")
print("*                   Welcome To Walk in Clinic System                       *")
print("*                                                                          *")
print("****************************************************************************")


while True:
   print("-----------------------------------------")
   print(
      "|Enter 1 for Admin mode			|\n|Enter 2 for Staff mode			|\n|Enter 3 for Doctor mode        |\n|Enter 4 to quit			|")
   print("-----------------------------------------")
   Admin_user_mode = input("Enter your mode : ")
   if Admin_user_mode == "1":  # Admin Mode
      print(
         "*****************************************\n|         Welcome to admin mode         |\n*****************************************")
      Password = input("Please enter your password : ")

      if Password == "1234":
         while True:
            print("====================================")
            print("(a). Add new patient's record")
            print("(b). Add new doctor's record")
            print("(c). Book a new appointment")
            print("(d). Audit system records")
            print("(e). Quit")
            print("====================================")
            EnterLetter = input("Please select a Letter from the Above Box menu: ")
            if EnterLetter == 'a':
               print("Please enter patient's details in order to add records")
               username = input("username: ")
               psw = input("password: ")
               user_type = 4
               first_name = input("first_name: ")
               last_name = input("last_name: ")
               encrypted_psw = encrypt_psw(psw)
               if encrypted_psw == "not_found":
                  print("Please enter a password using either alphabets or numerals or a combination of both.")
               else:
                  conn.execute("INSERT INTO User (username,user_type,password,first_name,last_name) VALUES (?,?,?,?,?)",
                               (username, user_type, encrypted_psw, first_name, last_name))
                  conn.commit()
                  print("Patient added successfully")
            elif EnterLetter == 'b':
               print("Please enter doctor's details in order to add records")
               username = input("username: ")
               password = input("password: ")
               user_type = 3
               first_name = input("first_name: ")
               last_name = input("last_name: ")
               encrypted_psw = encrypt_psw(password)
               if encrypted_psw == "not_found":
                  print("Please enter a password using either alphabets or numerals or a combination of both.")
               else:
                  conn.execute("INSERT INTO User (username,user_type,password,first_name,last_name) VALUES (?,?,?,?,?)",
                               (username, user_type, encrypted_psw,  first_name, last_name))
                  conn.commit()
                  print("Doctor added successfully")
            elif EnterLetter == 'c':
               print("Please enter details in order to add a new appointment")
               doctor_id = input("Enter doctor id: ")
               patient_id = input("Enter patient id: ")
               date = input("Enter date: ")
               conn.execute("INSERT INTO Apointment (doctor_id,patient_id,date) VALUES (?,?,?)",
                            (doctor_id, patient_id, date))
               conn.commit()
               print("Appointment added successfully")
            elif EnterLetter == 'd':
               print(
                  "|Enter 1 for Doctor details		|\n|Enter 2 for Patient details         |")
               report_type = input("Enter your audit type : ")
               if report_type == '1':
                  doc_data = conn.execute("Select * from User where user_type='3'").fetchall()
                  s_no = 1
                  doc_list = []
                  for item in doc_data:
                     first_name = item[4]
                     last_name = item[5]
                     doc_full_name = first_name + ' ' + last_name
                     doc_list.append([s_no, doc_full_name])
                     s_no = s_no + 1
                  doc_list.append(['Total Doctors', len(doc_list)])
                  lst = doc_list
                  total_rows = len(lst)
                  total_columns = len(lst[0])
                  root = Tk()
                  t = Table(root)
                  root.mainloop()
               elif report_type == '2':
                  p_data = conn.execute("Select * from User where user_type='4'").fetchall()
                  s_no = 1
                  p_list = []
                  for item in p_data:
                     first_name = item[4]
                     last_name = item[5]
                     p_full_name = first_name + ' ' + last_name
                     p_list.append([s_no, p_full_name])
                     s_no = s_no + 1
                  p_list.append(['Total Patients', len(p_list)])
                  lst = p_list
                  total_rows = len(lst)
                  total_columns = len(lst[0])
                  root = Tk()
                  t = Table(root)
                  root.mainloop()
            elif EnterLetter == 'e':
               break
            else:
               print("please select one among the provided options")
            print("Operation done successfully")
      elif Password != "1234":
         print("Password incorrect, please try again : ")
         continue


   elif Admin_user_mode == "3":  # Doctor Mode
      print(
         "*****************************************\n|         Welcome to doctor mode         |\n*****************************************")
      Password = input("Please enter your password : ")
      if Password == "1234":
         while True:
            print("====================================")
            print("(a). Add a prescription")
            print("(b). Quit")
            print("====================================")
            EnterLetter = input("Please select a Letter from the Above Box menu: ")
            if EnterLetter == 'a':
               print("Please enter details in order to add prescription")
               doctor_id = input("Enter your id: ")
               patient_id = input("Enter patient id: ")
               date = input("Enter date: ")
               prescription = input("Enter prescription: ")
               appointment_id = conn.execute("Select * from Apointment where patient_id=? and doctor_id=? and date=?", (patient_id,doctor_id,date)).fetchone()[0]
               conn.execute("INSERT INTO Prescription (appointment_id,detail) VALUES (?,?)",
                            (appointment_id, prescription))
               conn.commit()
            elif EnterLetter == 'b':
               break
            else:
               print("please select one among the provided options")
               print("Prescription added successfully")
      elif Password != "1234":
         print("Password incorrect, please try again : ")
         continue

   elif Admin_user_mode == "2":  # staff Mode
      print(
         "*****************************************\n|         Welcome to staff mode         |\n*****************************************")
      Password = input("Please enter your password : ")
      if Password == "1234":
         while True:
            print("====================================")
            print("(a). Extract a report")
            print("(b). Quit")
            print("====================================")
            EnterLetter = input("Please select a Letter from the Above Box menu: ")
            if EnterLetter == 'a':
               print("|Enter 1 for Appointment Status Report		|\n|Enter 2 for Doctor-Appointments Report          |")
               report_type = input("Enter your report type : ")
               if report_type == '1':
                  appointment_ids = conn.execute("Select Id from Apointment").fetchall()
                  appointment_ids = [item for t in appointment_ids for item in t]
                  appointment_complete = 0
                  appointment_not_complete = 0
                  for id in appointment_ids:
                     try:
                        if conn.execute("Select Id from Prescription where appointment_id=?", (str(id))).fetchone() == None:
                           appointment_not_complete = appointment_not_complete + 1
                        else:
                           appointment_complete = appointment_complete + 1
                     except:
                        pass
                  total_appointments = appointment_complete + appointment_not_complete
                  plt.style.use('ggplot')
                  matplotlib.rcParams['figure.figsize'] = (6, 5)
                  a = ['incomplete', 'complete']
                  b = [appointment_not_complete, appointment_complete]
                  plt.bar(a, b)
                  plt.yticks(range(1, 11))
                  plt.show()
                  import csv
                  with open('appointment_status_report.csv', 'w', newline='') as file:
                     writer = csv.writer(file)
                     writer.writerow(["SN", "Total Appointments", "Completed Appointments", "Pending Appointments"])
                     writer.writerow([1, total_appointments, appointment_complete, appointment_not_complete])
                  print("Report generated successfully")
               if report_type == '2':
                  doctor_ids = conn.execute("Select Id from User where user_type='3'").fetchall()
                  doctor_ids = [item for t in doctor_ids for item in t]
                  doc_dict = {}
                  doc_list = []
                  p_count = []
                  for id in doctor_ids:
                     try:
                        total_patients = len(conn.execute("Select Id from Apointment where doctor_id=?", ([str(id)])).fetchall())
                        doctor_name = conn.execute("Select first_name from User where Id=?", ([str(id)])).fetchone()
                        doc_dict[str(id)+'_'+doctor_name[0]] = total_patients
                        doc_list.append(doctor_name[0])
                        p_count.append(total_patients)
                     except:
                        pass
                  print("exit loop")
                  plt.style.use('ggplot')
                  matplotlib.rcParams['figure.figsize'] = (6, 5)
                  plt.bar(doc_list, p_count)
                  plt.xlabel("Doctors")
                  plt.ylabel("Number of patients")
                  plt.yticks(range(1, 11))
                  plt.show()
                  import csv
                  with open('doctor_appointments.csv', 'w', newline='') as file:
                     writer = csv.writer(file)
                     writer.writerow(["Doctor", "Total Appointments"])
                     for key in doc_dict.keys():
                        file.write("%s,%s\n" % (key, doc_dict[key]))
                  print("Report generated successfully")
            elif EnterLetter == 'b':
               break
      elif Password != "1234":
         print("Password incorrect, please try again : ")
         continue


   elif Admin_user_mode == "4":
      conn.close()
      break














