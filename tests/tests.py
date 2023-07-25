import pandas as pd

file_path = r"<.csv>"

df = pd.read_csv(file_path)

dict_df = df.to_dict()

list_of_headers = dict_df.keys()
    
for index in range(len(dict_df["ID"])):
    dict_df["ID"][index]
    dict_df["Nome"][index]
    dict_df["Sobrenome"][index]
    dict_df["Email"][index]
    dict_df["Telefone"][index]
    
print(list_of_headers)