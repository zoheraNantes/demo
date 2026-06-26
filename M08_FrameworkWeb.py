from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine

Base = declarative_base()

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    street_name = Column(String(255))
    city = Column(String(255))
    user_id = Column(Integer, ForeignKey('user.id'))

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    addresses = relationship("Address", backref="user", cascade="all, delete-orphan")


engine = create_engine('sqlite:///my_db.sqlite', echo=False)
Base.metadata.bind = engine
Base.metadata.create_all(engine)

DbSession = sessionmaker(bind=engine)
session = DbSession()

new_user = User(first_name="Emmanuel", last_name="Macron")
new_address = Address(street_name="Rue du fbg st Honoré", city="Paname", user = new_user)

session.add(new_address)
session.commit()

print([(u.first_name, u.last_name) for u in session.query(User).all()])

users = session.query(User).filter_by(last_name= 'Macron').all()
print([(user.first_name, user.last_name, user.addresses) for user in users])