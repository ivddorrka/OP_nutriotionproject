import json

def json_dict_transformations():
    '''
    This function demonstrates json object conversion into python dictionary and vice versa
    '''
    # initial json object represented as str
    data_json = '{"nickname":"yves","hours_spent":300,"active":true}'
    print(f"JSON ({type(data_json)}): {data_json}")

    # transforms json object into python dictionary
    data_dict = json.loads(data_json)
    print(f"Json -> Dict ({type(data_dict)}): {data_dict}")

    # transforms python dictionary into json object, represented as str
    json_data = json.dumps(data_json)
    print(f"Dict -> Json ({type(json_data)}): {json_data}")

def read_and_write_json_file(path : str = 'example.json'):
    '''
    This function demonstrates how to read and write json from/into file
    '''
    with open(path) as json_file:
        data = json.load(json_file)

    print(f'{type(data)}: {data}')

    # write to new json file in pretty format (with indents) and sorted
    with open(f"new.json", 'w') as json_file:
        json.dump(data, json_file, indent=4, sort_keys=True)


if __name__ == '__main__':
    json_dict_transformations()
    read_and_write_json_file()
