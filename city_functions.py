# City Function
""" print city & Country """
def city_country(city,country,population=''):
    if population:
        return (city + ', ' + country + ' - ' + population)
    else:
        return (city + ', ' + country)
