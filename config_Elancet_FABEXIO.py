import os
from pathlib import Path

# FABIO v2
fabio_filepath = Path(
    "/your/local/path/to/fabio_v2_beta"
)

# FABIO v1.2 mass and calorie data
fabio_masskcal_path = Path(
    "/your/local/path/to/fabio_v1.2"
)

calories_path = fabio_masskcal_path / "calories"
biomass_path = fabio_masskcal_path / "biomass"


# EXIOBASE
exiobase_path = Path(
    "/your/local/path/to/EXIOBASE_3_8_2"
)

start_year = 1995
end_year = 2020



extracted_sectors = (  
    [  # Agriculture products 
        'Paddy rice',
        'Wheat',
        'Cereal grains nec',
        'Vegetables, fruit, nuts',
        'Oil seeds',
        'Sugar cane, sugar beet',
        'Plant-based fibers',
        'Crops nec',
        'Cattle',
        'Pigs',
        'Poultry',
        'Meat animals nec',
        'Animal products nec',
        'Raw milk',
        'Fish and other fishing products; services incidental of fishing (05)',
    ]
    + 
    [  # Food processing
        'Products of meat cattle',
        'Products of meat pigs',
        'Products of meat poultry',
        'Meat products nec',
        'products of Vegetable oils and fats',
        'Dairy products',
        'Processed rice',
        'Sugar',
        'Food products nec',
        'Beverages',
        'Fish products',
        #'Tobacco products (16)',
    ]
)



