import json
with open("players.json", "r") as read_file:
    data = json.load(read_file)
    # print(data)


team_name = data['response'][0]['team']['name']
team_logo = data['response'][0]['team']['logo']
player_name = data['response'][1]['players'][0]['player']['name']
player_photo = data['response'][1]['players'][0]['player']['photo']
player_position = data['response'][1]['players'][0]['statistics'][0]['games']['position']
off_sides = data['response'][1]['players'][0]['statistics'][0]['offsides']
total_shots = data['response'][1]['players'][0]['statistics'][0]['shots']['total']
ontarget_shots = data['response'][1]['players'][0]['statistics'][0]['shots']['on']
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
goals = data['response'][1]['players'][0]['statistics'][0]['goals']
passes = data['response'][1]['players'][0]['statistics'][0]['passes']
tackles = data['response'][1]['players'][0]['statistics'][0]['tackles']
duels = data['response'][1]['players'][0]['statistics'][0]['duels']
dribbles = data['response'][1]['players'][0]['statistics'][0]['dribbles']
fouls = data['response'][1]['players'][0]['statistics'][0]['fouls']
cards = data['response'][1]['players'][0]['statistics'][0]['cards']
penalty = data['response'][1]['players'][0]['statistics'][0]['penalty']


print('goals: ', goals)
print('passes: ', passes)
print('tackles: ', tackles)
print('duels: ', duels)
print('dribbles: ', dribbles)
print('fouls: ', fouls)
print('cards: ', cards)
print('penalty: ', penalty)




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