


# print('goals: ', goals)
# print('passes: ', passes)
# print('tackles: ', tackles)
# print('duels: ', duels)
# print('dribbles: ', dribbles)
# print('fouls: ', fouls)
# print('cards: ', cards)
# print('penalty: ', penalty)




# data['response'][1]['players'][0]['statistics'][0]['games']['position']['goals'],
# data['response'][1]['players'][0]['statistics'][0]['games']['position']['passes'],
# data['response'][1]['players'][0]['statistics'][0]['games']['position']['tackles'],
# data['response'][1]['players'][0]['statistics'][0]['games']['position']['duels'],
# data['response'][1]['players'][0]['statistics'][0]['games']['position']['dribbles'],
# data['response'][1]['players'][0]['statistics'][0]['games']['position']['fouls'],
# data['response'][1]['players'][0]['statistics'][0]['games']['position']['cards'],
# data['response'][1]['players'][0]['statistics'][0]['games']['position']['penalty'],
# data['response'][1]['players'][0]['statistics'][0]['games']['position']['offsides'])

# data['response'][1]['players'][0]['statistics'][0]['games']['position']['shots']
# data['response'][1]['players'][0]['statistics'][0]['games']['position']['goals']
# data['response'][1]['players'][0]['statistics'][0]['games']['position']['passes']
# data['response'][1]['players'][0]['statistics'][0]['games']['position']['tackles']
# data['response'][1]['players'][0]['statistics'][0]['games']['position']['duels']
# data['response'][1]['players'][0]['statistics'][0]['games']['position']['dribbles']
# data['response'][1]['players'][0]['statistics'][0]['games']['position']['fouls']
# data['response'][1]['players'][0]['statistics'][0]['games']['position']['cards']
# data['response'][1]['players'][0]['statistics'][0]['games']['position']['penalty']
# data['response'][1]['players'][0]['statistics'][0]['games']['position']['offsides']


# $$$$$$$$$$$$$$$$$ These work              $$$$$$$$$$$$$$$$$
# print('offsides: ', data['response'][1]['players'][0]['statistics'][0]['offsides'])
# print('shots: ', data['response'][1]['players'][0]['statistics'][0]['shots']['total'])
# print('shots_ontarget: ', data['response'][1]['players'][0]['statistics'][0]['shots']['on'])
# print('team_name:', team_name)
# print('team_logo: ', team_logo)
# print('player_name: ', player_name)
# print('player_photo: ', player_photo)
# print('player_position: ', player_position)
# $$$$$$$$$$$$$$$$$ These work              $$$$$$$$$$$$$$$$$




players = []

for d in data:
    for key, value in data.items():
        players.append(data.items())
        # print(players)
count = 0
for player in players:
    # print(player)
    count += 1
    # print(count)
    # print(type(player))

for p in player:
    for key, value in player.items():
        print(key, value)
#         players.append({key, value})
#         print('------------------TOP----------------------')
#         # print(d)
#         print(key)
#         print(value)
#         print('------------------BOTTOM----------------------')