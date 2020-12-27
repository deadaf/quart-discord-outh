songs = [
    {"title": "happy birthday", "playcount": 4},
    {"title": "AC/DC", "playcount": 2},
    {"title": "Billie Jean", "playcount": 6},
    {"title": "Human Touch", "playcount": 3}
]

# print("===========================")
# print(f'Songs --> {songs} \n')
# title = list(map(lambda x: x['title'], songs))
# print(f'Print Title --> {title}')

# playcount = list(map(lambda x: x['playcount'], songs))
# print(f'Print Playcount --> {playcount}')
# print(f'Print Sorted playcount --> {sorted(playcount)}')

# # Aliter -
# print(sorted(list(map(lambda x: x['playcount'], songs))))

for i in songs:
    print('title = ', i['title'], '\nplaycount = ', i['playcount'])
# print('playcount = ', i['playcount'])
