import os
import psycopg2
from sqlalchemy import update ,create_engine, MetaData, Table,select, Column, Integer, String, Float, DateTime, ForeignKey, text, insert, UniqueConstraint
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, echo=True)

metadata = MetaData()

clients = Table(
    'clients', metadata,
    Column('client_id', Integer, primary_key=True),
    Column('first_name', String(50), nullable=False),
    Column('last_name', String(50), nullable=False),
    Column('email', String(100), nullable=False, unique=True),
    Column('phone_number', String(20))
)

destinations = Table(
    'destinations', metadata,
    Column('destination_id', Integer, primary_key=True),
    Column('name', String(100), nullable=False),
    Column('country', String(50), nullable=False),
    Column('price_per_person', Float, nullable=False),
    UniqueConstraint('name', 'country', name='uix_name_country')
)

bookings = Table(
    'bookings', metadata,
    Column('booking_id', Integer, primary_key=True),
    Column('client_id', Integer, ForeignKey('clients.client_id'), nullable=False),
    Column('booking_date', DateTime, default=datetime),
    Column('total_price', Float, nullable=False)
)

booking_items = Table(
    'booking_items', metadata,
    Column('item_id', Integer, primary_key=True),
    Column('booking_id', Integer, ForeignKey('bookings.booking_id'), nullable=False),
    Column('destination_id', Integer, ForeignKey('destinations.destination_id'), nullable=False),
    Column('travelers_count', Integer, nullable=False)
)

metadata.create_all(engine)

with engine.connect() as connection:
    result = connection.execute(text("SELECT version();"))
    print("Connexion réussie à PostgreSQL :", result.fetchone())

    insert_client = insert(clients).values([
        {
            'first_name': 'Alice',
            'last_name': 'Durand',
            'email': 'alice.durand@example.com',
            'phone_number': '0612345678'
        },
        {
            'first_name': 'Bob',
            'last_name': 'Martin',
            'email': 'bob.martin@example.com',
            'phone_number': '0623456789'
        },
        {
            'first_name': 'Carla',
            'last_name': 'Lopez',
            'email': 'carla.lopez@example.com',
            'phone_number': '0634567890'
        },
        {
            'first_name': 'David',
            'last_name': 'Nguyen',
            'email': 'david.nguyen@example.com',
            'phone_number': '0645678901'
        },
        {
            'first_name': 'Emma',
            'last_name': 'Kassimi',
            'email': 'emma.kassimi@example.com',
            'phone_number': '0656789012'
        }
    ])

    insert_destinations = insert(destinations).values([
        {'name': 'Paris Tour', 'country': 'France', 'price_per_person': 250.0},
        {'name': 'Sahara Adventure', 'country': 'Morocco', 'price_per_person': 300.0},
        {'name': 'Tokyo Discovery', 'country': 'Japan', 'price_per_person': 500.0}

    ])

    client_ids = connection.execute(select(clients.c.client_id)).fetchmany(3)

    booking_insert = insert(bookings).returning(bookings.c.booking_id).values([
        {'client_id': client_ids[0][0], 'booking_date': datetime(2025, 7, 1), 'total_price': 500.0},
        {'client_id': client_ids[1][0], 'booking_date': datetime(2025, 7, 2), 'total_price': 900.0},
        {'client_id': client_ids[2][0], 'booking_date': datetime(2025, 7, 3), 'total_price': 1500.0}
    ])

    booking_ids = connection.execute(select(bookings.c.booking_id)).fetchmany(3)
    destination_ids = connection.execute(select(destinations.c.destination_id)).fetchmany(3)

    insert_booking_items = insert(booking_items).values([
        {
            'booking_id': booking_ids[0][0],
            'destination_id': destination_ids[0][0],
            'travelers_count': 2
        },
        {
            'booking_id': booking_ids[0][0],
            'destination_id': destination_ids[1][0],
            'travelers_count': 1
        },
        {
            'booking_id': booking_ids[1][0],
            'destination_id': destination_ids[1][0],
            'travelers_count': 3
        },
        {
            'booking_id': booking_ids[2][0],
            'destination_id': destination_ids[2][0],
            'travelers_count': 4
        }
    ])




    connection.execute(insert_client)
    connection.execute(insert_destinations)
    connection.execute(booking_insert).fetchall()
    connection.execute(insert_booking_items)
    connection.commit()


    query_clients = select(
        clients.c.first_name,
        clients.c.email,
        clients.c.phone_number
    )
    result_clients = connection.execute(query_clients).fetchall()

    print("Liste des clients :")
    for row in result_clients:
        print(row)

    print("------------------------------")

    query_expensive_destinations = select(
        destinations.c.name,
        destinations.c.country,
        destinations.c.price_per_person
    ).where(destinations.c.price_per_person > 1000.0)

    result_destinations = connection.execute(query_expensive_destinations).fetchall()

    print("Destinations avec un prix > 1000 € :")
    for row in result_destinations:
        print(row)
    print("******************")

    print("Réservations avec nom du client, destination, nb de voyageurs, prix/personne :")
    query_join = (
        select(
            clients.c.first_name,
            destinations.c.name,
            booking_items.c.travelers_count,
            destinations.c.price_per_person
        )
        .select_from(
            booking_items.join(bookings, booking_items.c.booking_id == bookings.c.booking_id)
                        .join(clients, bookings.c.client_id == clients.c.client_id)
                        .join(destinations, booking_items.c.destination_id == destinations.c.destination_id)
        )
    )

    results = connection.execute(query_join).fetchall()
    for row in results:
        print(row)


    print("******************")

    client_id_to_update = 1  
    new_email = "testupdateEmail.email@example.com"

    update_email = (
        update(clients)
        .where(clients.c.client_id == client_id_to_update)
        .values(email=new_email)
    )

    connection.execute(update_email)
    connection.commit()

    country_target = 'Morocco'

    reduce_price = (
        update(destinations)
        .where(destinations.c.country == country_target)
        .values(price_per_person=destinations.c.price_per_person * 0.9)
    )

    connection.execute(reduce_price)
    connection.commit()



    print("******************")





