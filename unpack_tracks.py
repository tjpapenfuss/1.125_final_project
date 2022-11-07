from xml.etree.ElementTree import tostringlist
import pandas as pd
import re

imported_df = pd.read_csv("athena_build/data/edm_playlist_tracks_original.csv")

ini_list = imported_df['artist_id'][0]
ini_list = re.sub('\'', '', ini_list)
# printing initialized string of list and its type
print ("initial string", ini_list)
print (type(ini_list))
  
# Converting string to list
res = ini_list.strip('][').split(', ')
  
# printing final result and its type
print ("final list", res)
print (type(res))
print(res[0])

dict_artist_id = {}
dict_artist_name = {}    
itemNo = 0

for item in range(len(imported_df)):
    count = 1
    dict_artist_id[itemNo] = {}
    dict_artist_name[itemNo] = {}
    if("[" in imported_df['artist_id'][item]):
        ini_list_id = imported_df['artist_id'][item]
        ini_list_id = re.sub('\'', '', ini_list_id)
        res_id = ini_list_id.strip('][').split(', ')
                
        for x in res_id:
            dict_artist_id[itemNo]["Artist{0}_id".format(count)] = x
            count += 1
    else:
        dict_artist_id[itemNo]["Artist{0}_id".format(count)] = imported_df['artist_id'][item]
    
    if("[" in imported_df['artist_name'][item]):
        count = 1
        ini_list_name = imported_df['artist_name'][item]
        ini_list_name = re.sub('\'', '', ini_list_name)
        res_name = ini_list_name.strip('][').split(', ')

        for x in res_name:
            dict_artist_name[itemNo]["Artist{0}_name".format(count)] = x
            count += 1
    else:
        dict_artist_name[itemNo]["Artist{0}_name".format(count)] = imported_df['artist_name'][item]
    imported_df["name"][item] = imported_df["name"][item].replace(',', '')

    itemNo += 1


imported_df = imported_df.join(pd.DataFrame.from_dict(dict_artist_id, orient='index'))
imported_df = imported_df.drop(columns=['artist_id'])
imported_df = imported_df.join(pd.DataFrame.from_dict(dict_artist_name, orient='index'))
imported_df = imported_df.drop(columns=['artist_name'])
# df = pd.DataFrame.from_dict(dict_artist_id, orient='index')

imported_df.to_csv("athena_build/data/edm_playlist_tracks.csv", index=False)

