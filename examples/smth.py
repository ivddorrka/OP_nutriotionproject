import pandas as pd
a = pd.read_csv("recipes1.csv")
b = pd.read_csv("recipes2_new.csv")
merged = a.merge(b, on=['name', 'products', 'instuction',
                        'calories', 'lipids', 'fats', 'carbohydrates'])
merged.to_csv("recipes.csv", index=False)
