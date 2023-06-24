import os
import sys


def main() -> None:
    """
    Execute the scraper function
    """
    src_path = os.path.abspath("src")
    sys.path.append(src_path)

    from mongodb.config import Database
    from scraping.scraper import Scraper

    Database.initialize()
    Scraper(tournament_id="8ozUQU").main()


if __name__ == "__main__":
    main()
