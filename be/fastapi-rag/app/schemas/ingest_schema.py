from pydantic import BaseModel

class IngestRequest(BaseModel):
    rebuild: bool = True