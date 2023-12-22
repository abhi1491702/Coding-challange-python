
class Patient:
    def __init__(self,patientId,firstName,lastName,dateOfBirth,gender,contactNumber,address,db_connector):
        self._patientId=patientId
        self._firstName=firstName
        self._lastName=lastName
        self._dateOfBirth=dateOfBirth
        self._gender=gender
        self._contactNumber=contactNumber
        self._address=address
        self._db_connector=db_connector


    @property
    def patientId(self):
        return self._patientId
    @patientId.setter
    def patientId(self, new_patientId):
        self._patientId = new_patientId

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
    def dateOfBirth(self):
        return self._dateOfBirth
    @dateOfBirth.setter
    def dateOfBirth(self, new_dateOfBirth):
        self._dateOfBirth = new_dateOfBirth

    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, new_gender):
        self._gender = new_gender

    @property
    def contactNumber(self):
        return self._contactNumber
    @contactNumber.setter
    def contactNumber(self, new_contactNumber):
        self._contactNumber = new_contactNumber

    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, new_address):
        self._address = new_address
