import json
import os
import pandas as pd



lst = os.listdir(os.path.join(os.getcwd(),'dataset'))

df = []

for f in lst:
    if not f.endswith('.py'):
            with open('dataset/' + f, 'r') as j:
                obj = json.load(j)
                dict_lst = obj.get('data')
                if dict_lst != None:
                    for dic in dict_lst:
                        df.append({'ratings': dic['rating'], 'text': ' '.join(dic['text'].split('\n'))})

tbl = pd.DataFrame(df)
tbl.to_csv('seedly.csv', index=False)
