from database.db import session_maker
from database.tables import User, Dog, Sex, Tag, Breed

session = session_maker()

user1 = User(
    email="john.doe@example.com",
    first_name="John",
    last_name="Doe",
    location="New York",
    is_premium=True
)

user2 = User(
    email="jane.doe@example.com",
    first_name="Jane",
    last_name="Doe",
    location="California",
    is_premium=False
)

session.add_all([user1, user2])
session.commit()

# Create some dogs
dog1 = Dog(
    name="Buddy",
    photo_url="http://example.com/buddy.jpg",
    sex=Sex.MALE,
    age=3,
    breed=Breed.AKITA,
    tags=[Tag.PASSPORT, Tag.VACCINATION],
    description="A friendly Akita.",
    is_visible=True,
    owner_id=user1.id
)

dog2 = Dog(
    name="Lucy",
    photo_url="http://example.com/lucy.jpg",
    sex=Sex.FEMALE,
    age=4,
    breed=Breed.HUSKY,
    tags=[Tag.VACCINATION],
    description="An energetic Husky.",
    is_visible=True,
    owner_id=user2.id
)

session.add_all([dog1, dog2])
session.commit()

session.close()