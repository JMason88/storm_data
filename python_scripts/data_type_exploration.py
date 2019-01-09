import pandas as pd
from csv_download import response

df = pd.read_csv(response)

print(df.head())

print("-"*50)
print("FID")
print("-"*50)
print("Max is {}".format(df['FID'].max()))
print("Min is {}".format(df['FID'].min()))

##########################################

print("-"*50)
print("YEAR")
print("-"*50)
print("Max is {}".format(df['YEAR'].max()))
print("Min is {}".format(df['YEAR'].min()))

##########################################

print("-"*50)
print("MONTH")
print("-"*50)
print("Max is {}".format(df['MONTH'].max()))
print("Min is {}".format(df['MONTH'].min()))

##########################################

print("-"*50)
print("DAY")
print("-"*50)
print("Max is {}".format(df['DAY'].max()))
print("Min is {}".format(df['DAY'].min()))

##########################################

print("-"*50)
print("AD_TIME")
print("-"*50)
print("Max is {}".format(df['AD_TIME'].max()))
print("Min is {}".format(df['AD_TIME'].min()))

##########################################

print("-"*50)
print("BTID")
print("-"*50)
print("Max is {}".format(df['BTID'].max()))
print("Min is {}".format(df['BTID'].min()))

##########################################

print("-"*50)
print("NAME")
print("-"*50)
name_lengths = []
for name in df['NAME']:
    name_lengths.append(len(name))

print("Max is {}".format(max(name_lengths)))
print("Min is {}".format(min(name_lengths)))

##########################################

print("-"*50)
print("LAT")
print("-"*50)
print("Max is {}".format(df['LAT'].max()))
print("Min is {}".format(df['LAT'].min()))

##########################################

print("-"*50)
print("LONG")
print("-"*50)
print("Max is {}".format(df['LONG'].max()))
print("Min is {}".format(df['LONG'].min()))

##########################################

print("-"*50)
print("WIND_KTS")
print("-"*50)
print("Max is {}".format(df['WIND_KTS'].max()))
print("Min is {}".format(df['WIND_KTS'].min()))

##########################################

print("-"*50)
print("PRESSURE")
print("-"*50)
print("Max is {}".format(df['PRESSURE'].max()))
print("Min is {}".format(df['PRESSURE'].min()))

##########################################

print("-"*50)
print("CAT")
print("-"*50)
cat_lengths = []
for cat in df['CAT']:
    cat_lengths.append(len(cat))

print("Max is {}".format(max(cat_lengths)))
print("Min is {}".format(min(cat_lengths)))

##########################################

print("-"*50)
print("BASIN")
print("-"*50)
basin_lengths = []
for basin in df['BASIN']:
    basin_lengths.append(len(basin))

print("Max is {}".format(max(basin_lengths)))
print("Min is {}".format(min(basin_lengths)))

##########################################

print("-"*50)
print("Shape_Leng")
print("-"*50)

print("Max is {}".format(df['Shape_Leng'].max()))
print("Min is {}".format(df['Shape_Leng'].min()))
