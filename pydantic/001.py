from pydantic import BaseModel, validator
    
class Patient(BaseModel):
    name: str
    age: int 
    weight: float
    
def insert_patient(Patient):
    print(Patient.name)
    print(Patient.age)

patient_info = Patient(name="John", age=30)

insert_patient(patient_info)
    