# Hybrid-model settings
EXIOBASE_sectors = [
    'Paddy rice',
    'Wheat',
    'Cereal grains nec',
    'Vegetables, fruit, nuts',
    'Oil seeds',
    'Sugar cane, sugar beet',
    'Plant-based fibers',
    'Crops nec',
    'Cattle',
    'Pigs',
    'Poultry',
    'Meat animals nec',
    'Animal products nec',
    'Raw milk',
    'Wool, silk-worm cocoons',
    'Manure (conventional treatment)',
    'Manure (biogas treatment)',
    'Products of forestry, logging and related services (02)',
    'Fish and other fishing products; services incidental of fishing (05)',
    'Anthracite',
    'Coking Coal',
    'Other Bituminous Coal',
    'Sub-Bituminous Coal',
    'Patent Fuel',
    'Lignite/Brown Coal',
    'BKB/Peat Briquettes',
    'Peat',
    'Crude petroleum and services related to crude oil extraction, excluding surveying',
    'Natural gas and services related to natural gas extraction, excluding surveying',
    'Natural Gas Liquids',
    'Other Hydrocarbons',
    'Uranium and thorium ores (12)',
    'Iron ores',
    'Copper ores and concentrates',
    'Nickel ores and concentrates',
    'Aluminium ores and concentrates',
    'Precious metal ores and concentrates',
    'Lead, zinc and tin ores and concentrates',
    'Other non-ferrous metal ores and concentrates',
    'Stone',
    'Sand and clay',
    'Chemical and fertilizer minerals, salt and other mining and quarrying products n.e.c.',
    'Products of meat cattle',
    'Products of meat pigs',
    'Products of meat poultry',
    'Meat products nec',
    'products of Vegetable oils and fats',
    'Dairy products',
    'Processed rice',
    'Sugar',
    'Food products nec',
    'Beverages',
    'Fish products',
    'Tobacco products (16)',
    'Textiles (17)',
    'Wearing apparel; furs (18)',
    'Leather and leather products (19)',
    'Wood and products of wood and cork (except furniture); articles of straw and plaiting materials (20)',
    'Wood material for treatment, Re-processing of secondary wood material into new wood material',
    'Pulp',
    'Secondary paper for treatment, Re-processing of secondary paper into new pulp',
    'Paper and paper products',
    'Printed matter and recorded media (22)',
    'Coke Oven Coke',
    'Gas Coke',
    'Coal Tar',
    'Motor Gasoline',
    'Aviation Gasoline',
    'Gasoline Type Jet Fuel',
    'Kerosene Type Jet Fuel',
    'Kerosene',
    'Gas/Diesel Oil',
    'Heavy Fuel Oil',
    'Refinery Gas',
    'Liquefied Petroleum Gases (LPG)',
    'Refinery Feedstocks',
    'Ethane',
    'Naphtha',
    'White Spirit & SBP',
    'Lubricants',
    'Bitumen',
    'Paraffin Waxes',
    'Petroleum Coke',
    'Non-specified Petroleum Products',
    'Nuclear fuel',
    'Plastics, basic',
    'Secondary plastic for treatment, Re-processing of secondary plastic into new plastic',
    'N-fertiliser',
    'P- and other fertiliser',
    'Chemicals nec',
    'Charcoal',
    'Additives/Blending Components',
    'Biogasoline',
    'Biodiesels',
    'Other Liquid Biofuels',
    'Rubber and plastic products (25)',
    'Glass and glass products',
    'Secondary glass for treatment, Re-processing of secondary glass into new glass',
    'Ceramic goods',
    'Bricks, tiles and construction products, in baked clay',
    'Cement, lime and plaster',
    'Ash for treatment, Re-processing of ash into clinker',
    'Other non-metallic mineral products',
    'Basic iron and steel and of ferro-alloys and first products thereof',
    'Secondary steel for treatment, Re-processing of secondary steel into new steel',
    'Precious metals',
    'Secondary preciuos metals for treatment, Re-processing of secondary preciuos metals into new preciuos metals',
    'Aluminium and aluminium products',
    'Secondary aluminium for treatment, Re-processing of secondary aluminium into new aluminium',
    'Lead, zinc and tin and products thereof',
    'Secondary lead for treatment, Re-processing of secondary lead into new lead',
    'Copper products',
    'Secondary copper for treatment, Re-processing of secondary copper into new copper',
    'Other non-ferrous metal products',
    'Secondary other non-ferrous metals for treatment, Re-processing of secondary other non-ferrous metals into new other non-ferrous metals',
    'Foundry work services',
    'Fabricated metal products, except machinery and equipment (28)',
    'Machinery and equipment n.e.c. (29)',
    'Office machinery and computers (30)',
    'Electrical machinery and apparatus n.e.c. (31)',
    'Radio, television and communication equipment and apparatus (32)',
    'Medical, precision and optical instruments, watches and clocks (33)',
    'Motor vehicles, trailers and semi-trailers (34)',
    'Other transport equipment (35)',
    'Furniture; other manufactured goods n.e.c. (36)',
    'Secondary raw materials',
    'Bottles for treatment, Recycling of bottles by direct reuse',
    'Electricity by coal',
    'Electricity by gas',
    'Electricity by nuclear',
    'Electricity by hydro',
    'Electricity by wind',
    'Electricity by petroleum and other oil derivatives',
    'Electricity by biomass and waste',
    'Electricity by solar photovoltaic',
    'Electricity by solar thermal',
    'Electricity by tide, wave, ocean',
    'Electricity by Geothermal',
    'Electricity nec',
    'Transmission services of electricity',
    'Distribution and trade services of electricity',
    'Coke oven gas',
    'Blast Furnace Gas',
    'Oxygen Steel Furnace Gas',
    'Gas Works Gas',
    'Biogas',
    'Distribution services of gaseous fuels through mains',
    'Steam and hot water supply services',
    'Collected and purified water, distribution services of water (41)',
    'Construction work (45)',
    'Secondary construction material for treatment, Re-processing of secondary construction material into aggregates',
    'Sale, maintenance, repair of motor vehicles, motor vehicles parts, motorcycles, motor cycles parts and accessoiries',
    'Retail trade services of motor fuel',
    'Wholesale trade and commission trade services, except of motor vehicles and motorcycles (51)',
    'Retail  trade services, except of motor vehicles and motorcycles; repair services of personal and household goods (52)',
    'Hotel and restaurant services (55)',
    'Railway transportation services',
    'Other land transportation services',
    'Transportation services via pipelines',
    'Sea and coastal water transportation services',
    'Inland water transportation services',
    'Air transport services (62)',
    'Supporting and auxiliary transport services; travel agency services (63)',
    'Post and telecommunication services (64)',
    'Financial intermediation services, except insurance and pension funding services (65)',
    'Insurance and pension funding services, except compulsory social security services (66)',
    'Services auxiliary to financial intermediation (67)',
    'Real estate services (70)',
    'Renting services of machinery and equipment without operator and of personal and household goods (71)',
    'Computer and related services (72)',
    'Research and development services (73)',
    'Other business services (74)',
    'Public administration and defence services; compulsory social security services (75)',
    'Education services (80)',
    'Health and social work services (85)',
    'Food waste for treatment: incineration',
    'Paper waste for treatment: incineration',
    'Plastic waste for treatment: incineration',
    'Intert/metal waste for treatment: incineration',
    'Textiles waste for treatment: incineration',
    'Wood waste for treatment: incineration',
    'Oil/hazardous waste for treatment: incineration',
    'Food waste for treatment: biogasification and land application',
    'Paper waste for treatment: biogasification and land application',
    'Sewage sludge for treatment: biogasification and land application',
    'Food waste for treatment: composting and land application',
    'Paper and wood waste for treatment: composting and land application',
    'Food waste for treatment: waste water treatment',
    'Other waste for treatment: waste water treatment',
    'Food waste for treatment: landfill',
    'Paper for treatment: landfill',
    'Plastic waste for treatment: landfill',
    'Inert/metal/hazardous waste for treatment: landfill',
    'Textiles waste for treatment: landfill',
    'Wood waste for treatment: landfill',
    'Membership organisation services n.e.c. (91)',
    'Recreational, cultural and sporting services (92)',
    'Other services (93)',
    'Private households with employed persons (95)',
    'Extra-territorial organizations and bodies'
]



