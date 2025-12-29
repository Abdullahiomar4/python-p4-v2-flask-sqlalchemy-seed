#!/usr/bin/env python3
from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():

    # Initialize Faker
    fake = Faker()

    # Delete all rows before seeding
    Pet.query.delete()

    # List of species
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Generate 10 random pets
    pets = [Pet(name=fake.first_name(), species=rc(species)) for _ in range(10)]

    # Add all pets to database
    db.session.add_all(pets)
    db.session.commit()

    print("Database seeded with 10 pets!")
