import json

msg = {'first_name': 'John',
       'second_name': 'Dow',
       'age': 33,
       'is_male': True
       }

json_string = '{"first_name" : "John", "second_name" : "Dow", "age" : 33, "is_male": true }'


def dict_to_json():
    json_data = json.dumps(msg)
    print(json_data)


def dict_to_json_pretty():
    json_data = json.dumps(msg, indent=4)
    print(json_data)


def json_from_string():
    data = json.loads(json_string)
    print(data['first_name'], data['second_name'])  # John Dow


def json_from_file():
    with open('../data/params.json', 'r') as file:
        json_object = json.load(file)
        print(json_object)


if __name__ == '__main__':
    json_from_string()

    # dict_to_json()
    # dict_to_json_pretty()

    # json_from_file()
