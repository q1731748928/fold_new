from DrissionPage import ChromiumPage, ChromiumOptions

driver = ChromiumPage()
base_url = "https://gleami.apps.fao.org/"
tab = driver.get(base_url)
# 选择下拉框，并选择第二个选项
driver.ele('x://select[@id="region_selection"]').ele('x:./option[2]').click()
driver.ele('x://select[@id="country_selection"]').ele('x:./option[2]').click()
driver.ele('x://*[@id="zoneform"]/button').click()
animals_selection = base_url + "animals_selection"
driver.get(animals_selection)
print(driver.html)
labels = driver.ele('x://li[@class="nobullet"]//label')
