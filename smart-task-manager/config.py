import os

class Config:

    SECRET_KEY = "supersecretkey"

    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Aman#152003@localhost:5432/postgres"

    SQLALCHEMY_TRACK_MODIFICATIONS = False