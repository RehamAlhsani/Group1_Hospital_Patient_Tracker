from hospital import Hospital

hospital = Hospital()

while True :
    print("Hospital System : ")
    print("1. Register Patient")
    print("2. Add Doctor")
    print("3. Book Appointment")
    print("4. Cancel Appointment")
    print("5. View Patient Record")
    print("6. View Doctor Schedule")
    print("7. Today's Appointments")
    print("8. Exit")

    try :
        choice = int(input("Choose : "))
    except ValueError:
        print("Please, Enter a number !")
        continue

    match choice :

        case 1 :
            hospital.register_patient()

        case 2 :
            hospital.add_doctor()

        case 3 :
            hospital.book_appointment()

        case 4 :
            hospital.cancel_appointment()

        case 5 :
            hospital.view_patient_record()

        case 6 :
            hospital.view_doctor_schedule()

        case 7 :
            hospital.todays_appointments()

        case 8 :
            print("Goodbye !")
            break

        case _ :
            print("Invalid choice !")