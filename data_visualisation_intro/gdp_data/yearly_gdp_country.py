import json
import pygal

file = 'gdp_json.json'

with open(file) as f:
    data = json.load(f)

def get_gdp_by_country(country_name):
    gdp_values= []
    gdp_year = []
    for line in data:
        if line['Country Name'] == country_name:
            gdp_value = int(float(line['Value']))
            year = int(line['Year'])
            gdp_values.append(gdp_value)
            gdp_year.append(year)
    return gdp_values, gdp_year



selected_country = 'Germany'
gdp_values, gdp_year = get_gdp_by_country(selected_country)

graph = pygal.Line()
graph.title = f"Yearly GDP evolution of {selected_country}"
graph.value_formatter = lambda y: "{:,}".format(y)
graph.x_labels = gdp_year
graph.add('GDP',gdp_values)
graph.render_to_file('romania_gdp.svg')