from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel

app = FastAPI()

class Patient(BaseModel):
    id: str
    name: str
    age: int
    gender: str
    address: str
    phone: str
    email: str

patient = [{
    "id": "1",
    "name": "John Doe",
    "age": 30,
    "gender": "Male",
    "address": "123 Main St",
    "phone": "123-456-7890",
    "email": "johndoe@example.com"
},{
    "id":"2",
    "name": "Jane Doe",
    "age": 25,
    "gender": "Female",
    "address": "456 Elm St",
    "phone": "987-654-3210",
    "email": "janedoe@example.com"
}
]

@app.get("/")
async def read_root():
    return {"Message": "Welcome"}

@app.get('/view')
async def view_patient() -> list:
    return patient


@app.post('/create')
async def create_patient(Patient: Patient):
    patient.append(Patient.model_dump())
    return {"Message": "Patient Created"}

@app.get('/view/{patient_id}')
async def view_patient_by_id(patient_id: str = Path(..., description="View patient by the ID stored in DB ", ge=1, example="1")):
    for p in patient:
        if p['id'] == patient_id:
            return p
    raise HTTPException(status_code=404, detail="Patient not found")
   

#update patient records
@app.put('/update/{patient_id}')
async def update_patient(patient_id: str = Path(..., description="Update patient by the ID stored in DB ", ge=1, example="1"), Patient: Patient = Path(..., example="{\"id\": \"1\", \"name\": \"John Doe\", \"age\": 30, \"gender\": \"Male\", \"address\": \"123 Main St\", \"phone\": \"123-456-7890\", \"email\": \"johndoe@example.com\"}")):
    for p in patient:
        if p['id'] == patient_id:
            p.update(Patient.model_dump())
            return {"Message": "Patient updated"}
    raise HTTPException(status_code=404, detail="Patient not found")

#Delete patient Record
@app.delete('/delete/{patient_id}')
async def delete_patient(patient_id: str = Path(..., description="Delete patient by the ID stored in DB ", ge=1, example="1")):
    for p in patient:
        if p['id'] == patient_id:
            patient.remove(p)
            return {"Message": "Patient deleted"}
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get('/sort')
async def sort(sort_by: str = Query(..., description="Sort patients by age or id"), order: str = Query("asc", description="Order of sorting: asc or desc")):
    if sort_by not in ["age", "id"]:
        raise HTTPException(status_code=400, detail="Invalid sort_by value")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order value")
    
    reverse = order == "desc"
    sorted_patients = sorted(patient, key=lambda x: x[sort_by], reverse=reverse)
    return sorted_patients
