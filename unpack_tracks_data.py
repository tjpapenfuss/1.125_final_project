from xml.etree.ElementTree import tostringlist
import pandas as pd
import re

imported_df_edm = pd.read_csv("athena_build/data/edm_playlist_tracks_data.csv", index_col=False)
imported_df_indie = pd.read_csv("athena_build/data/indie_playlist_tracks_data.csv", index_col=False)
imported_df_jazz = pd.read_csv("athena_build/data/Jazz_playlist_tracks_data.csv", index_col=False)

df_indie_pl = pd.read_csv("athena_build/data/indie_playlist_data.csv", index_col=False)
df_jazz_pl = pd.read_csv("athena_build/data/Jazz_playlist_data.csv", index_col=False)
df_edm_pl = pd.read_csv("athena_build/data/edm_playlist_data.csv", index_col=False)

imported_df_edm["track_name"] = imported_df_edm["track_name"].str.replace("[^A-Za-z0-9 ]", "", regex=True)
imported_df_indie["track_name"] = imported_df_indie["track_name"].str.replace("[^A-Za-z0-9 ]", "", regex=True)
imported_df_jazz["track_name"] = imported_df_jazz["track_name"].str.replace("[^A-Za-z0-9 ]", "", regex=True)

imported_df_edm["playlist_name"] = imported_df_edm["playlist_name"].str.replace("[^A-Za-z0-9 ]", "", regex=True, flags=re.UNICODE)
imported_df_indie["playlist_name"] = imported_df_indie["playlist_name"].str.replace("[^A-Za-z0-9 ]", "", regex=True, flags=re.UNICODE)
imported_df_jazz["playlist_name"] = imported_df_jazz["playlist_name"].str.replace("[^A-Za-z0-9 ]", "", regex=True, flags=re.UNICODE)

df_indie_pl["playlist_name"] = df_indie_pl["playlist_name"].str.replace("[^A-Za-z0-9 ]", "", regex=True, flags=re.UNICODE)
df_edm_pl["playlist_name"] = df_edm_pl["playlist_name"].str.replace("[^A-Za-z0-9 ]", "", regex=True, flags=re.UNICODE)
df_jazz_pl["playlist_name"] = df_jazz_pl["playlist_name"].str.replace("[^A-Za-z0-9 ]", "", regex=True, flags=re.UNICODE)

imported_df_edm.to_csv("athena_build/data/edm_playlist_tracks_data.csv", index=False)
imported_df_indie.to_csv("athena_build/data/indie_playlist_tracks_data.csv", index=False)
imported_df_jazz.to_csv("athena_build/data/Jazz_playlist_tracks_data.csv", index=False)

df_indie_pl.to_csv("athena_build/data/indie_playlist_data.csv", index=False)
df_jazz_pl.to_csv("athena_build/data/Jazz_playlist_data.csv", index=False)
df_edm_pl.to_csv("athena_build/data/edm_playlist_data.csv", index=False)

# df.astype(str).apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))


dict_artist_id = {}
dict_artist_name = {}    
itemNo = 0

#for item in range(len(imported_df)):
    # count = 1
    # dict_artist_id[itemNo] = {}
    # dict_artist_name[itemNo] = {}
    # if("[" in imported_df['artist_id'][item]):
    #     ini_list_id = imported_df['artist_id'][item]
    #     ini_list_id = re.sub('\'', '', ini_list_id)
    #     res_id = ini_list_id.strip('][').split(', ')
                
    #     for x in res_id:
    #         dict_artist_id[itemNo]["Artist{0}_id".format(count)] = x
    #         count += 1
    # else:
    #     dict_artist_id[itemNo]["Artist{0}_id".format(count)] = imported_df['artist_id'][item]
    
    # if("[" in imported_df['artist_name'][item]):
    #     count = 1
    #     ini_list_name = imported_df['artist_name'][item]
    #     ini_list_name = re.sub('\'', '', ini_list_name)
    #     res_name = ini_list_name.strip('][').split(', ')

    #     for x in res_name:
    #         dict_artist_name[itemNo]["Artist{0}_name".format(count)] = x
    #         count += 1
    # else:
    #     dict_artist_name[itemNo]["Artist{0}_name".format(count)] = imported_df['artist_name'][item]
    
    #imported_df["track_name"][item] = imported_df["track_name"][item].replace(',', '')

    #itemNo += 1


#imported_df = imported_df.join(pd.DataFrame.from_dict(dict_artist_id, orient='index'))
#imported_df = imported_df.drop(columns=['artist_id'])
#imported_df = imported_df.join(pd.DataFrame.from_dict(dict_artist_name, orient='index'))
#imported_df = imported_df.drop(columns=['artist_name'])
# df = pd.DataFrame.from_dict(dict_artist_id, orient='index')

# imported_df.to_csv("athena_build/data/edm_playlist_tracks_data.csv", index=False)


