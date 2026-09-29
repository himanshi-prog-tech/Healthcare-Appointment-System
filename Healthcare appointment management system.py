# Doctor appointment management system

name= input("Enter your name: ")
age= int(input("Enter your age: "))
Mobile_number= int(input("Enter your mobile number: "))

print("Hi", name, ", Welcome to Cygnus Hospital.")

# Select the department you want to visit
department= input(
    "Enter the department you want to visit : (Clinical=1, diagnostic=2, administrative=3): ")


if department == "1":
    print("You have selected Clinical Department.")

    a= input("Enter the specific clinical department you want to visit: Cardiology=1,Neurology=2,Orthopedics=3,Paediatrics=4,Oncology (cancer)=5,Obstetrics & Gynaecology=6 :"
    )

    if a == "1":
        print("You have selected Cardiology Department.")
        selected_doctor= input("Enter the doctor you want to visit: (Dr.Satish=1, Dr. Ravi=2, Dr. Rakesh=3): ")
        if selected_doctor == "1":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Satish.")
            print("Qualifications: MBBS, MD (Cardiology)")
            print("Experience: 15 years in Cardiology")
            print("Dr. Satish is available from 10:00 AM to 2:00 PM.")
            print("Your appointment with Dr. Satish has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "2":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Ravi.")
            print("Qualifications: MBBS, MD (Cardiology)")
            print("Experience: 10 years in Cardiology")
            print("Dr. Ravi is available from 2:00 PM to 6:00 PM.")
            print("Your appointment with Dr. Ravi has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")
        elif selected_doctor == "3":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Rakesh.")
            print("Qualifications: MBBS, MD (Cardiology)")
            print("Experience: 8 years in Cardiology")
            print("Dr. Rakesh is available from 6:00 PM to 10:00 PM.")
            print("Your appointment with Dr. Rakesh has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

    elif a == "2":
        print("You have selected Neurology Department.")
        selected_doctor= input("Enter the doctor you want to visit: (Dr. Sara=1, Dr. Sakshi=2, Dr. Samay=3): ")
        if selected_doctor == "1":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Sara.")
            print("Qualifications: MBBS, MD (Neurology)")
            print("Experience: 12 years in Neurology")
            print("Dr. Sara is available from 10:00 AM to 2:00 PM.")
            print("Your appointment with Dr. Sara has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "2":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Sakshi.")
            print("Qualifications: MBBS, MD (Neurology)")
            print("Experience: 9 years in Neurology")
            print("Dr. Sakshi is available from 2:00 PM to 6:00 PM.")
            print("Your appointment with Dr. Sakshi has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")
        elif selected_doctor == "3":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Samay.")
            print("Qualifications: MBBS, MD (Neurology)")
            print("Experience: 6 years in Neurology")
            print("Dr. Samay is available from 6:00 PM to 10:00 PM.")
            print("Your appointment with Dr. Samay has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

    elif a == "3":
        print("You have selected Orthopedics Department.")
        selected_doctor= input("Enter the doctor you want to visit: (Dr. Ramesh=1, Dr. Kavita=2, Dr. Manoj=3): ")
        if selected_doctor == "1":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Ramesh.")
            print("Qualifications: MBBS, MS (Orthopedics)")
            print("Experience: 14 years in Orthopedics")
            print("Dr. Ramesh is available from 10:00 AM to 2:00 PM.")
            print("Your appointment with Dr. Ramesh has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "2":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Kavita.")
            print("Qualifications: MBBS, MS (Orthopedics)")
            print("Experience: 11 years in Orthopedics")
            print("Dr. Kavita is available from 2:00 PM to 6:00 PM.")
            print("Your appointment with Dr. Kavita has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "3":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Manoj.")
            print("Qualifications: MBBS, MS (Orthopedics)")
            print("Experience: 9 years in Orthopedics")
            print("Dr. Manoj is available from 6:00 PM to 10:00 PM.")
            print("Your appointment with Dr. Manoj has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

    elif a == "4":
        print("You have selected Paediatrics Department.")
        selected_doctor= input("Enter the doctor you want to visit: (Dr. Ananya=1,,Dr. Ritu=2, ,Dr. Karan=3): "
        )
        if selected_doctor == "1":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Ananya.")
            print("Qualifications: MBBS, MD (Paediatrics)")
            print("Experience: 13 years in Paediatrics")
            print("Dr. Ananya is available from 10:00 AM to 2:00 PM.")
            print("Your appointment with Dr. Ananya has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "2":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Ritu.")
            print("Qualifications: MBBS, MD (Paediatrics)")
            print("Experience: 10 years in Paediatrics")
            print("Dr. Ritu is available from 2:00 PM to 6:00 PM.")
            print("Your appointment with Dr. Ritu has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "3":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Karan.")
            print("Qualifications: MBBS, MD (Paediatrics)")
            print("Experience: 8 years in Paediatrics")
            print("Dr. Karan is available from 6:00 PM to 10:00 PM.")
            print("Your appointment with Dr. Karan has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

    elif a == "5":
        print("You have selected Oncology (Cancer) Department.")
        selected_doctor= input("Enter the doctor you want to visit: (Dr. Meera=1,Dr. Arjun=2, Dr. Nisha=3):" 
        )
        if selected_doctor == "1":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Meera.")
            print("Qualifications: MBBS, MD (Oncology)")
            print("Experience: 15 years in Oncology")
            print("Dr. Meera is available from 10:00 AM to 2:00 PM.")
            print("Your appointment with Dr. Meera has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "2":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Arjun.")
            print("Qualifications: MBBS, MD (Oncology)")
            print("Experience: 12 years in Oncology")
            print("Dr. Arjun is available from 2:00 PM to 6:00 PM.")
            print("Your appointment with Dr. Arjun has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "3":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Nisha.")
            print("Qualifications: MBBS, MD (Oncology)")
            print("Experience: 10 years in Oncology")
            print("Dr. Nisha is available from 6:00 PM to 10:00 PM.")
            print("Your appointment with Dr. Nisha has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

    elif a == "6":
        print("You have selected Obstetrics & Gynaecology Department.")
        selected_doctor= input("Enter the doctor you want to visit: (Dr. Priyanka=1, Dr. Suman=2,Dr. Rakesh=3): ")
        if selected_doctor == "1":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Priyanka.")
            print("Qualifications: MBBS, MD (Obstetrics & Gynaecology)")
            print("Experience: 14 years in Obstetrics & Gynaecology")
            print("Dr. Priyanka is available from 10:00 AM to 2:00 PM.")
            print("Your appointment with Dr. Priyanka has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "2":

            print()
            print('*******************')
            print()
            print("You have selected Dr. Suman.")
            print("Qualifications: MBBS, MD (Obstetrics & Gynaecology)")
            print("Experience: 11 years in Obstetrics & Gynaecology")
            print("Dr. Suman is available from 2:00 PM to 6:00 PM.")
            print("Your appointment with Dr. Suman has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "3":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Rakesh.")
            print("Qualifications: MBBS, MD (Obstetrics & Gynaecology)")
            print("Experience: 9 years in Obstetrics & Gynaecology")
            print("Dr. Rakesh is available from 6:00 PM to 10:00 PM.")
            print("Your appointment with Dr. Rakesh has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")


elif department == "2":
    print("You have selected Diagnostic Department.")
    b= input("Enter the specific diagnostic department you want to visit: "
    "Radiology=1, Pathology=2, Microbiology=3, Biochemistry=4, Immunology=5 :"
    )

    if b == "1":
        print("You have selected Radiology Department.")
        selected_doctor= input("Enter the doctor you want to visit: (Dr. Sam=1, Dr. Sameer=2, Dr. Pragya=3): ")
        if selected_doctor == "1":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Sam.")
            print("Qualifications: MBBS, MD (Radiology)")
            print("Experience: 12 years in Radiology")
            print("Dr. Sam is available from 10:00 AM to 2:00 PM.")
            print("Your appointment with Dr. Sam has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "2":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Sameer.")
            print("Qualifications: MBBS, MD (Radiology)")
            print("Experience: 9 years in Radiology")
            print("Dr. Sameer is available from 2:00 PM to 6:00 PM.")
            print("Your appointment with Dr. Sameer has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")
        elif selected_doctor == "3":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Pragya.")
            print("Qualifications: MBBS, MD (Radiology)")
            print("Experience: 7 years in Radiology")
            print("Dr. Pragya is available from 6:00 PM to 10:00 PM.")
            print("Your appointment with Dr. Pragya has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

    elif b == "2":
        print("You have selected Pathology Department.")
        selected_doctor= input("Enter the doctor you want to visit: (Dr. satwika=1, Dr. Rudra=2, Dr. Manav=3): ")
        if selected_doctor == "1":
            print()
            print('*******************')
            print()
            print("You have selected Dr. satwika.")
            print("Qualifications: MBBS, MD (Pathology)")
            print("Experience: 14 years in Pathology")
            print("Dr. satwika is available from 10:00 AM to 2:00 PM.")
            print("Your appointment with Dr. satwika has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "2":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Rudra.")
            print("Qualifications: MBBS, MD (Pathology)")
            print("Experience: 11 years in Pathology")
            print("Dr. Rudra is available from 2:00 PM to 6:00 PM.")
            print("Your appointment with Dr. Rudra has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "3":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Manav.")
            print("Qualifications: MBBS, MD (Pathology)")
            print("Experience: 9 years in Pathology")
            print("Dr. Manav is available from 6:00 PM to 10:00 PM.")
            print("Your appointment with Dr. Manav has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

    elif b == "3":
        print("You have selected Microbiology Department.")
        selected_doctor= input("Enter the doctor you want to visit: (Dr. Sangwan=1, Dr. Rina=2, Dr. Purvik=3): ")
        if selected_doctor == "1":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Sangwan.")
            print("Qualifications: MBBS, MD (Microbiology)")
            print("Experience: 13 years in Microbiology")
            print("Dr. Sangwan is available from 10:00 AM to 2:00 PM.")
            print("Your appointment with Dr. Sangwan has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "2":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Rina.")
            print("Qualifications: MBBS, MD (Microbiology)")
            print("Experience: 10 years in Microbiology")
            print("Dr. Rina is available from 2:00 PM to 6:00 PM.")
            print("Your appointment with Dr. Rina has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "3":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Purvik.")
            print("Qualifications: MBBS, MD (Microbiology)")
            print("Experience: 8 years in Microbiology")
            print("Dr. Purvik is available from 6:00 PM to 10:00 PM.")
            print("Your appointment with Dr. Purvik has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

    elif b == "4":
        print("You have selected Radiology Department.")
        selected_doctor = input("Enter the doctor you want to visit: (Dr. Soumya=1, Dr. Riya=2, Dr. Kartik=3): ")
        if selected_doctor == "1":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Soumya.")
            print("Qualifications: MBBS, MD (Radiology)")
            print("Experience: 12 years in Radiology")
            print("Dr. Soumya is available from 10:00 AM to 2:00 PM.")
            print("Your appointment with Dr. Soumya has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "2":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Riya.")
            print("Qualifications: MBBS, MD (Radiology)")
            print("Experience: 9 years in Radiology")
            print("Dr. Riya is available from 2:00 PM to 6:00 PM.")
            print("Your appointment with Dr. Riya has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "3":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Kartik.")
            print("Qualifications: MBBS, MD (Radiology)")
            print("Experience: 7 years in Radiology")
            print("Dr. Kartik is available from 6:00 PM to 10:00 PM.")
            print("Your appointment with Dr. Kartik has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

    elif b == "5":
        print("You have selected Immunology Department.")
        selected_doctor = input("Enter the doctor you want to visit: (Dr. Anjali=1, Dr. Ramesh=2, Dr. Priya=3): ")
        if selected_doctor == "1":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Anjali.")
            print("Qualifications: MBBS, MD (Immunology)")
            print("Experience: 11 years in Immunology")
            print("Dr. Anjali is available from 10:00 AM to 2:00 PM.")
            print("Your appointment with Dr. Anjali has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "2":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Ramesh.")
            print("Qualifications: MBBS, MD (Immunology)")
            print("Experience: 8 years in Immunology")
            print("Dr. Ramesh is available from 2:00 PM to 6:00 PM.")
            print("Your appointment with Dr. Ramesh has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "3":
            print()
            print('*******************')
            print()
            print("You have selected Dr. Priya.")
            print("Qualifications: MBBS, MD (Immunology)")
            print("Experience: 6 years in Immunology")
            print("Dr. Priya is available from 6:00 PM to 10:00 PM.")
            print("Your appointment with Dr. Priya has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

elif department == "3":
    print("You have selected Administrative Department.")
    c= input("Enter the specific administrative department you want to visit: (Human Resources=1, Finance=2, Operations=3, Marketing=4, IT=5 ):" )

    if c == "1":
        print("You have selected Human Resources Department.")
        selected_doctor= input("Enter the officer you want to visit: Mr. Rajesh=1, Ms. Priya=2, Mr. Anil=3): ")
        if selected_doctor == "1":
            print()
            print('*******************')
            print()
            print("You have selected Mr. Rajesh.")
            print("Designation: HR Manager")
            print("Experience: 10 years in Human Resources")
            print("Mr. Rajesh is available from 10:00 AM to 2:00 PM.")
            print("Your appointment with Mr. Rajesh has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "2":
            print()
            print('*******************')
            print()
            print("You have selected Ms. Priya.")
            print("Designation: HR Executive")
            print("Experience: 7 years in Human Resources")
            print("Ms. Priya is available from 2:00 PM to 6:00 PM.")
            print("Your appointment with Ms. Priya has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "3":
            print()
            print('*******************')
            print()
            print("You have selected Mr. Anil.")
            print("Designation: HR Assistant")
            print("Experience: 5 years in Human Resources")
            print("Mr. Anil is available from 6:00 PM to 10:00 PM.")
            print("Your appointment with Mr. Anil has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

    elif c == "2":
        print("You have selected Finance Department.")
        selected_doctor= input("Enter the officer you want to visit: Mr. Suresh=1, Ms. Anjali=2, Mr. Rohan=3: ")
        if selected_doctor == "1":
            print()
            print('*******************')
            print()
            print("You have selected Mr. Suresh.")
            print("Designation: Finance Manager")
            print("Experience: 12 years in Finance")
            print("Mr. Suresh is available from 10:00 AM to 2:00 PM.")
            print("Your appointment with Mr. Suresh has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "2":
            print()
            print('*******************')
            print()
            print("You have selected Ms. Anjali.")
            print("Designation: Finance Executive")
            print("Experience: 8 years in Finance")
            print("Ms. Anjali is available from 2:00 PM to 6:00 PM.")
            print("Your appointment with Ms. Anjali has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "3":
            print()
            print('*******************')
            print()
            print("You have selected Mr. Rohan.")
            print("Designation: Finance Assistant")
            print("Experience: 6 years in Finance")
            print("Mr. Rohan is available from 6:00 PM to 10:00 PM.")
            print("Your appointment with Mr. Rohan has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

    elif c == "3":
        print("You have selected Operations Department.")
        selected_doctor= input("Enter the officer you want to visit: (Mr. Amit=1, Ms. Sneha=2, Mr. Karan=3): ")
        if selected_doctor == "1":
            print()
            print('*******************')
            print()
            print("You have selected Mr. Amit.")
            print("Designation: Operations Manager")
            print("Experience: 11 years in Operations")
            print("Mr. Amit is available from 10:00 AM to 2:00 PM.")
            print("Your appointment with Mr. Amit has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "2":
            print()
            print('*******************')
            print()
            print("You have selected Ms. Sneha.")
            print("Designation: Operations Executive")
            print("Experience: 7 years in Operations")
            print("Ms. Sneha is available from 2:00 PM to 6:00 PM.")
            print("Your appointment with Ms. Sneha has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "3":
            print()
            print('*******************')
            print()
            print("You have selected Mr. Karan.")
            print("Designation: Operations Assistant")
            print("Experience: 5 years in Operations")
            print("Mr. Karan is available from 6:00 PM to 10:00 PM.")
            print("Your appointment with Mr. Karan has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

    elif c == "4":
        print("You have selected Marketing Department.")
        selected_doctor= input("Enter the officer you want to visit: (Mr. Rohit=1, Ms. Aisha=2, Mr. Varun=3): ")
        if selected_doctor == "1":
            print()
            print('*******************')
            print()
            print("You have selected Mr. Rohit.")
            print("Designation: Marketing Manager")
            print("Experience: 10 years in Marketing")
            print("Mr. Rohit is available from 10:00 AM to 2:00 PM.")
            print("Your appointment with Mr. Rohit has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "2":
            print()
            print('*******************')
            print("You have selected Ms. Aisha.")
            print()
            print("Designation: Marketing Executive")
            print("Experience: 7 years in Marketing")
            print("Ms. Aisha is available from 2:00 PM to 6:00 PM.")
            print("Your appointment with Ms. Aisha has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "3":
            print()
            print('*******************')
            print()
            print("You have selected Mr. Varun.")
            print("Designation: Marketing Assistant")
            print("Experience: 5 years in Marketing")
            print("Mr. Varun is available from 6:00 PM to 10:00 PM.")
            print("Your appointment with Mr. Varun has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

    elif c == "5":
        print("You have selected IT Department.")
        selected_doctor= input("Enter the officer you want to visit: (Mr. Aditya=1, Ms. Rhea=2, Mr. Kunal=3: ")
        if selected_doctor == "1":
            print()
            print('*******************')
            print()
            print("You have selected Mr. Aditya.")
            print("Designation: IT Manager")
            print("Experience: 12 years in IT")
            print("Mr. Aditya is available from 10:00 AM to 2:00 PM.")
            print("Your appointment with Mr. Aditya has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor== "2":
            print()
            print('*******************')
            print()
            print("You have selected Ms. Rhea.")
            print("Designation: IT Executive")
            print("Experience: 8 years in IT")
            print("Ms. Rhea is available from 2:00 PM to 6:00 PM.")
            print("Your appointment with Ms. Rhea has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

        elif selected_doctor == "3":
            print()
            print('*******************')
            print()
            print("You have selected Mr. Kunal.")
            print("Designation: IT Assistant")
            print("Experience: 6 years in IT")
            print("Mr. Kunal is available from 6:00 PM to 10:00 PM.")
            print("Your appointment with Mr. Kunal has been successfully booked. Please arrive 15 minutes before your scheduled time.")
            print("Thank you for using the Healthcare Management System. We hope you have a great experience at Cygnus Hospital.")

    
    
    elif department not in ["1", "2", "3"]:
            print("Invalid department selection. Please try again.")
                   