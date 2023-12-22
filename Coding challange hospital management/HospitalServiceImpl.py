from IHospitalService import IHospitalService
from Appointmentclass import Appointment
from Exception  import PatientNumberNotFound
from DatabaseConnector import DBConnection
import mysql.connector

class HospitalServiceImpl(IHospitalService):
    def __init__(self):
        self.connection = DBConnection.get_connection()

    def get_appointment_by_id(self, appointment_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM Appointment WHERE appointmentId = %s"
            cursor.execute(query, (appointment_id,))
            result = cursor.fetchone()
            cursor.close()

            if result:
                appointment = Appointment(result['appointmentId'], result['patientId'], result['doctorId'],
                                          result['appointmentDate'], result['description'])
                return appointment
            else:
                return None
        except mysql.connector.Error as err:
            print("Error:", err)
            return None

    def get_appointments_for_patient(self, patient_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM Appointment WHERE patientId = %s"
            cursor.execute(query, (patient_id,))
            results = cursor.fetchall()
            cursor.close()

            appointments = []
            for result in results:
                appointment = Appointment(result['appointmentId'], result['patientId'], result['doctorId'],
                                          result['appointmentDate'], result['description'])
                appointments.append(appointment)

            return appointments
        except mysql.connector.Error as err:
            print("Error:", err)
            return []

    def get_appointments_for_doctor(self, doctor_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM Appointment WHERE doctorId = %s"
            cursor.execute(query, (doctor_id,))
            results = cursor.fetchall()
            cursor.close()

            appointments = []
            for result in results:
                appointment = Appointment(result['appointmentId'], result['patientId'], result['doctorId'],
                                          result['appointmentDate'], result['description'])
                appointments.append(appointment)

            return appointments
        except mysql.connector.Error as err:
            print("Error:", err)
            return []

    def schedule_appointment(self, appointment):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Appointment (patientId, doctorId, appointmentDate, description) " \
                    "VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (appointment.patient_id, appointment.doctor_id,
                                   appointment.appointment_date, appointment.description))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def update_appointment(self, appointment):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Appointment SET patientId = %s, doctorId = %s, " \
                    "appointmentDate = %s, description = %s WHERE appointmentId = %s"
            cursor.execute(query, (appointment.patient_id, appointment.doctor_id,
                                   appointment.appointment_date, appointment.description, appointment.appointment_id))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def cancel_appointment(self, appointment_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Appointment WHERE appointmentId = %s"
            cursor.execute(query, (appointment_id,))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False
