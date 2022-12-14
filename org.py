













# v------------------------- this works ----------------------------v

# player_list = []
# player_list.append(data.copy())

# for player in player_list:
#     print(player)

# ^------------------------- this works ----------------------------^

# v------------------------- this works ----------------------------v

# player_list = []
# player_list.append(data.copy())

# for player in player_list:
#     for key, value in player.items():
#         print(key, value)

# ^------------------------- this works ----------------------------^

# v------------------------- this works ----------------------------v

# team_name = data['response'][0]['team']['name']
# team_logo = data['response'][0]['team']['logo']
# player_name = data['response'][1]['players'][0]['player']['name']
# player_photo = data['response'][1]['players'][0]['player']['photo']
# player_position = data['response'][1]['players'][0]['statistics'][0]['games']['position']
# off_sides = data['response'][1]['players'][0]['statistics'][0]['offsides']
# total_shots = data['response'][1]['players'][0]['statistics'][0]['shots']['total']
# ontarget_shots = data['response'][1]['players'][0]['statistics'][0]['shots']['on']
# # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# goals = data['response'][1]['players'][0]['statistics'][0]['goals']
# passes = data['response'][1]['players'][0]['statistics'][0]['passes']
# tackles = data['response'][1]['players'][0]['statistics'][0]['tackles']
# duels = data['response'][1]['players'][0]['statistics'][0]['duels']
# dribbles = data['response'][1]['players'][0]['statistics'][0]['dribbles']
# fouls = data['response'][1]['players'][0]['statistics'][0]['fouls']
# cards = data['response'][1]['players'][0]['statistics'][0]['cards']
# penalty = data['response'][1]['players'][0]['statistics'][0]['penalty']

# ^------------------------- this works ----------------------------^

# v------------------------- this works ----------------------------v

# goals = data['response'][1]['players'][0]['statistics'][0]['goals']
# print(goals)
# print(type(goals))

# for goal in goals:
#     for key, value in goals.items():
#         print(key)
#         print(value)

# ^------------------------- this works ----------------------------^

# v------------------------- this works ----------------------------v

# players = data['response']
# print(' players :',players)
# l = []
# for player in players:
#     for key, value in player.items():
        # print('%%%%%%%%%%%%TOP%%%%%%%%%%%%%%%')
        # print(' player :', player)
        # print('************BOTTOM************')
        # print(type(player))

# ^------------------------- this works ----------------------------^

# v------------------------- this works ----------------------------v

# players = data['response']
# print(' players :',players)
# l = []
# for player in players:
#     for key, value in player.items():
#         l.append(player)
        # print('%%%%%%%%%%%%TOP%%%%%%%%%%%%%%%')
        # print(' player :', player)
        # print('************BOTTOM************')
        # print(type(player))
        # print(l)

# print(l)

# ^------------------------- this works ----------------------------^










# v------------------------- this works ----------------------------v
# for group in groups:
#     team = group.get('team')
#     id = team.get('id')
#     print(id)
#     print(team)
# ^------------------------- this works ----------------------------^


# v------------------------- this works ----------------------------v
# groups = data['response']
# print(type(groups))
# print('groups :',groups)



# for group in groups:
#     team = group.get('team')
#     id = team.get('id')
#     players = group.get('players')
    # print(players)
    # print(id)
    # print(team)
    # print(players)


 
# for player in players:
#     print(player)
#     count =+ 1
#     print(count)
# ^------------------------- this works ----------------------------^
