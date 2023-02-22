#week 4 homework

import csv

nationality_writers = {}

with open ('Artworks.csv') as file:
   processed_csv = csv.reader(file)
   header_row = next(processed_csv,None)
   for row in processed_csv:
      nationalities_str = row[4]
      nationalities = nationalities_str.split(' ')
      for nat in nationalities:
         if nat in nationality_writers:
           nationality_writers[nat]['csv'].writerow(row)
         else:
             nat_file = open(f'res/{nat}.csv', 'w')
             nat_csv = csv.writer(nat_file)
             nat_csv.writerow(header_row)
             nat_csv.writerow(row)
             nationality_writers[nat] = {
                 'file': nat_file,
                 'csv': nat_csv
               }

#for files in nationality_writers:
#   nationality_writers[files]('file').close()


#import pandas as pd
#import os

#df = pd.read_csv('documents/info664exercises/week_4/Artworks.csv')
#column_name = 'Nationality'
#unique_values = df[column_name].unique()

#for unique_value in unique_values:
#   df_output = df[df[column_name].str.contains(unique_value)]
#   output_path = os.path.join('output', unique_value + '.csv')
#   df_output.to_csv(output_path, file_name=unique_value, index=False)

#import csv

#res = {}
#with open('Documents/info664exercises/week_4/Artworks.csv') as art_file:
#   art_csv = csv.DictReader(art_file)
#  for art in art_csv:
#     nats = art['Nationality'].split(" ")
#     for nat in nats:
#        res[nat] = res.setdefault(nat, 0) + 1

#for bla in res:
#   print(f'{bla}: {res[bla]}')