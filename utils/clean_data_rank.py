combined_data = []

# Open all the CSV files
with open("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/2016.csv", "r") as f, open("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/2017.csv", "r") as f2, open("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/2018.csv", "r") as f3, open("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/2019.csv", "r") as f4,open("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/Final.csv", "r") as f5:
    for line in f:
        line = line.strip().split(",")
        country = line[0]
        Overall_rank = line[2] if line[2] != "" else '0'
        if country != "Country":
            combined_data.append([country, '2016', Overall_rank])

    for line in f2:
        line = line.strip().split(",")
        country = line[0]
        Overall_rank = line[1] if line[1] != "" else '0'
        if country != "Country":
            combined_data.append([country, '2017', Overall_rank])

    for line in f3:
        line = line.strip().split(",")
        country = line[1]
        Overall_rank = line[0] if line[0] != "" else '0'
        if country != "Country":
            combined_data.append([country, '2018', Overall_rank])

    for line in f4:
        line = line.strip().split(",")
        country = line[1]
        Overall_rank = line[0] if line[0] != "" else '0'
        if country != "Country":
            combined_data.append([country, '2019', Overall_rank])


# Write the combined data to a new CSV file
with open("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/heat_map.csv", "w") as f:
    f.write("Country,Year,Overall rank\n")
    for row in combined_data:
        line = f"{row[0]},{int(row[1])},{float(row[2])}\n"
        f.write(line)
