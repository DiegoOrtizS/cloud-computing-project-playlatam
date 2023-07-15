import json

from mongodb import Database
from scraping.scraper import Scraper


# pylint: disable=broad-exception-caught
def handler(event: dict, _context) -> dict:
    """
    Handler aws lambda function to run the scraper.

    Args:
        event (dict): Event from aws lambda.

    Returns:
        dict: Response from aws lambda with status code and body.
    """
    body: dict = json.loads(event.get("body"))
    tournament_id: str | None = body.get("tournament_id")
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
        download_success: bool = Scraper(tournament_id, True).main()
        if download_success:
            http_res["statusCode"] = 201
            res_body["message"] = "Created"
            http_res["body"] = json.dumps(res_body)
            return http_res
        http_res["statusCode"] = 409
        res_body["message"] = f"Tournament with {tournament_id} already on db"
        http_res["body"] = json.dumps(res_body)
        return http_res
    except Exception as e:
        http_res["statusCode"] = 500
        res_body["message"] = f"An error occurred: {str(e)}"
        http_res["body"] = json.dumps(res_body)
        return http_res
