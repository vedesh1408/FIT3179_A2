country_dict = dict()

# Define a function to replace empty elements with 0
def replace_empty_with_zero(value):
    return value if value != '' else '0'

# Open all the CSV files
with open("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/2016.csv", "r") as f, open("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/2017.csv", "r") as f2, open("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/2018.csv", "r") as f3, open("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/2019.csv", "r") as f4:
    for line in f:
        line = line.strip().split(",")
        country = line[0]
        score = replace_empty_with_zero(line[3])
        if country != "Country":
            country_dict[country] = {'2016': score}

    for line in f2:
        line = line.strip().split(",")
        country = line[0]
        score = replace_empty_with_zero(line[2])
        if country not in country_dict and country != "Country":
            country_dict[country] = {'2017': score}
        elif country != "Country":
            country_dict[country]['2017'] = score

    for line in f3:
        line = line.strip().split(",")
        country = line[1]
        score = replace_empty_with_zero(line[2])
        if country not in country_dict and country != "Country":
            country_dict[country] = {'2018': score}
        elif country != "Country":
            country_dict[country]['2018'] = score

    for line in f4:
        line = line.strip().split(",")
        country = line[1]
        score = replace_empty_with_zero(line[2])
        if country not in country_dict and country != "Country":
            country_dict[country] = {'2019': score}
        elif country != "Country":
            country_dict[country]['2019'] = score

# Write the combined data to a new CSV file
with open("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/combined.csv", "w") as f:
    f.write("Country,2016,2017,2018,2019\n")
    for country, scores in country_dict.items():
        line = f"{country},{scores.get('2016', '0')},{scores.get('2017', '0')},{scores.get('2018', '0')},{scores.get('2019', '0')}\n"
        f.write(line)
