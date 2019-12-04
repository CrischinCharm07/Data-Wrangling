import pandas as pd

messy = {'Box': ['Box1', 'Box1', 'Box1', 'Box2', 'Box2', 'Box2'], 
         'Dimension': ['Length', 'Width', 'Height', 'Length', 'Width', 'Height'],
         'Value': [6, 4, 2, 5, 3, 4]}
messy = pd.DataFrame(messy, columns=['Box', 'Dimension', 'Value'])

tidy = messy.pivot_table(index=['Box'], columns = 'Dimension', values = 'Value')

tidy['Volume'] = tidy.Length*tidy.Height*tidy.Width

print(" ")
print(tidy)
