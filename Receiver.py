# obtains chip sequence of the station which receiver wants to listen
def chip_assignment(listen):
    chip = []
    if listen == "a": info = file[1]
    elif listen == "b": info = file[2]
    elif listen == "c": info = file[3]
    elif listen == "d": info = file[4]
    else: print("Check the \"receive.txt\" file, Enter station you want to listen correctly, e.g., \"a\" or \"b\" or \"c\" or \"d\" ")

    info = info.strip()

    # checks case: when line is blank, i.e., chip sequence not present
    if len(info) == 0:
        raise Exception("One of the chip sequence is not given")

    # checks case: if user wrongly entered chip sequence in format -> -1, +1, -1,
    if (info[-1]) == ',':
        raise Exception("No comma after the last station's bit name")

    info = info.split(",")  # trim whitespaces & obtain a list of strings

    # both case: +1, -1, +1 or +1,-1,+1 should be okay
    for i in range(len(info)):
        info[i] = info[i].strip()

    # checks case: for chip sequence, 8 bits must be transmitted.
    if len(info) != 8:
        raise Exception("Each chip sequence must be 8 bits")

    # checks case: each chip sequence must contain only '+1' or '-1'
    for i in range(len(info)):
        if info[i] == "+1" or info[i] == "-1":
            pass
        else:
            raise Exception("Each chip sequence must contain only '+1' or '-1'")

    for i in info:
        chip.append(int(i)) #convert chip seq. from str to int
    return chip

#calculates the normalized innner product of sequence S and the station receiver wants to listen to
def inner_product(chip):
    sum = 0; S = []; Seq = file[8]; Seq = Seq.strip(); Seq = Seq.split(", ")
    for i in Seq:
        S.append(int(i))
    for j in range(len(chip)):
        sum += chip[j]*S[j] #inner product
    return sum/8

def read_station():
    #reads chip seq. from receive.txt which was written from transmitter.py
    listen = file[6]
    listen = listen.strip()
    # checks case: when line 6 is blank, i.e., no station name
    if len(listen) == 0:
        raise Exception("No station name given")

    listen = listen.casefold()

    if len(listen) != 1:
        raise Exception("Enter only one value: a or b or c or d")

    #checks case: station name is only alphabetic.
    if listen.isalpha() == False:
        raise Exception("Station name should only be alphabetic")

    #checks case: station name is only a, b, c, d
    if listen == 'a' or listen == 'b' or listen == 'c' or listen == 'd':
            pass
    else:
        raise Exception("Stations name can only be: a or b or c or d")

    return listen

bit_sequence = open("receive.txt", "r")
file = bit_sequence.readlines()
listen = ""
try:
    listen = read_station()
except Exception as e:
    print(e)
    exit(1)

chip = []
try:
    chip = chip_assignment(listen) #call func chip_assignment to convert str to list
except Exception as e:
    print(e)
    exit(1)

in_prod = inner_product(chip)

if in_prod == 1: print("Station " + listen + " sent bit 1")
elif in_prod == -1: print("Station " + listen + " sent bit 0")
elif in_prod == 0: print("Station " + listen + " is not active, so no bit is received")
else: print("Error! Enter the data in 'receive.txt' and trans.txt in correct format")
