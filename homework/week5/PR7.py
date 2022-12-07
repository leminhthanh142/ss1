import random

capitals = {'Alabama': 'Montgomery',        'Alaska': 'Juneau',
            'Arizona': 'Phoenix',           'Arkansas': 'Little Rock',
            'California': 'Sacramento',     'Colorado': 'Denver',
            'Connecticut': 'Hartford',      'Delaware': 'Dover',
            'Florida': 'Tallahassee',       'Georgia': 'Atlanta',
            'Hawaii': 'Honolulu',           'Idaho': 'Boise',
            'Illinois': 'Springfield',      'Indiana': 'Indianapolis',
            'Iowa': 'Des Moines',           'Kansas': 'Topeka',
            'Kentucky': 'Frankfort',        'Louisiana': 'Baton Rouge',
            'Maine': 'Augusta',             'Maryland': 'Annapolis',
            'Massachusetts': 'Boston',      'Michigan': 'Lansing',
            'Minnesota': 'Saint Paul',      'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City',   'Montana': 'Helena',
            'Nebraska': 'Lincoln',          'Nevada': 'Carson City',
            'New Hampshire': 'Concord',     'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe',       'New York': 'Albany',
            'North Carolina': 'Raleigh',    'North Dakota': 'Bismarck',
            'Ohio': 'Columbus',             'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem',              'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence',   'South Carolina': 'Columbia',
            'South Dakota': 'Pierre',       'Tennessee': 'Nashville',
            'Texas': 'Austin',              'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier',        'Virginia': 'Richmond',
            'Washington': 'Olympia',        'West Virginia': 'Charleston',
            'Wisconsin': 'Madison',         'Wyoming': 'Cheyenne'}


def main():
    right = 0
    wrong = 0

    while True:
        k = random.choice(list(capitals.keys()))
        state = input('Enter the capital of ' + k + ' : ')
        if state.upper() == capitals[k].upper():
            right += 1
        else:
            wrong += 1

        choice = input('Do you want to continue y/n: ')
        if choice.upper() == 'Y':
            continue
        elif choice.upper() == 'N':
            print('Number of correct answers is: ', right)
            print("Number of incorrect answers is:", wrong)
            print('thank you for playing')
            break


if __name__ == '__main__':
    main()