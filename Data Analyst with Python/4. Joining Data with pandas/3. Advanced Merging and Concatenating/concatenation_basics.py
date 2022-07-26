'''You have been given a few tables of data with musical track info for different albums from the metal band, Metallica. The track info comes from their Ride The Lightning, Master Of Puppets, and St. Anger albums. Try various features of the .concat() method by concatenating the tables vertically together in different ways.

The tables tracks_master, tracks_ride, and tracks_st have loaded for you.'''



#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''Concatenate tracks_master, tracks_ride, and tracks_st, in that order, setting sort to True.'''

# Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               sort=True)
print(tracks_from_albums)


#################################################################

'''Concatenate tracks_master, tracks_ride, and tracks_st, where the index goes from 0 to n-1.'''

# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               ignore_index=True,
                               sort=True)
print(tracks_from_albums)


#################################################################

'''Concatenate tracks_master, tracks_ride, and tracks_st, showing only columns that are in all tables.'''

# Concatenate the tracks, show only columns names that are in all tables
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               join='inner',
                               sort=True)
print(tracks_from_albums)

