from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pokemon import Pokemon

tournament_id = "XYz2IB"
pokemon = []

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://pairings.playlatam.net/roster/" + tournament_id
driver.get(url)

header_element = driver.find_element_by_xpath("//h2[text()='Master Division']")
table_element = header_element.find_element_by_xpath("./following-sibling::table[1]")
tr_elements = table_element.find_elements_by_xpath(".//tr[position() > 1]")

href_list = []

# Collect the href values first to avoid stale element reference
for tr_element in tr_elements:
    td_element = tr_element.find_elements_by_tag_name("td")[2]
    a_element = td_element.find_element_by_tag_name("a")
    href = a_element.get_attribute("href")
    href_list.append(href)

for href in href_list:
    driver.get(href)
    a_element = driver.find_element_by_xpath('//a[normalize-space(@onclick)="translateTeam(\'ENG\')"]')
    a_element.click()
    
    li_elements = driver.find_elements_by_xpath("//li[contains(@class, 'collection-item')]")

    for i in range(3, len(li_elements)):
        name = li_elements[i].find_element_by_xpath(f".//span[@id='p{i-2}-name-s']").get_attribute("innerHTML")
        tera_type = li_elements[i].find_element_by_xpath(f".//img[@id='p{i-2}-teratype-icon-s']").get_attribute("alt")
        ability = li_elements[i].find_element_by_xpath(f".//span[@id='p{i-2}-ability-s']").get_attribute("innerHTML")
        item = li_elements[i].find_element_by_xpath(f".//span[@id='p{i-2}-item-s']").get_attribute("innerHTML")
        move1 = li_elements[i].find_element_by_xpath(f".//span[@id='p{i-2}-m1-s']").get_attribute("innerHTML")
        move2 = li_elements[i].find_element_by_xpath(f".//span[@id='p{i-2}-m2-s']").get_attribute("innerHTML")
        move3 = li_elements[i].find_element_by_xpath(f".//span[@id='p{i-2}-m3-s']").get_attribute("innerHTML")
        move4 = li_elements[i].find_element_by_xpath(f".//span[@id='p{i-2}-m4-s']").get_attribute("innerHTML")
        pokemon.append(Pokemon(name, tera_type, ability, item, move1, move2, move3, move4))

    driver.get(url)

print(pokemon)
driver.quit()
