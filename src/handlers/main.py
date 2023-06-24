from mongodb import Database
from scraping.scraper import Scraper


def handler(event, _context) -> dict:
    Database.initialize()
    Scraper(True, event["tournament_id"]).main()
    return {"statusCode": 200, "body": "OK"}
