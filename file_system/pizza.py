from time import time
from datetime import datetime
#from parse import *


def main():
    names = []
    orders = {}
    list_orders = []
    used_commands = []
    counter = 0
    sec_counter = 0
    while (True):
        command = input("Enter command>").split()
        used_commands.append(command)
        ts = time()
        stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
        if command[0] == "take":
            if command[1] not in names:
                orders[command[1]] = float(command[2])
            else:
                orders[command[1]] += float(command[2])
            names.append(command[1])
        elif command[0] == "status":
            for el in orders:
                print (el+" - ", orders[el])
        elif command[0] == "save":
            list_orders.append(stamp)
            file = open(stamp, "w+")
            for el in orders:
                file.write(el + " - /n")
                file.write(str(orders[el])+"/n")
        elif command[0] == "list":
            for i in range(0, len(list_orders)):
                print ("[%d] - " % (i+1) + list_orders[i])
        elif command[0] == "load":
            if "list" not in used_commands:
                print("Use list command before loading")
            elif stamp not in list_orders:
                if counter == 0:
                    print ("You have not saved the current order./n If you wish to discard it, type load <number> again.")
                    counter = 1
                else:
                    file = open(list_orders[command[1]])
        elif command[0] == "finish":
            if stamp not in list_orders:
                if sec_counter == 0:
                    sec_counter = 1
                    print ("You have not saved your order./n If you wish to continue, type finish again. /n If you want to save your order, type save")
                else:
                    break


if __name__ == '__main__':
    main()
