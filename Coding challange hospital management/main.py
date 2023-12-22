from DatabaseConnector import DatabaseConnector
host = "localhost"
database = "hospitalmanagementsystem"
user = "root"
password = "Ram@12345"


db_connector = DatabaseConnector(host, database, user, password)
db_connector.open_connection()
db_connector.close_connection()


from HospitalServiceImpl import HospitalServiceImpl
from Exception  import PatientNumberNotFound

class MainModule:
    @staticmethod
    def main():
        # Create an instance of the service implementation class
        hospital_service = HospitalServiceImpl()

        # Trigger methods in the service implementation class
        try:
            # Example: Get appointment by ID
            appointment = hospital_service.get_appointment_by_id(1)
            if appointment:
                print("Appointment Details:")
                appointment.print_details()
            else:
                print("Appointment not found.")

            # Example: Get appointments for a patient
            patient_id = 1
            appointments_for_patient = hospital_service.get_appointments_for_patient(patient_id)
            if appointments_for_patient:
                print("\nAppointments for Patient ID", patient_id)
                for appointment in appointments_for_patient:
                    appointment.print_details()
                    print("------------------------")
            else:
                print("No appointments found for Patient ID", patient_id)

            # Example: Handle PatientNumberNotFoundException
            invalid_patient_id = 999
            try:
                appointment_for_invalid_patient = hospital_service.get_appointments_for_patient(invalid_patient_id)
            except PatientNumberNotFound as e:
                print(f"\nException: {e}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    MainModule.main()

