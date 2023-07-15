from utils.constants import POKEMON_TYPES

pokemon_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["_id", "tournament_id", "name", "tera_type", "ability", "move1"],
        "properties": {
            "_id": {
                "bsonType": "objectId",
                "description": "must be an objectId and is required",
            },
            "tournament_id": {
                "bsonType": "string",
                "description": "must be an string and is required",
            },
            "name": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "tera_type": {
                "bsonType": "string",
                "enum": POKEMON_TYPES,
                "description": "must be one of the Pokémon types",
            },
            "ability": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "item": {
                "bsonType": ["string", "null"],
                "description": "must be a string or null",
            },
            "move1": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "move2": {
                "bsonType": ["string", "null"],
                "description": "must be a string or null",
            },
            "move3": {
                "bsonType": ["string", "null"],
                "description": "must be a string or null",
            },
            "move4": {
                "bsonType": ["string", "null"],
                "description": "must be a string or null",
            },
        },
    }
}
