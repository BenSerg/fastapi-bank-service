from fastapi import APIRouter, HTTPException
from models.s_vector import SVector
from utils.date_utils import last_day_of_month
from datetime import datetime, timedelta
from typing import Optional

router = APIRouter(
    prefix="/calculate",
    tags=["Расчет баланса"]
)


@router.post("")
async def calculate(data: SVector) -> dict[str, Optional[float]]:
    try:
        tmp_date = datetime.strptime(data.date, "%d.%m.%Y")
        tmp_amount = data.amount
        results = {}
        for period in range(1, data.periods + 1):
            if period > data.periods:
                results[tmp_date.strftime("%d.%m.%Y")] = None
            else:
                tmp_amount *= (1 + data.rate / 12 / 100)
                results[tmp_date.strftime("%d.%m.%Y")] = round(tmp_amount, 2)
                tmp_date = last_day_of_month(tmp_date + timedelta(days=1))
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
