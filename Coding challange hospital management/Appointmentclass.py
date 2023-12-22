
class Appointment:
    def __init__(self,appointmentId,patientId,doctorId,appointmentDate,description,db_connector):
        self._appointmentId=appointmentId
        self._patientId=patientId
        self._doctorId=doctorId
        self._appointmentDate=appointmentDate
        self._description=description
        self._db_connector=db_connector

    @property
    def appointmentId(self):
        return self._appointmentId
    @appointmentId.setter
    def appointmentId(self, new_appointmentId):
        self._appointmentId = new_appointmentId

    @property
    def patientId(self):
        return self._patientId
    @patientId.setter
    def patientId(self, new_patientId):
        self._patientId = new_patientId

    @property
    def doctorId(self):
        return self._doctorId
    @doctorId.setter
    def doctorId(self, new_doctorId):
        self._doctorId = new_doctorId

    @property
    def appointmentDate(self):
        return self._appointmentDate
    @appointmentDate.setter
    def appointmentDate(self, new_appointmentDate):
        self._appointmentDate = new_appointmentDate

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, new_description):
        self._description = new_description


