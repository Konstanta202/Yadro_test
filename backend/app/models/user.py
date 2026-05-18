from typing import Optional
from sqlalchemy import TIMESTAMP, BigInteger
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        index=True
    )

    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    father_name: Mapped[Optional[str]] = mapped_column(nullable=True)
    gender: Mapped[Optional[str]] = mapped_column(nullable=True)
    gender_code: Mapped[Optional[str]] = mapped_column(nullable=True)
    date_of_birth: Mapped[Optional[str]] = mapped_column(nullable=True)
    years_old: Mapped[Optional[int]] = mapped_column(nullable=True)

    phone: Mapped[Optional[str]] = mapped_column(nullable=True)
    email: Mapped[Optional[str]] = mapped_column(nullable=True)
    login: Mapped[Optional[str]] = mapped_column(nullable=True)
    password: Mapped[Optional[str]] = mapped_column(nullable=True)

    passport_num: Mapped[Optional[str]] = mapped_column(nullable=True)
    passport_serial: Mapped[Optional[str]] = mapped_column(nullable=True)
    passport_number: Mapped[Optional[int]] = mapped_column(nullable=True)
    passport_code: Mapped[Optional[str]] = mapped_column(nullable=True)
    passport_issued: Mapped[Optional[str]] = mapped_column(nullable=True)
    passport_date: Mapped[Optional[str]] = mapped_column(nullable=True)

    inn_fiz: Mapped[Optional[str]] = mapped_column(nullable=True)
    inn_ur: Mapped[Optional[str]] = mapped_column(nullable=True)
    snils: Mapped[Optional[str]] = mapped_column(nullable=True)
    oms: Mapped[Optional[BigInteger]] = mapped_column(
        BigInteger,
        nullable=True
    )
    ogrn: Mapped[Optional[str]] = mapped_column(nullable=True)
    kpp: Mapped[Optional[int]] = mapped_column(nullable=True)

    address: Mapped[Optional[str]] = mapped_column(nullable=True)
    address_reg: Mapped[Optional[str]] = mapped_column(nullable=True)
    country: Mapped[Optional[str]] = mapped_column(nullable=True)
    region: Mapped[Optional[str]] = mapped_column(nullable=True)
    city: Mapped[Optional[str]] = mapped_column(nullable=True)
    street: Mapped[Optional[str]] = mapped_column(nullable=True)
    house: Mapped[Optional[int]] = mapped_column(nullable=True)
    apartment: Mapped[Optional[int]] = mapped_column(nullable=True)

    bank_bik: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    bank_corr: Mapped[Optional[str]] = mapped_column(nullable=True)
    bank_inn: Mapped[Optional[BigInteger]] = mapped_column(
        BigInteger,
        nullable=True
    )
    bank_kpp: Mapped[Optional[int]] = mapped_column(nullable=True)
    bank_num: Mapped[Optional[str]] = mapped_column(nullable=True)
    bank_client: Mapped[Optional[str]] = mapped_column(nullable=True)
    bank_card: Mapped[Optional[str]] = mapped_column(nullable=True)
    bank_date: Mapped[Optional[str]] = mapped_column(nullable=True)
    bank_cvc: Mapped[Optional[int]] = mapped_column(nullable=True)

    edu_specialty: Mapped[Optional[str]] = mapped_column(nullable=True)
    edu_program: Mapped[Optional[str]] = mapped_column(nullable=True)
    edu_name: Mapped[Optional[str]] = mapped_column(nullable=True)
    edu_doc_num: Mapped[Optional[str]] = mapped_column(nullable=True)
    edu_reg_number: Mapped[Optional[str]] = mapped_column(nullable=True)
    edu_year: Mapped[Optional[int]] = mapped_column(nullable=True)

    car_brand: Mapped[Optional[str]] = mapped_column(nullable=True)
    car_model: Mapped[Optional[str]] = mapped_column(nullable=True)
    car_year: Mapped[Optional[int]] = mapped_column(nullable=True)
    car_color: Mapped[Optional[str]] = mapped_column(nullable=True)
    car_number: Mapped[Optional[str]] = mapped_column(nullable=True)
    car_vin: Mapped[Optional[str]] = mapped_column(nullable=True)
    car_sts: Mapped[Optional[str]] = mapped_column(nullable=True)
    car_sts_date: Mapped[Optional[str]] = mapped_column(nullable=True)
    car_pts: Mapped[Optional[str]] = mapped_column(nullable=True)
    car_pts_date: Mapped[Optional[str]] = mapped_column(nullable=True)

    created_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP,
        server_default=func.now()
    )

    updated_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )

    def __repr__(self):
        return (
            f"<User(id={self.id},"
            f"name='{self.first_name} {self.last_name}')>"
        )
