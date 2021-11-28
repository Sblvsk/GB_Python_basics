from itertools import zip_longest
import json

with open('users.csv', encoding='utf-8') as f:
    users_list = [x.strip().replace(',', ' ') for x in f]

with open('hobby.csv', encoding='utf-8') as f:
    hobby_list = [x.strip().replace(',', ', ') for x in f]

if len(hobby_list) < len(users_list):
    users_hobbys_dict = {key: value for key,value in zip_longest(users_list, hobby_list)}
else:
    exit(1)

with open('users_hobbys.json', 'w', encoding='utf-8') as f:
    users_hobbys_dict_to_str = json.dumps(users_hobbys_dict)
    #json.dump(users_hobbys_dict_to_str, f)
    f.write(users_hobbys_dict_to_str)












