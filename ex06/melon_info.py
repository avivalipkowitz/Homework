"""
melon_info.py - Prints out all the melons in our inventory

"""

from melons import melon_name, melon_seedless, melon_price





catalogue = {}
cantaloupe_dict = {}
crenshaw_dict = {}
crane_dict = {}
casaba_dict = {}
honey_dict = {}



melon_name_list = []
melon_seeds_list = []
melon_price_list = []

for k, v in melon_name.iteritems():
	melon_name_list.append(v)


cantaloupe_dict["price"] = [melon_price[1]]
cantaloupe_dict["seedless"] = [melon_seedless[1]]

crenshaw_dict['price'] = [melon_price[2]]
crenshaw_dict["seedless"] = [melon_seedless[2]]

crane_dict['price'] = [melon_price[3]]
crane_dict["seedless"] = [melon_seedless[3]]

casaba_dict['price'] = [melon_price[4]]
casaba_dict["seedless"] = [melon_seedless[4]]

honey_dict['price'] = [melon_price[5]]
honey_dict["seedless"] = [melon_seedless[5]]

catalogue["Cantaloupe"] = cantaloupe_dict
catalogue["Crenshaw"] = crenshaw_dict
catalogue["Crane"] = crane_dict
catalogue['Honeydew'] = honey_dict
catalogue['Casaba'] = casaba_dict



	