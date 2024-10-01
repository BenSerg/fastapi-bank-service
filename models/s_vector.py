from pydantic import BaseModel, constr, conint, confloat


class SVector(BaseModel):
    date: constr(pattern=r"^\d{2}\.\d{2}\.\d{4}$")
    periods: conint(ge=1, le=60)
    amount: conint(ge=10_000, le=1_000_000)
    rate: confloat(ge=1, le=8)
