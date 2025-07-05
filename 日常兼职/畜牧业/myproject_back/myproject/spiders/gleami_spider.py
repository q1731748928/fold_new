import scrapy
import json
import re

from scrapy import cmdline
from scrapy_splash import SplashRequest

class GleamiItem(scrapy.Item):
    area = scrapy.Field()
    country = scrapy.Field()
    species = scrapy.Field()
    herd = scrapy.Field() # For Herd characteristics data
    feed = scrapy.Field() # For Feed Rations data
    manure = scrapy.Field() # For Manure Management data

class GleamiSpider(scrapy.Spider):
    name = 'gleami_spider'
    allowed_domains = ['gleami.org', 'gleami.apps.fao.org']
    start_urls = ['https://gleami.apps.fao.org/']

    def start_requests(self):
        script = """
        function main(splash, args)
          splash.wait(1) -- Increased initial wait time
          local element = splash.select('#nextBtn')
          if element then
            splash.wait(5) -- Wait for the page to fully render after the element is found
          else
            splash.wait(10) -- Fallback wait if element not found
          end
          return {
            html = splash.html(),
            png = splash.png(),
            har = splash.har(),
          }
        end
        """
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='execute', args={'lua_source': script})

    def parse(self, response):
        # Extract allinput_data from the script tag
        script_data = response.xpath("//script[contains(., 'var allinput_data =')]/text()").get()

        if script_data:
            # Use regex to extract the JSON part
            json_match = re.search(r"var allinput_data = (\[.*?\]);", script_data, re.S)

            if json_match:
                json_string = json_match.group(1)
                try:
                    allinput_data = json.loads(json_string)
                    self.logger.info(f"Successfully loaded {len(allinput_data)} entries from allinput_data.")

                    # Extract species_names for lookup
                    species_script_data = response.xpath("//script[contains(., 'var species_names =')]/text()").get()
                    species_names = {}
                    if species_script_data:
                         species_match = re.search(r"var species_names = ({.*?});", species_script_data, re.S)
                         if species_match:
                             species_json_string = species_match.group(1)
                             try:
                                 species_names = json.loads(species_json_string)
                                 self.logger.info(f"Successfully loaded {len(species_names)} species names.")
                             except json.JSONDecodeError:
                                 self.logger.error("Could not decode species_names JSON")

                    # Extract page_location
                    page_location = {}
                    location_script_data = response.xpath("//script[contains(., 'var page_location =')]/text()").get()
                    if location_script_data:
                        location_match = re.search(r"var page_location = ({.*?});", location_script_data, re.S)
                        if location_match:
                            location_json_string = location_match.group(1)
                            try:
                                page_location = json.loads(location_json_string)
                                self.logger.info(f"Successfully loaded page_location.")
                            except json.JSONDecodeError:
                                self.logger.error("Could not decode page_location JSON")

                    # Create a single item for the entire page's data
                    gleami_item = GleamiItem()
                    gleami_item['area'] = page_location.get('area', 'N/A')
                    gleami_item['country'] = page_location.get('country', 'N/A')
                    gleami_item['species'] = 'N/A' # Will be set based on the first relevant entry

                    gleami_item['herd'] = []
                    gleami_item['feed'] = []
                    gleami_item['manure'] = []

                    # Process each entry in allinput_data
                    for entry in allinput_data:
                        entry_code = entry.get('code')
                        module_data = {
                            'parameter_name': entry.get('name'),
                            'code': entry_code,
                            'unit': entry.get('unit'),
                            'production_system': entry.get('production_system'),
                            'orientation': entry.get('orientation'),
                            'default_value': entry.get('str_value'),
                            'scenarios': {} # Dictionary to hold scenario values
                        }

                        # Dynamically capture scenario values (keys are numbers)
                        for key, value in entry.items():
                            if isinstance(key, str) and key.isdigit():
                                module_data['scenarios'][key] = value

                        category = entry.get('category')
                        species_id = entry.get('species_id')

                        # Set species name for the main item based on the first entry that has it
                        if 'species' in species_names and species_id is not None and gleami_item['species'] == 'N/A':
                             gleami_item['species'] = species_names.get(str(species_id), f'Unknown Species ID: {species_id}')


                        if category == 'Herd characteristics':
                            gleami_item['herd'].append(module_data)
                        elif category == 'Feed rations':
                            # Add feed-specific fields
                            module_data['feedgroup'] = entry.get('feedgroup')
                            module_data['feedtype'] = entry.get('feedtype')
                            gleami_item['feed'].append(module_data)
                        elif category == 'Manure management':
                            # Add manure-specific fields
                            module_data['manure_management'] = entry.get('manuremanagement')
                            module_data['manure_system'] = entry.get('manuresystem') # Added manure system extraction
                            gleami_item['manure'].append(module_data)
                        # Add other categories if needed
                        # else:
                        #     self.logger.warning(f"Unknown category: {category} for entry code {entry_code}")


                    yield gleami_item # Yield the single item containing all data

                except json.JSONDecodeError:
                    self.logger.error("Could not decode allinput_data JSON from script tag.")
            else:
                self.logger.error("Could not find 'var allinput_data = [...]' in the script tag.")
        else:
            self.logger.info(f"Could not find script tag containing 'var allinput_data ='. Saving response to file.")
            with open('response_body.html', 'w', encoding='utf-8') as f:
                f.write(response.text)
            self.logger.error("Could not find script tag containing 'var allinput_data ='. Response saved to response_body.html")

if __name__ == '__main__':
    cmdline.execute('scrapy crawl gleami_spider'.split())
