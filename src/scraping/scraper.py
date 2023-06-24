from datetime import datetime

from bson.objectid import ObjectId
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from mongodb.config import Database
from utils.constants import MONTHS, TOURNAMENTS_ROSTER_URI


class Scraper:
    """
    Scraper class to scrape data from the PlayLatam website.
    """

    def __init__(self, deploy: bool = False, tournament_id: str = "XYz2IB") -> None:
        self.tournament_id: str = tournament_id
        options: Options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--single-process")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-dev-tools")
        options.add_argument("--no-zygote")
        self.driver: WebDriver
        if deploy:
            options.binary_location = "/opt/chrome/chrome"
            service = Service("/opt/chromedriver")
            self.driver = webdriver.Chrome(service=service, options=options)
        else:
            self.driver = webdriver.Chrome(options=options)
        self.url: str = TOURNAMENTS_ROSTER_URI + self.tournament_id

    def scrap_and_insert_tournament_data(self) -> None:
        """
        Scrapes and inserts the tournament data into the database.
        """
        self.driver.get(self.url)

        category: str = self.driver.find_element(By.TAG_NAME, "h1").text
        tournament_type: str = self.driver.find_element(By.TAG_NAME, "h2").text

        collection_items: list[str] = self.driver.execute_script(
            """
            var items = document.getElementsByClassName('collection-item');
            var modifiedTexts = [];
            for (var i = 0; i < items.length; i++) {
                var text = items[i].textContent.trim()
                modifiedTexts.push(text.substring(text.indexOf(' ') + 1).trim());
            }
            return modifiedTexts;
        """
        )
        name: str = collection_items[0]
        country_and_region: list[str] = collection_items[1].split(",  ")
        country: str = country_and_region[0]
        region: str = country_and_region[1]
        address: str = collection_items[2]
        date: str = collection_items[3]
        date = date.replace("de ", "")
        day, month_name, year = date.split(" ")
        month = MONTHS[month_name]
        date = f"{year}-{month}-{day}"
        Database.insert_one(
            "tournament",
            {
                "_id": self.tournament_id,
                "category": category,
                "type": tournament_type,
                "name": name,
                "country": country,
                "region": region,
                "address": address,
                "date": datetime.strptime(date, "%Y-%m-%d"),
            },
        )

    def scrap_and_insert_pokemon_data(self) -> None:
        """
        Scrapes and inserts the pokemon data into the database.
        """
        self.driver.get(self.url)

        header_element: WebElement = self.driver.find_element(
            "xpath", "//h2[text()='Master Division']"
        )
        table_element: WebElement = header_element.find_element(
            "xpath", "./following-sibling::table[1]"
        )
        tr_elements: list[WebElement] = table_element.find_elements(
            "xpath", ".//tr[position() > 1]"
        )

        href_list: list[str] = []

        # Collect the href values first to avoid stale element reference
        for tr_element in tr_elements:
            td_element: WebElement = tr_element.find_elements(By.TAG_NAME, "td")[2]
            try:
                a_element: WebElement = td_element.find_element(By.TAG_NAME, "a")
                href: str = a_element.get_attribute("href")
                href_list.append(href)
            except Exception:
                pass

        for href in href_list:
            self.driver.get(href)
            a_element: WebElement = self.driver.find_element(
                "xpath", "//a[normalize-space(@onclick)=\"translateTeam('ENG')\"]"
            )
            a_element.click()

            li_elements: list[WebElement] = self.driver.find_elements(
                "xpath", "//li[contains(@class, 'collection-item')]"
            )

            team_pokemon_list: list[dict] = []

            for i in range(3, len(li_elements)):
                name: str | None = (
                    li_elements[i]
                    .find_element("xpath", f".//span[@id='p{i-2}-name-s']")
                    .get_attribute("innerHTML")
                    or None
                )
                tera_type: str | None = (
                    li_elements[i]
                    .find_element("xpath", f".//img[@id='p{i-2}-teratype-icon-s']")
                    .get_attribute("alt")
                    or None
                )
                ability: str | None = (
                    li_elements[i]
                    .find_element("xpath", f".//span[@id='p{i-2}-ability-s']")
                    .get_attribute("innerHTML")
                    or None
                )
                item: str | None = (
                    li_elements[i]
                    .find_element("xpath", f".//span[@id='p{i-2}-item-s']")
                    .get_attribute("innerHTML")
                    or None
                )
                move1: str | None = (
                    li_elements[i]
                    .find_element("xpath", f".//span[@id='p{i-2}-m1-s']")
                    .get_attribute("innerHTML")
                    or None
                )
                move2: str | None = (
                    li_elements[i]
                    .find_element("xpath", f".//span[@id='p{i-2}-m2-s']")
                    .get_attribute("innerHTML")
                    or None
                )
                move3: str | None = (
                    li_elements[i]
                    .find_element("xpath", f".//span[@id='p{i-2}-m3-s']")
                    .get_attribute("innerHTML")
                    or None
                )
                move4: str | None = (
                    li_elements[i]
                    .find_element("xpath", f".//span[@id='p{i-2}-m4-s']")
                    .get_attribute("innerHTML")
                    or None
                )

                if (
                    name is not None
                    and tera_type is not None
                    and ability is not None
                    and move1 is not None
                ):
                    team_pokemon_list.append(
                        {
                            "_id": ObjectId(),
                            "name": name,
                            "tera_type": tera_type,
                            "ability": ability,
                            "item": item,
                            "move1": move1,
                            "move2": move2,
                            "move3": move3,
                            "move4": move4,
                        }
                    )

            Database.insert_many("pokemon", team_pokemon_list)
            Database.insert_one(
                "team",
                {
                    "_id": ObjectId(),
                    "tournament_id": self.tournament_id,
                    "pokemon": [
                        {
                            "_id": pokemon["_id"],
                            "name": pokemon["name"],
                        }
                        for pokemon in team_pokemon_list
                    ],
                },
            )
            self.driver.get(self.url)

    def main(self) -> None:
        """
        Main method to run the scraper.
        """
        tournament: dict | None = Database.find_one(
            "tournament", {"_id": self.tournament_id}
        )

        if tournament is None:
            self.scrap_and_insert_tournament_data()
            self.scrap_and_insert_pokemon_data()
            self.driver.quit()
