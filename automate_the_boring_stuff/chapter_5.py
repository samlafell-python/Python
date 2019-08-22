birthdays = {'Alice': 'Apr 1',
             'Bob': 'Dec 12',
             'Carol': 'Mar 4'
             }

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday? (Format: ex, Jun 18)')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
    break


# for v in birthdays.values():
#     print(v)
#
# for k in birthdays.keys():
#     print(k)
#
# for i in birthdays.items():
#     print(list(i))
#
# for k, v in birthdays.items():
#     print('Key:', k, 'Value:', v)

import pprint
#
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] += 1
#  print(count)
#  pprint.pprint(count)
#
# # Can store pprint in a variable
# pretty_count = pprint.pformat(count)
# print(pretty_count)

# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' '
#                , 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
#
# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
#
# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'
#
# printBoard(theBoard)


# Nested Dictionaries and Lists

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

# def totalBrought(guests, items):
#     numBrought = 0
#     for k, v in guests.items():
#         numBrought = numBrought + v.get(items, 0)
#     return numBrought
#
# print('Number of things being brought:')
# print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
# print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
# print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
# print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
# print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))


# Chapter 5 Project:

def displayInventory(inventory):
    print('Inventory: ')
    itemTotal = 0
    for k, v in inventory.items():
        k = k.capitalize()
        if v > 1:
            k = k + 's'
        itemTotal += v
        print(v, k)
    print('Total number of items:', itemTotal)


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(inv)


def add_to_inventory(inventory, addedItems):
    for item in addedItems:
        if item not in inventory.keys():
            inventory[item] = 1
        else:
            inventory[item] += 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
displayInventory(inv)
