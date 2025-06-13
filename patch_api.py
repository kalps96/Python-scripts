from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess

app = FastAPI()

os_type: str
#to define variable types in f
# os_type: strunction
class PatchRequest(BaseModel):
    os_type: str

app.post("/patch")
def apply_patch(req ,PatchRequest):
    if req.os_type == "Linux":
       cmd = ["/deploy.sh", ""] 
    elif req.os_type == "Windows":
       cmd = ["powershell/exe", "deploy.ps1"]
    else:
       raise HTTPException(status_code = 400, capture = "unsupported type")
    
    try: 
       result = subprocess.run(cmd, capture_output = True )
       return{"status": "sucess", "output": result.stdout}
    except Exception as e:
       raise HTTPException(status_code=500, detail=str(e))

              