food_sectors=['Cultivation of paddy rice',
 'Cultivation of wheat',
 'Cultivation of cereal grains nec',
 'Cultivation of vegetables, fruit, nuts',
 'Cultivation of oil seeds',
 'Cultivation of sugar cane, sugar beet',
 'Cultivation of plant-based fibers',
 'Cultivation of crops nec',
 'Cattle farming',
 'Pigs farming',
 'Poultry farming',
 'Meat animals nec',
 'Animal products nec',
 'Raw milk',
'Fishing, operating of fish hatcheries and fish farms; service activities incidental to fishing (05)',
'Processing of meat cattle',
 'Processing of meat pigs',
 'Processing of meat poultry',
 'Production of meat products nec',
 'Processing vegetable oils and fats',
 'Processing of dairy products',
 'Processed rice',
 'Sugar refining',
 'Processing of Food products nec',
 'Manufacture of beverages',
 'Manufacture of fish products']

# Sectors to exclude in MRIO model
excluded_sectors = (
    [
        #'Chemical and fertilizer minerals, salt and other mining and quarrying products n.e.c.',
        #'N-fertiliser',
        #'P- and other fertiliser'
    ]
)

other_sectors = list(
    set(EXIOBASE_sectors)
    - set(excluded_sectors)
    - set(extracted_sectors)
)


fabio_final_demand_categories = (
    [
        "balancing",
        "food",
        "losses",
        "other",
        "stock_addition",
        "tourist",
        "unspecified",
        "processing", 
        "residuals"        
    ]
)

exclude_negatives = True


# Food groups used in the dietary scenarios

Whole_grains_fao = [
    'Rice and products',
    'Wheat and products',
    'Barley and products',
    'Maize and products',
    'Rye and products',
    'Oats',
    'Millet and products',
    'Sorghum and products',
    'Cereals, Other', # specific for FABIO
    'Cereals, other'# specific for FAO
]

Vegetables_fao = [
    'Tomatoes and products',
    'Onions',
    'Vegetables, other',
    'Pepper',
    'Pimento'
]

Starchy_vegetables_fao = [
    'Cassava and products',
    'Potatoes and products',
    'Sweet potatoes',
    'Yams',
    'Roots, Other',
    'Plantains'
]

Starchy_others_fao = [
    'Cassava and products',
    'Sweet potatoes',
    'Yams',
    'Roots, Other',
    'Plantains'
]

Potatoes_fao= [
    'Potatoes and products'
]

Fruits_fao = [
    'Oranges, Mandarines',
    'Lemons, Limes and products',
    'Grapefruit and products',
    'Citrus, Other',
    'Bananas',
    'Apples and products',
    'Pineapples and products',
    'Dates',
    'Grapes and products (excl wine)',
    'Fruits, Other'
]

Dairy_foods_fao = [
    'Milk - Excluding Butter'
]

Beef_lamb_pig_fao = [
    'Bovine Meat',
    'Mutton & Goat Meat',
    'Pigmeat',
    'Offals, Edible'
]

Poultry_fao = [
    'Poultry Meat',
    'Meat, Other'
    
]

Eggs_fao = [
    'Eggs'
]

Legumes_fao = [
    'Beans',
    'Pulses, Other and products',
    'Peas',
    'Soyabeans'
]

Nuts_seeds_fao=[
    'Sunflower seed',
    'Sesame seed',
    'Rape and Mustardseed',
    'Cottonseed',
    'Palm kernels',
    'Coconuts - Incl Copra',
    'Oilcrops, Other',
    'Nuts and products',
    'Groundnuts'
]

Nuts_fao = [
    'Nuts and products', 
    'Groundnuts'
]


Unsaturated_oil_fao = [
    'Rape and Mustard Oil',
    'Sunflowerseed Oil',
    'Olive Oil',
    'Sesameseed Oil',
    'Cottonseed Oil',
    'Oilcrops Oil, Other',
    'Maize Germ Oil',
    'Groundnut Oil',
    'Soyabean Oil' ,
    'Oilcrops Oil, Other'
    
]


Palm_coco_oil_fao= [
    'Palm Oil',
    'Coconut Oil',
    'Palmkernel Oil'
   
]

Lard_tallow_butter_fao=[
    'Fats, Animals, Raw',
    'Butter, Ghee'
]

Sugars_fao = [
    'Sugar (Raw Equivalent)',
    'Sugar non-centrifugal',
    'Honey'
]



Fish_fabio = [
    'Fish, Seafood'
]





