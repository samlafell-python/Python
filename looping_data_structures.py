import pandas as pd
brics = pd.read_csv('brics.csv', index_col=0)

# for val in brics:
#  print(val)

# for lab, row in brics.iterrows():
# print(lab)
#  print(row)


# To Only Print Capital
for lab, row in brics.iterrows():
    print(lab + ': ' + row['capital'])

# More Complicated
# for lab, row in brics.iterrows():
#   brics.loc[lab, 'name_length'] = len(row['country'])

#brics["name_length"] = brics['country'].apply(len)

# print(brics)
