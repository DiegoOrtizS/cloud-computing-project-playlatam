tournament_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": [
            "_id",
            "category",
            "type",
            "name",
            "country",
            "region",
            "address",
            "date",
        ],
        "properties": {
            "_id": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "category": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "type": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "name": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "country": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "region": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "address": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "date": {
                "bsonType": "date",
                "description": "must be a date and is required",
            },
        },
    }
}
