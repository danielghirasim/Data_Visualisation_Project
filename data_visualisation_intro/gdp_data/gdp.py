import json
import pygal
from pygal_maps_world.i18n import COUNTRIES
from pygal import style

def get_country_code(country_name):
    for code, country in COUNTRIES.items():
        if country_name == country:
            return code
        elif country_name == 'Yemen, Rep.':
            return 'ye'
    else:
        return None

filepath = 'gdp_json.json'

with open(filepath) as f:
    data = json.load(f)

    desired_year = 2002

    gdp_all, gdp_1, gdp_2, gdp_3 = {}, {}, {}, {}
    faults = {}
    for line in data:
        country_name = line['Country Name']
        gdp_value = line['Value']
        code = get_country_code(country_name)
        if code and line['Year'] == desired_year:
            gdp_all[code] = line['Value']
        if not code:
            faults[country_name] = code

for code, value in gdp_all.items():
    if value <= 1_000_000_000:
        gdp_1[code] = value
    if value > 1_000_000_000 and value < 1_000_000_000_000:
        gdp_2[code] = value
    else:
        gdp_3[code] = value

wm_style = pygal.style.RotateStyle('#996699')
graph = pygal.maps.world.World(style=wm_style)
graph.value_formatter = lambda x: "{:,}".format(x)
graph.add('GDP < 1bn', gdp_1)
graph.add('GDP between 1bn < 100bn ',gdp_2)
graph.add('GDP > 1trillion',gdp_3)
graph.render_to_file('gdp.svg')