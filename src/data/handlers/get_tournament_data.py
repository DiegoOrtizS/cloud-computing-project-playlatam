import json
from datetime import datetime

from mongodb import Database


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


# pylint: disable=broad-exception-caught
def handler(event: dict, _context) -> dict:
    """
    Handler aws lambda function to get tournament data.

    Args:
        event (dict): Event from aws lambda.

    Returns:
        dict: Response from aws lambda with status code and body.
    """
    tournament_id: str = event["queryStringParameters"]["tournament_id"]
    res_body: dict = {}
    http_res: dict = {}
    http_res["headers"] = {}
    http_res["headers"]["Content-Type"] = "application/json"
    if tournament_id is None:
        http_res["statusCode"] = 400
        res_body["message"] = "Missing tournament_id"
        http_res["body"] = json.dumps(res_body)
        return http_res
    try:
        Database.initialize()
        tournament: dict | None = Database.find_one(
            "tournament", {"_id": tournament_id}
        )
        if tournament is None:
            http_res["statusCode"] = 404
            res_body["message"] = f"Tournament with {tournament_id} not found"
            http_res["body"] = json.dumps(res_body)
            return http_res
        http_res["statusCode"] = 200
        http_res["body"] = json.dumps(tournament, cls=DateTimeEncoder)
        return http_res
    except Exception as e:
        http_res["statusCode"] = 500
        res_body["message"] = f"An error occurred: {str(e)}"
        http_res["body"] = json.dumps(res_body)
        return http_res
