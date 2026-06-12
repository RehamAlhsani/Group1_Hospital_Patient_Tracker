from classes import Patient , Doctor , GeneralDoctor , Specialist


class Hospital :
    def __init__(self) :
        self.patients = {}
        self.doctors = {}
        self.blood_types = set()

    # System Features  1 : Register a New Patient 
    def register_patient(self) :
        name = input(" What's your name ? ")
        national_id = input(" What's your national ID ? ")

        if national_id in self.patients :
            print(" Patient already exists ! ")
            return

        try :
            age = int(input(" How old are you ? "))
        except ValueError :
            print("Please, Enter a number for age !")
            return

        blood_type = input(" What's your blood type ? ")

        patient = Patient(name , national_id , age , blood_type)

        self.patients[national_id] = patient
        self.blood_types.add(blood_type)

        print("Patient registered")

    # System Features  2 : Add a New Doctor  
    def add_doctor(self) :
        name = input(" What's the doctor's name ? ")
        doctor_id = input(" What's the doctor ID ? ")
        doc_type = input(" What's the type : general or specialist ? ").lower()
        department = input(" What's the department ? ")

        match doc_type :
            case "general" :
                doctor = GeneralDoctor(name , doctor_id , department)

            case "specialist" :
                specialty = input("Specialty ? ")
                doctor = Specialist(name , doctor_id , department , specialty)

            case _ :
                print("Invalid type")
                return

        self.doctors[doctor_id] = doctor
        print("Doctor added")

    # System Features  3 : Book an Appointment  
    def book_appointment(self) :
        patient_id = input("What's the patient ID ? ")
        doctor_id = input("What's the doctor ID ? ")

        if patient_id not in self.patients or doctor_id not in self.doctors:
           print("Not found !")
           return

        patient = self.patients[patient_id]
        doctor = self.doctors[doctor_id]

        date = input("Date (YYYY-MM-DD) ? ")
        time = input("Time ? ")

        for appt in doctor.appointments :
            if appt[0] == date and appt[1] == time :
              print("Doctor busy")
              return

        appointment = (date, time, doctor.name, patient.name)

        doctor.add_appointment(appointment)
        patient.add_note(f"Booked with Dr {doctor.name}")

        print(f"Booked - Fee: {doctor.consultation_fee()} SAR")
        print("Appointment booked successfully")



    # System Features 4 : Cancel an Appointment 
    def cancel_appointment(self):
        doctor_id = input("Enter doctor ID ? ")

        if doctor_id not in self.doctors:
            print("Doctor not found !")
            return

        doctor = self.doctors[doctor_id]

        date = input("Enter Date ? ")
        time = input("Enter Time ? ")

        for appt in doctor.appointments:
            if appt[0] == date and appt[1] == time:

                doctor.cancel_appointment(appt)

                patient_name = appt[3]

                for patient in self.patients.values():
                    if patient.name == patient_name:
                        patient.add_note(f"Cancelled with Dr {doctor.name}")

                print("Appointment cancelled")
                return

        print("Appointment not found !")

    # System Features 5 : View Patient Record 
    def view_patient_record(self):
        patient_id = input(" Enter patient ID ? ")

        if patient_id not in self.patients:
            print("Patient not found !")
            return

        patient = self.patients[patient_id]

        patient.display()

        print("\nMedical History ?")
        for note in patient.get_history():
            print("-", note)

    # System Features 6 : View Doctor Schedule  
    def view_doctor_schedule(self) :
        doctor_id = input("Enter doctor ID ?")

        if doctor_id not in self.doctors :
            print("Doctor not found !")
            return

        doctor = self.doctors[doctor_id]

        doctor.display()

        print("\nAppointments ? ")
        for appt in doctor.appointments:
            print(appt)  

    # System Features 7 : Today's Appointments
    def todays_appointments(self) :
        date = input("Enter today's date (YYYY-MM-DD) ? ")

        total = 0

        for doctor in self.doctors.values() :
            for appt in doctor.appointments :
                if appt[0] == date :
                    print(f"{doctor.name} - {appt}")

                    total += doctor.consultation_fee()  

        print(f"\nTotal Earnings: {total} SAR")