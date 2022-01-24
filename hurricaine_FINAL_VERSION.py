from collections import OrderedDict

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# updated damages where the recorded data is converted to float values and the missing data is retained as "Damages not recorded".
def UpdatedDamages(lst):

    global updated_damages

    updated_damages = [(float(word[:-1])*conversion["M"]) if word[-1] == "M" else ((float(word[:-1])*conversion["B"]) if word[-1] == "B" else word[:]) for word in damages]
    
    return updated_damages

UpdatedDamages(damages)
# print(updated_damages)
# 2 
# Create a Table

# Create and view the hurricanes dictionary
def GenerateHurricainDict(names_list, 
                          months_list, 
                          years_list, 
                          max_sustained_winds_list, 
                          areas_affected_list, 
                          damages_list, 
                          deaths_list):
                          
    global hurricain_dictionary

    hurricain_dictionary = {}

    for index in range(len(names_list)):
      hurricain_dictionary[names_list[index]] = {
        "Name": names_list[index],
        "Month": months_list[index],
        "Year": years_list[index],
        "Max Sustained Wind": max_sustained_winds_list[index],
        "Areas Affected": areas_affected_list[index],
        "Damage": damages_list[index],
        "Deaths": deaths_list[index]
        }

    return hurricain_dictionary


hurricain_data = GenerateHurricainDict(names, 
                                       months, 
                                       years, 
                                       max_sustained_winds, 
                                       areas_affected, 
                                       updated_damages, 
                                       deaths)

print("-" * 30)
print("Here is the hurricain data:\n")
print(hurricain_data)
print("-" * 30)

# 3
# Organizing by Year
# create a new dictionary of hurricanes with year and key
def SetHurricainDictionaryByYear(hurricain_dictionary):
    
    # year_hurricain_dictionary = hurricain_dictionary.copy()
    year_hurricain_dictionary = {}

    for key, value in hurricain_dictionary.items():
        year = hurricain_dictionary[key]["Year"]
        if not year_hurricain_dictionary.get(year):
            year_hurricain_dictionary[year] = [value]
        else:
            year_hurricain_dictionary[year].append(value)

    return year_hurricain_dictionary


hurricain_data_by_year = SetHurricainDictionaryByYear(hurricain_data)

print("-" * 30)
print("Here is the hurricain data by YEAR:\n")
print(hurricain_data_by_year)
print("-" * 30)

# 4
# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in
def CountAffectedAreas(areas_affected):

    new_list = [val for sublist in areas_affected for val in sublist]

    global affected_areas_Dictionary_count

    affected_areas_Dictionary_count = {i:new_list.count(i) for i in new_list}

    return affected_areas_Dictionary_count


total_count_of_areas_affected = CountAffectedAreas(areas_affected)

print("-" * 30)
print("Here are the number of hurricains in each area affected:\n")
print(total_count_of_areas_affected)
print("-" * 30)

# 5 
# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in
def MaxHurricains(affected_areas_Dictionary_count):
    
    most_affected_key = max(zip(affected_areas_Dictionary_count.values(),affected_areas_Dictionary_count.keys()))[1]

    most_affected_value = affected_areas_Dictionary_count.get(most_affected_key, "Sorry cannot find key!")

    return f"The area most affected by hurricains is {most_affected_key} hit by a total of {most_affected_value} times."

most_hurricaines = MaxHurricains( affected_areas_Dictionary_count)

print("-" * 30)
print("MOST AFFECTED AREAS:\n")
print(most_hurricaines)
print("-" * 30)

# 6
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths
def GreatestNumberOfDeaths(hurricain_dictionary):

    hurricane = "Cuba I"
    max_deaths_count = 0

    for key, value in hurricain_dictionary.items():
        if value["Deaths"] > max_deaths_count:
            max_deaths_count = value['Deaths']
            hurricane = key
    
    return f"The hurricaine with the greatest death count is {hurricane} with a total of {max_deaths_count} deaths."


