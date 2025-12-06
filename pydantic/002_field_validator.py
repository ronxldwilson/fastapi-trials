from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated
    
class Patient(BaseModel):
    name: Annotated[str, Field(..., min_length=1, max_length=100, description="Name of the patient", examples=["John"])]
    age: int = Field(..., gt=0, lt=120)
    # weight: float     This allows for type conversions
    weight: Annotated[float, Field(..., gt=0, strict=True) ]
    height: float
    #married: bool
    married: Annotated[bool, Field(..., default=False, description="Marital status of the patient")]
    email: EmailStr
    linkedin_url: AnyUrl 
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]
    
    @field_validator('age')
    @classmethod
    def email_valid(cls, v):
        valid_domain = ["example.com", "gmail.com", "yahoo.com"]
        check = v.split('@')[-1]
        if check not in valid_domain:
            raise ValueError("Invalid email domain")
        return v
    
def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.allergies)
    print(patient.contact_details)

patient_info = { "name": "John", 
                "age": "30", 
                "weight": 70, 
                "height": 170, 
                "married": False, 
                "allergies": ["penicillin"], 
                "email": "john@example.com",
                "linkedin_url": "https://www.linkedin.com/in/john-doe/",
                "contact_details": {"email": "john@example.com", "phone": "123-456-7890"}}


patient01 = Patient(**patient_info)


insert_patient(patient01) 
    
