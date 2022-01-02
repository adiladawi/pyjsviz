from pydantic import BaseModel

class TemporalSuperSampling(BaseModel):
    enable: bool = False