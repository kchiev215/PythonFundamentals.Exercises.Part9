import json
import os
import pickle

#Part A
def read_json(file_path):
    f = open(file_path, 'rb')
    data = json.load(f.read())
    return data

#Part B
def read_all_json_files(file_path):
    list_of_json_file = []
    for files in os.walk(file_path):
        for json_file in files:
            if json_file.endswith('.json'):
                file_along_path = read_json(os.path.join(file_path, json_file))
                file_along_path.append(list_of_json_file)
    return list_of_json_file

#Part C
def write_pickle(file_path):
    with open('super_smash_characters.pickle', 'wb') as f:
        pickle.dump(file_path, f)

write_pickle('/Users/Thina/Desktop/Python/PythonFundamentals.Exercises.Part9')

#Part D
def load_pick(file_path):
    f = open(file_path, 'rb')
    data = pickle.load(f)
    return data

print(load_pick('super_smash_characters.pickle'))

#Exercise 2

DBZ = {
    'Human': 'Chichi',
    'Saiyan': 'Goku',
    'Educated': 'Gohan',
    'Prince': 'Vegeta'
}

new_file = open('/Users/Thina/Desktop/Python/PythonFundamentals.Exercises.Part9/data/dragon_ball_z/characters.json', 'w')
json.dump(DBZ, new_file)










