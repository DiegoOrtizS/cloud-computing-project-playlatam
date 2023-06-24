from mongodb.config import Database
from scraping.scraper import Scraper


def main() -> None:
    """
    Execute the scraper function
    """
    Database.initialize()
    Scraper(tournament_id="8ozUQU").main()


if __name__ == "__main__":
    main()
