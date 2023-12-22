
class Doctor:
    def __init__(self,doctorId,firstName,lastName,specialization,contactNumber,db_connector):
        self._doctorId=doctorId
        self._firstName=firstName
        self._lastName=lastName
        self._specialization=specialization
        self._contactNumber=contactNumber
        self._db_connector=db_connector

    @property
    def doctorId(self):
        return self._doctorId
    @doctorId.setter
    def doctorId(self, new_doctorId):
        self._doctorId = new_doctorId

    @property
    def firstName(self):
        return self._firstName
    @firstName.setter
    def firstName(self, new_firstName):
        self._firstName = new_firstName

    @property
    def lastName(self):
        return self._lastName
    @lastName.setter
    def lastName(self, new_lastName):
        self._lastName = new_lastName

    @property
    def specialization(self):
        return self._specialization
    @specialization.setter
    def specialization(self, new_specialization):
        self._specialization = new_specialization

    @property
    def contactNumber(self):
        return self._contactNumber
    @contactNumber.setter
    def contactNumber(self, new_contactNumber):
        self._contactNumber = new_contactNumber
