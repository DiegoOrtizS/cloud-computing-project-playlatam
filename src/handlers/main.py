from scraping.scraper import Scraper


def handler(event, _context) -> dict:
    Scraper(event["tournament_id"]).main()
    return {"statusCode": 200, "body": "OK"}
