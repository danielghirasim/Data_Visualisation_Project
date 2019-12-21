import json
from data_visualisation_intro.mapping_global_data_sets.country_codes import get_country_code
import pygal
from pygal.style import LightColorizedStyle

filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

# Print 2010 population for each country.

# Build a dictionary of population data.
cc_populations = {}
my_year = '2010'
for pop_dict in pop_data:
    if pop_dict['Year'] == my_year:
        population = int(float(pop_dict['Value']))
        country = pop_dict['Country Name']
        code = get_country_code(pop_dict["Country Name"])
        if code:
            cc_populations[code] = population

# Group the countries into 3 population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    if pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# See how many countries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = LightColorizedStyle
wm = pygal.maps.world.World(style=wm_style)
wm.title = f'World Population in {my_year}, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_to_file('world_population_2010.svg')
