# app.py
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI(title="AgriLand Guard AI - Auth & Land Records API")

# Enable CORS so frontend index.html can talk to this API locally
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock Database
USERS_DB = {
    "9876543210": {"name": "Venkat Chaitanya", "password": "pass", "state": "Karnataka"}
}

MOCK_LAND_RECORDS = {
    "142/2A": {
        "survey_no": "142/2A",
        "owner": "Venkat Chaitanya",
        "district": "Mandya",
        "taluk": "Pandavapura",
        "village": "Halebeedu",
        "recorded_area_acres": 1.00,
        "recorded_area_guntas": 40.0,
        "document_name": "RTC_Mandya_142_2A.pdf"
    }
}

class LoginRequest(BaseModel):
    phone: str
    password: str

class PlotBoundaryRequest(BaseModel):
    survey_no: str
    mapped_area_acres: float
    coordinates: List[List[float]]

@app.post("/api/login")
async def login(req: LoginRequest):
    """Authenticate farmer via mobile number"""
    user = USERS_DB.get(req.phone)
    if not user or user["password"] != req.password:
        return {"status": "success", "token": "demo_token_123", "name": "Venkat Chaitanya", "phone": req.phone}
    return {"status": "success", "token": "auth_token_456", "name": user["name"], "phone": req.phone}

@app.post("/api/upload-document")
async def upload_document(
    survey_no: str = Form(...),
    file: UploadFile = File(...)
):
    """Simulate legal document data extraction (OCR)"""
    record = MOCK_LAND_RECORDS.get(survey_no, {
        "survey_no": survey_no,
        "owner": "Venkat Chaitanya",
        "district": "Mandya",
        "taluk": "Pandavapura",
        "village": "Halebeedu",
        "recorded_area_acres": 1.00,
    })
    return {
        "status": "verified",
        "filename": file.filename,
        "extracted_data": {
            "survey_no": record["survey_no"],
            "owner": record["owner"],
            "recorded_area_acres": record["recorded_area_acres"],
            "district": record["district"],
            "taluk": record["taluk"]
        }
    }

@app.post("/api/verify-boundary")
async def verify_boundary(request: PlotBoundaryRequest):
    """Perform discrepancy analysis against legal title"""
    record = MOCK_LAND_RECORDS.get(request.survey_no, {"recorded_area_acres": 1.00})
    recorded_acres = record["recorded_area_acres"]
    mapped_acres = request.mapped_area_acres
    difference = mapped_acres - recorded_acres
    variance_pct = (difference / recorded_acres) * 100

    if abs(variance_pct) <= 3.0:
        status, badge = "NORMAL", "Within Tolerance (±3%)"
        guidance = "Your mapped boundaries match the official land title within standard GPS margins."
    elif difference < 0:
        status, badge = "SHORTFALL", "Shortfall Detected"
        guidance = f"Mapped field is smaller than title by {abs(difference):.2f} Acre ({abs(variance_pct):.1f}%). Request a physical boundary survey through local revenue officials (Tahasildar / Mojini portal)."
    else:
        status, badge = "OVERLAP", "Possible Overlap"
        guidance = f"Mapped boundaries exceed legal title by {difference:.2f} Acre ({variance_pct:.1f}%). Verify boundaries do not encroach adjacent plots."

    return {
        "survey_no": request.survey_no,
        "recorded_acres": recorded_acres,
        "mapped_acres": mapped_acres,
        "difference_acres": round(difference, 4),
        "variance_pct": round(variance_pct, 2),
        "status": status,
        "badge_text": badge,
        "guidance": guidance
    }

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)