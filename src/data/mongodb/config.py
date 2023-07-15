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

    @staticmethod
    def get_pokemon_in_tournament(tournament_id: str) -> list[dict]:
        """
        Retrieve Pokémon data for a given tournament.

        Args:
            tournament_id (str): Tournament ID.

        Returns:
            list[dict]: Pokémon data for the tournament.
        """
        pokemon = Database.find("pokemon", {"tournament_id": tournament_id})
        pokemon_counts: dict = {}
        pokemon_data = list(pokemon)
        pokemon_data_with_usage = []
        for pokemon in pokemon_data:
            pokemon_name = pokemon["name"]
            if pokemon_name not in pokemon_counts:
                pokemon_counts[pokemon_name] = 0
            pokemon_counts[pokemon_name] += 1

        for pokemon in pokemon_data:
            pokemon_data_with_usage.append(
                {
                    "_id": str(pokemon["_id"]),
                    "name": pokemon["name"],
                    "usage": round(
                        pokemon_counts[pokemon["name"]] / len(pokemon_data) * 100, 2
                    ),
                }
            )

        pokemon_data_with_usage = list(
            {v["name"]: v for v in pokemon_data_with_usage}.values()
        )
        pokemon_data_with_usage.sort(key=lambda pokemon: pokemon["usage"], reverse=True)
        return pokemon_data_with_usage

    @staticmethod
    def get_pokemon_detail(pokemon_name: str, tournament_id: str) -> dict:
        """
        Retrieve Pokémon data for a given tournament.

        Args:
            pokemon_name (str): Pokémon name.
            tournament_id (str): Tournament ID.

        Returns:
            dict: Pokémon data.
        """
        pokemon_query = Database.find(
            "pokemon", {"name": pokemon_name, "tournament_id": tournament_id}
        )
        pokemon_list = list(pokemon_query)
        teratype_stats: dict = {}
        ability_stats: dict = {}
        item_stats: dict = {}
        moves_stats: dict = {}
        for pokemon in pokemon_list:
            teratype = pokemon["tera_type"]
            ability = pokemon["ability"]
            item = pokemon["item"]
            move1 = pokemon["move1"]
            move2 = pokemon["move2"]
            move3 = pokemon["move3"]
            move4 = pokemon["move4"]
            if teratype not in teratype_stats:
                teratype_stats[teratype] = 0
            if ability not in ability_stats:
                ability_stats[ability] = 0
            if item not in item_stats and item is not None:
                item_stats[item] = 0
            if move1 not in moves_stats:
                moves_stats[move1] = 0
            if move2 not in moves_stats and move2 is not None:
                moves_stats[move2] = 0
            if move3 not in moves_stats and move3 is not None:
                moves_stats[move3] = 0
            if move4 not in moves_stats and move4 is not None:
                moves_stats[move4] = 0

            teratype_stats[teratype] += 1
            ability_stats[ability] += 1
            if item is not None:
                item_stats[item] += 1
            moves_stats[move1] += 1
            if move2 is not None:
                moves_stats[move2] += 1
            if move3 is not None:
                moves_stats[move3] += 1
            if move4 is not None:
                moves_stats[move4] += 1

        pokemon_detail: dict[list[dict]] = {}
        # get percentage of usage of each teratype, abilities, items and moves and sort by that each independt list
        # then join them all on a dict
        pokemon_detail["tera_type"] = sorted(
            [
                {
                    "name": teratype,
                    "usage": round(
                        teratype_stats[teratype] / len(pokemon_list) * 100, 2
                    ),
                }
                for teratype in teratype_stats
            ],
            key=lambda teratype: teratype["usage"],
            reverse=True,
        )
        pokemon_detail["ability"] = sorted(
            [
                {
                    "name": ability,
                    "usage": round(ability_stats[ability] / len(pokemon_list) * 100, 2),
                }
                for ability in ability_stats
            ],
            key=lambda ability: ability["usage"],
            reverse=True,
        )
        pokemon_detail["item"] = sorted(
            [
                {
                    "name": item,
                    "usage": round(item_stats[item] / len(pokemon_list) * 100, 2),
                }
                for item in item_stats
            ],
            key=lambda item: item["usage"],
            reverse=True,
        )
        pokemon_detail["moves"] = sorted(
            [
                {
                    "name": move,
                    "usage": round(moves_stats[move] / len(pokemon_list) * 100, 2),
                }
                for move in moves_stats
            ],
            key=lambda move: move["usage"],
            reverse=True,
        )
        print(pokemon_detail)
        return pokemon_detail
