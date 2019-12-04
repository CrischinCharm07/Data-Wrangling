import pandas as pd

A = {'Student': ['Ice Bear', 'Panda', 'Grizzly'],
     'Math': [80, 95, 79]}
A = pd.DataFrame(A, columns = ['Student','Math'])

B = {'Student': ['Ice Bear', 'Panda', 'Grizzly'],
     'Electronics': [85, 81, 83]}
B = pd.DataFrame(B, columns = ['Student','Electronics'])

C = {'Student': ['Ice Bear', 'Panda', 'Grizzly'],
     'GEAS': [90, 79, 93]}
C = pd.DataFrame(C, columns = ['Student','GEAS'])

D = {'Student': ['Ice Bear', 'Panda', 'Grizzly'],
     'ESAT': [93, 89, 88]}
D = pd.DataFrame(D, columns = ['Student','ESAT'])

E = pd.merge(A, B, how='outer', on='Student')

F = pd.merge(E, C, how='outer', on='Student')

print(" ")
print(pd.merge(F, D, how='outer', on='Student'))
print(" ")

G = pd.merge(F, D, how='outer', on='Student')

longformat = pd.melt(G, id_vars = 'Student', value_vars=['Math','Electronics','GEAS','ESAT'])

print(longformat.rename(columns={'variable':'Subject', 'value': 'Grades'}))
