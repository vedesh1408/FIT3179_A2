combined_data = []

# Open all the CSV files
with open("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/2016.csv", "r") as f, open("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/2017.csv", "r") as f2, open("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/2018.csv", "r") as f3, open("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/2019.csv", "r") as f4:
    for line in f:
        line = line.strip().split(",")
        country = line[0]
        score = line[3] if line[3] != "" else '0'
        if country != "Country":
            combined_data.append([country, '2016', score])

    for line in f2:
        line = line.strip().split(",")
        country = line[0]
        score = line[2] if line[2] != "" else '0'
        if country != "Country":
            combined_data.append([country, '2017', score])

    for line in f3:
        line = line.strip().split(",")
        country = line[1]
        score = line[2] if line[2] != "" else '0'
        if country != "Country":
            combined_data.append([country, '2018', score])

    for line in f4:
        line = line.strip().split(",")
        country = line[1]
        score = line[2] if line[2] != "" else '0'
        if country != "Country":
            combined_data.append([country, '2019', score])

# Write the combined data to a new CSV file
with open("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/combined.csv", "w") as f:
    f.write("Country,Year,Score\n")
    for row in combined_data:
        line = f"{row[0]},{row[1]},{row[2]}\n"
        f.write(line)
