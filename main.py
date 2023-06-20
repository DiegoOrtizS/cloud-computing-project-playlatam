import os
import sys

from src.scraping.scraper import scraper


def main() -> None:
    """
    Execute the scraper function from src/scraping//scraper.py
    """
    src_path = os.path.abspath("src")
    sys.path.append(src_path)
    scraper()


if __name__ == "__main__":
    main()