greatest_deaths = GreatestNumberOfDeaths(hurricain_dictionary)

print("-" * 30)
print("Greatest number of deaths:\n")
print(greatest_deaths)
print("-" * 30)

# 7
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key
def RateHurricaineDeathRate(hurricain_dictionary):
    
    mortality_scale = {}

    for value in hurricain_dictionary.values():
      if value["Deaths"]  == 0:
          mortality_scale.update({0:value["Name"]})
      if value["Deaths"] > 0 and value["Deaths"] <= 100:
          mortality_scale.update({1:value["Name"]})
      elif value["Deaths"] > 100 and value["Deaths"] <= 500:
          mortality_scale.update({2:value["Name"]})
      elif value["Deaths"] > 500 and value["Deaths"] <= 1000:
          mortality_scale.update({3:value["Name"]})
      elif value["Deaths"] > 1000 and value["Deaths"] <= 10000:
          mortality_scale.update({4:value["Name"]})

    ordered_mortality_scale = OrderedDict(sorted(mortality_scale.items()))

    ordered_mortality_scale = dict(ordered_mortality_scale)

    return ordered_mortality_scale


hurricaine_mortality_scale = RateHurricaineDeathRate(hurricain_dictionary)

print("-" * 30)
print("Hurricaine mortality scale rate:\n")
print("""mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}\n""")
print(hurricaine_mortality_scale)
print("-" * 30)

# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost
def HighestDamageAndCost(hurricain_dictionary):
    
    max_damage_cost = 0
    
    hurricaine = ""
    
    for key, value in hurricain_dictionary.items():
        if value["Damage"] != "Damages not recorded":
              if value["Damage"] > max_damage_cost:
                  max_damage_cost = value['Damage']
                  key = hurricaine

    return f"The hurraine that caused the most damage is '{key}' at a cost of {max_damage_cost}"


maximum_damage_from_hurricaine = HighestDamageAndCost(hurricain_dictionary)

print("-" * 30)
print("MOST DAMAGE FROM HURRICAINE:\n")
print(maximum_damage_from_hurricaine)
print("-" * 30)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def HurricaineDamageRate(hurricain_dictionary):

    hurricaine_damage_rate = {}
    list_0 = []
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    
    for value in hurricain_dictionary.values():
          if value["Damage"] != "Damages not recorded":
            if value["Damage"] == 0:
                hurricaine_damage_rate.update({0:sorted(list(zip(list_0, names)), reverse=True)})
            elif value["Damage"] >= 100000000 and value["Damage"] <= 1000000000:
                list_1.append(value["Damage"])
                hurricaine_damage_rate.update({1:sorted(list(zip(list_1, names)), reverse=True)})
            elif value["Damage"] >= 1000000000 and value["Damage"] <= 10000000000:
                list_2.append(value["Damage"])
                hurricaine_damage_rate.update({2:sorted(list(zip(list_2, names)), reverse=True)})
            elif value["Damage"] >= 10000000000 and value["Damage"] <= 50000000000:
                list_3.append(value["Damage"])
                hurricaine_damage_rate.update({3:sorted(list(zip(list_3, names)), reverse=True)})
            elif value["Damage"] > 50000000000:
                list_4.append(value["Damage"])
                hurricaine_damage_rate.update({4:sorted(list(zip(list_4, names)), reverse=True)})

    # ordered_damage_scale = OrderedDict(sorted(hurricaine_damage_rate.items()))

    # ordered_damage_scale = dict(ordered_damage_scale)

    return hurricaine_damage_rate


hurricaine_damage_scale = HurricaineDamageRate(hurricain_dictionary)

print("-" * 30)
print("Hurricaine cost of damage scale rate:\n")
print("""damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}\n""")
print(hurricaine_damage_scale)
print("-" * 30)

# ------------ END OF FLE -------------------