import os
import sys

from src.mongodb.config import Database
from src.scraping.scraper import Scraper


def main() -> None:
    """
    Execute the scraper function from src/scraping//scraper.py
    """
    Database.initialize()
    src_path = os.path.abspath("src")
    sys.path.append(src_path)
    Scraper().main()


if __name__ == "__main__":
    main()
