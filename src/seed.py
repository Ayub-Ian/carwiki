from datetime import datetime, timedelta
from app import create_app, db
from app.models import Item, Auction, Status
import uuid

app = create_app()

def seed_data():
    print("Starting seeding data ....")
    with app.app_context():
        # Drop existing data (optional)
        db.drop_all()
        db.create_all()

        # Create auction items
        auctions = [
            # 1 Ford GT
            Auction(
                id=uuid.UUID("afbee524-5972-4075-8800-7d1f9d7b0a0c"),
                status=Status.LIVE,
                reserve_price=20000,
                seller='bob',
                auction_end=datetime.utcnow() + timedelta(days=10),
                item=Item(
                    make='Ford',
                    model='GT',
                    color='White',
                    mileage=50000,
                    year=2020,
                    image_url='https://cdn.pixabay.com/photo/2016/05/06/16/32/car-1376190_960_720.jpg'
                )
            ),
            # 2 Bugatti Veyron
            Auction(
                id=uuid.UUID("c8c3ec17-01bf-49db-82aa-1ef80b833a9f"),
                status=Status.LIVE,
                reserve_price=90000,
                seller='alice',
                auction_end=datetime.utcnow() + timedelta(days=60),
                item=Item(
                    make='Bugatti',
                    model='Veyron',
                    color='Black',
                    mileage=15035,
                    year=2018,
                    image_url='https://cdn.pixabay.com/photo/2012/05/29/00/43/car-49278_960_720.jpg'
                )
            ),
            # 3 Ford Mustang
            Auction(
                id=uuid.UUID("bbab4d5a-8565-48b1-9450-5ac2a5c4a654"),
                status=Status.LIVE,
                seller='bob',
                auction_end=datetime.utcnow() + timedelta(days=4),
                item=Item(
                    make='Ford',
                    model='Mustang',
                    color='Black',
                    mileage=65125,
                    year=2023,
                    image_url='https://cdn.pixabay.com/photo/2012/11/02/13/02/car-63930_960_720.jpg'
                )
            ),
            # 4 Mercedes SLK
            Auction(
                id=uuid.UUID("155225c1-4448-4066-9886-6786536e05ea"),
                status=Status.RESERVE_NOT_MET,
                reserve_price=50000,
                seller='tom',
                auction_end=datetime.utcnow() + timedelta(days=-10),
                item=Item(
                    make='Mercedes',
                    model='SLK',
                    color='Silver',
                    mileage=15001,
                    year=2020,
                    image_url='https://cdn.pixabay.com/photo/2016/04/17/22/10/mercedes-benz-1335674_960_720.png'
                )
            ),
            # 5 BMW X1
            Auction(
                id=uuid.UUID("466e4744-4dc5-4987-aae0-b621acfc5e39"),
                status=Status.LIVE,
                reserve_price=20000,
                seller='alice',
                auction_end=datetime.utcnow() + timedelta(days=30),
                item=Item(
                    make='BMW',
                    model='X1',
                    color='White',
                    mileage=90000,
                    year=2017,
                    image_url='https://cdn.pixabay.com/photo/2017/08/31/05/47/bmw-2699538_960_720.jpg'
                )
            ),
            # 6 Ferrari Spider
            Auction(
                id=uuid.UUID("dc1e4071-d19d-459b-b848-b5c3cd3d151f"),
                status=Status.LIVE,
                reserve_price=20000,
                seller='bob',
                auction_end=datetime.utcnow() + timedelta(days=45),
                item=Item(
                    make='Ferrari',
                    model='Spider',
                    color='Red',
                    mileage=50000,
                    year=2015,
                    image_url='https://cdn.pixabay.com/photo/2017/11/09/01/49/ferrari-458-spider-2932191_960_720.jpg'
                )
            ),
            # 7 Ferrari F-430
            Auction(
                id=uuid.UUID("47111973-d176-4feb-848d-0ea22641c31a"),
                status=Status.LIVE,
                reserve_price=150000,
                seller='alice',
                auction_end=datetime.utcnow() + timedelta(days=13),
                item=Item(
                    make='Ferrari',
                    model='F-430',
                    color='Red',
                    mileage=5000,
                    year=2022,
                    image_url='https://cdn.pixabay.com/photo/2017/11/08/14/39/ferrari-f430-2930661_960_720.jpg'
                )
            ),
            # 8 Audi R8
            Auction(
                id=uuid.UUID("6a5011a1-fe1f-47df-9a32-b5346b289391"),
                status=Status.LIVE,
                seller='bob',
                auction_end=datetime.utcnow() + timedelta(days=19),
                item=Item(
                    make='Audi',
                    model='R8',
                    color='White',
                    mileage=10050,
                    year=2021,
                    image_url='https://cdn.pixabay.com/photo/2019/12/26/20/50/audi-r8-4721217_960_720.jpg'
                )
            ),
            # 9 Audi TT
            Auction(
                id=uuid.UUID("40490065-dac7-46b6-acc4-df507e0d6570"),
                status=Status.LIVE,
                reserve_price=20000,
                seller='tom',
                auction_end=datetime.utcnow() + timedelta(days=20),
                item=Item(
                    make='Audi',
                    model='TT',
                    color='Black',
                    mileage=25400,
                    year=2020,
                    image_url='https://cdn.pixabay.com/photo/2016/09/01/15/06/audi-1636320_960_720.jpg'
                )
            ),
            # 10 Ford model T
            Auction(
                id=uuid.UUID("3659ac24-29dd-407a-81f5-ecfe6f924b9b"),
                status=Status.LIVE,
                reserve_price=20000,
                seller='bob',
                auction_end=datetime.utcnow() + timedelta(days=48),
                item=Item(
                    make='Ford',
                    model='Model T',
                    color='Rust',
                    mileage=150150,
                    year=1938,
                    image_url='https://cdn.pixabay.com/photo/2017/08/02/19/47/vintage-2573090_960_720.jpg'
                )
            ),
        ]

        # Add all auction items to the session
        db.session.add_all(auctions)
        db.session.commit()

    print("Finished seeding! Hoorah.")
if __name__ == "__main__":
    seed_data()
