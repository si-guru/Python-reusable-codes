import sys


def process(**data):
    print(data)
    print(data['value1'])
    print(data['value2'])
    print(data['value3'])


def main():

    # Position from which
    position = 1
    arguments = sys.argv[position:]
    json_value = {}
    for arg in arguments:
        data = arg.split('=')
        key = data[0].strip()
        value = data[1].strip()
        json_value[key] = value
    process(**json_value)
    pass


if __name__ == "__main__":
    main()