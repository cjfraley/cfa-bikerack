import csv
import yaml
# Where is the user?

# What's the closest bike rack?
def closest_bike_rack(lat,lon):
    field_names=["RackID","Address","Ward","Community Area","Community Name","TotInstall","Latitude","Longitude","Historical","F12","F13","LOCATION","Boundaries - ZIP Codes","Community Areas","Zip Codes","Census Tracts","Wards",":@computed_region_awaf_s7ux"]
    target_rack={
        "Latitude": 0,
        "Longitude": 0,
        "RackID": 0,
        "Distance": 10000
    }
    with open("Bike_Racks.csv", "r") as csv_stream:
        data_reader=csv.DictReader(csv_stream)
        for row in data_reader:
            dist=(lat-float(row["Latitude"]))**2+(lon-float(row["Longitude"]))**2
            if dist<target_rack["Distance"]:
                target_rack={
                    "Latitude": row["Latitude"],
                    "Longitude": row["Longitude"],
                    "RackID": row["RackID"],
                    "Distance": dist
                }

        return target_rack

if __name__ == "__main__":
    print(yaml.dump(closest_bike_rack(41.875659, -87.618945)))
