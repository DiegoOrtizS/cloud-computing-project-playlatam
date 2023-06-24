from mongodb import Database
from scraping.scraper import Scraper


def handler(event: dict, _context) -> dict:
    """
    Handler aws lambda function to run the scraper.

    Args:
        event (dict): Event from aws lambda.
        _context (LambdaContext): Context from aws lambda.

    Returns:
        dict: Response from aws lambda with status code and body.
    """
    tournament_id: str | None = event.get("tournament_id")
    if tournament_id is None:
        return {"statusCode": 400, "body": "Missing tournament_id"}

    try:
        Database.initialize()
        download_success: bool = Scraper(tournament_id, True).main()
        if download_success:
            return {"statusCode": 200, "body": "OK"}
        return {
            "statusCode": 409,
            "body": f"Tournament with {tournament_id} already on db",
        }
    except Exception as e:
        return {"statusCode": 500, "body": f"An error occurred: {str(e)}"}
