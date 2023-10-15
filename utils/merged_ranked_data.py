combined_data = []

# Open all the CSV files
with open("C:/Users/vedes/Documents/GitHub/FIT3179_A2\data/source_data_for_heatmap/2015.csv", "r") as f, open("C:/Users/vedes/Documents/GitHub/FIT3179_A2\data/source_data_for_heatmap/2016.csv", "r") as f2, open("C:/Users/vedes/Documents/GitHub/FIT3179_A2\data/source_data_for_heatmap/2017.csv", "r") as f3, open("C:/Users/vedes/Documents/GitHub/FIT3179_A2\data/source_data_for_heatmap/2018.csv", "r") as f4,open("C:/Users/vedes/Documents/GitHub/FIT3179_A2\data/source_data_for_heatmap/2019.csv", "r") as f5,open("C:/Users/vedes/Documents/GitHub/FIT3179_A2\data/source_data_for_heatmap/2020.csv", "r") as f6,open("C:/Users/vedes/Documents/GitHub/FIT3179_A2\data/source_data_for_heatmap/2021.csv", "r") as f7,open("C:/Users/vedes/Documents/GitHub/FIT3179_A2\data/source_data_for_heatmap/2022.csv", "r") as f8:
    '''
        2015 - f
        2016 - f2
        2017 - f3
        2018 - f4
        2019 - f5
        2020 - f6
        2021 - f7
        2022 - f8
    '''
    
    
    for line in f:
        line = line.strip().split(",")
        country = line[0]
        Overall_rank = line[2] if line[2] != "" else '0'
        if country != "Country":
            combined_data.append([country, '2015', Overall_rank])

    for line in f2:
        line = line.strip().split(",")
        country = line[0]
        Overall_rank = line[2] if line[2] != "" else '0'
        if country != "Country":
            combined_data.append([country, '2016', Overall_rank])

    for line in f3:
        line = line.strip().split(",")
        country = line[0]
        Overall_rank = line[1] if line[1] != "" else '0'
        if country != "Country":
            combined_data.append([country, '2017', Overall_rank])

    for line in f4:
        line = line.strip().split(",")
        country = line[1]
        Overall_rank = line[0] if line[0] != "" else '0'
        if country != "Country":
            combined_data.append([country, '2018', Overall_rank])

    for line in f5:
        line = line.strip().split(",")
        country = line[1]
        Overall_rank = line[0] if line[0] != "" else '0'
        if country != "Country":
            combined_data.append([country, '2019', Overall_rank])


# Write the combined data to a new CSV file
with open("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/heat_map_v2.csv", "w") as f:
    f.write("Country,Year,Overall rank\n")
    for row in combined_data:
        print(row)
        line = f"{row[0]},{int(row[1])},{float(row[2])}\n"
        print(line)
        f.write(line)
