team_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["_id", "tournament_id", "pokemon"],
        "properties": {
            "_id": {
                "bsonType": "objectId",
                "description": "must be an objectId and is required",
            },
            "tournament_id": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "pokemon": {
                "bsonType": "array",
                "description": "must be an array and is required",
                "items": {
                    "bsonType": "object",
                    "required": ["_id", "name"],
                    "properties": {
                        "_id": {
                            "bsonType": "objectId",
                            "description": "must be an objectId and is required",
                        },
                        "name": {
                            "bsonType": "string",
                            "description": "must be a string and is required",
                        },
                    },
                },
                "minItems": 4,
                "maxItems": 6,
            },
        },
    }
}
