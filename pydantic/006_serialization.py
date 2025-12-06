from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    pincode: str

class Patient(BaseModel):
    name: str
    age: int
    address: Address
    
address_dict = {"street":"123 Main St", "city":"Anytown", "pincode":"12345"}

address1 = Address(**address_dict)

patient_dict = {"name":"John Doe", "age":30, "address":address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.address.street)
print(patient1.address.city)
print(patient1.address.pincode)


temp =  patient1.model_dump()

temp_json = patient1.model_dump_json()
temp_json = patient1.model_dump_json(exclude=['address']) # This also has exclude/include parameters
temp_json = patient1.model_dump_json(exclude_unset=True) # This excludes fields that have not been explicitly set

print(temp)
print(type(temp))

print(temp_json)
print(type(temp_json))
print(patient1.model_dump())