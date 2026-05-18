from pydantic import BaseModel
from typing import Optional
from datetime import date


class BookingDates(BaseModel):
    checkin: date
    checkout: date

class Booking(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Optional [str] = None

class BookingResponse(BaseModel):
    #верхнеуровневый класс. Basemodel-базовая модель pydantic
    bookingid: int
    booking: Booking
    #класс Booking ниже, но расположен выше

    #10:53

