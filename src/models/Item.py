from sqlalchemy.orm import Mapped, mapped_column

class Item():
    id: Mapped[int] = mapped_column(primary_key=True)
    make: Mapped[str]
    model: Mapped[str]
    year: Mapped[int]
    color: Mapped[str]
    mileage: Mapped[int]
    image_url: Mapped[str]
