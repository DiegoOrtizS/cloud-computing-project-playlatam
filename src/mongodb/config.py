import os

import pymongo
from dotenv import load_dotenv

from mongodb.validators import (
    pokemon_validator,
    team_validator,
    tournament_validator,
)

load_dotenv()


class Database:
    """
    Database class to connect to MongoDB

    Attributes:
        URI (str): MongoDB connection URI.
        DATABASE (pymongo.database.Database | None): MongoDB database.
    """

    URI = f"mongodb+srv://admin:{os.getenv('PASSWORD')}@playlatampokemonvgc.6gdjrin.mongodb.net/"
    DB = None

    @staticmethod
    def initialize() -> None:
        """
        Initialize database connection.
        """
        client = pymongo.MongoClient(Database.URI)
        Database.DB = client[os.getenv("DB_NAME")]
        collection_names = Database.DB.list_collection_names()

        if "pokemon" not in collection_names:
            Database.DB.create_collection("pokemon", validator=pokemon_validator)

        if "tournament" not in collection_names:
            Database.DB.create_collection("tournament", validator=tournament_validator)

        if "team" not in collection_names:
            Database.DB.create_collection("team", validator=team_validator)

    @staticmethod
    def insert_one(collection: str, data: dict) -> None:
        """
        Insert data into collection.

        Args:
            collection (str): Collection name.
            data (dict): Data to insert.
        """
        Database.DB[collection].insert_one(data)

    @staticmethod
    def insert_many(collection: str, data: list[dict]) -> None:
        """
        Insert many data into collection.

        Args:
            collection (str): Collection name.
            data (list[dict]): Data to insert.
        """
        Database.DB[collection].insert_many(data)

    @staticmethod
    def find(collection: str, query: dict) -> pymongo.cursor.Cursor:
        """
        Find data in collection.

        Args:
            collection (str): Collection name.
            query (dict): Query to find.

        Returns:
            pymongo.cursor.Cursor: Cursor with data.
        """
        return Database.DB[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: dict) -> dict | None:
        """
        Find one data in collection.

        Args:
            collection (str): Collection name.
            query (dict): Query to find.

        Returns:
            dict | None: Data found.
        """
        return Database.DB[collection].find_one(query)
