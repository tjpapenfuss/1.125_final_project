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
