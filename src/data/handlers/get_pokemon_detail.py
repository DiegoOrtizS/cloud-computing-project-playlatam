import json

from mongodb import Database


def handler(event: dict, _context) -> dict:
    """
    Handler aws lambda function to get pokemon detail from _id

    Args:
        event (dict): Event from aws lambda.

    Returns:
        dict: Response from aws lambda with status code and body.
    """
    pokemon_name: str = event["queryStringParameters"]["pokemon_name"]
    tournament_id: str = event["queryStringParameters"]["tournament_id"]
    res_body: dict = {}
    http_res: dict = {}
    http_res["headers"] = {}
    http_res["headers"]["Content-Type"] = "application/json"
    if pokemon_name is None:
        http_res["statusCode"] = 400
        res_body["message"] = "Missing pokemon_name"
        http_res["body"] = json.dumps(res_body)
        return http_res
    if tournament_id is None:
        http_res["statusCode"] = 400
        res_body["message"] = "Missing tournament_id"
        http_res["body"] = json.dumps(res_body)
        return http_res
    try:
        Database.initialize()
        pokemon_list: list[dict] = Database.get_pokemon_detail(
            pokemon_name, tournament_id
        )
        http_res["statusCode"] = 200
        res_body["pokemon"] = pokemon_list
        http_res["body"] = json.dumps(res_body)
        return http_res
    except Exception as e:
        http_res["statusCode"] = 500
        res_body["message"] = f"An error occurred: {str(e)}"
        http_res["body"] = json.dumps(res_body)
        return http_res
