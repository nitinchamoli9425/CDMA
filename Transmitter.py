
#checks pairwise orthogonality of chip sequences
def isOrthogonal():
    chip_list1 = []
    def chip_func(i): #reads chip sequence from trans.txt & coverts from str to list
        chip = []
        info = file[i] #read chip sequence at line i in trans.txt
        info = info.strip();
        info = info.strip("\n")

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
                raise Exception("Enter correct chip sequence format, e.g., (-1, +1, -1, +1, +1, +1, -1, -1). Note: chip sequence must contain only '+1' or '-1'.")

        for j in info:
            chip.append(int(j))
        return chip
    for i in range(4):
        chip_list1.append(chip_func(i + 1)) #create list of lists, where each element is a list of individual chip seq

    #checks auto correlation, S . S = 1
    for j in range(len(chip_list1)):
        sum = 0
        for i in chip_list1[j]:
            sum += i*i
        sum /=8
        if sum == 1:
            pass

    #checks cross co-relation
    i = 0
    while(i < 3):
        for k in range(i+1,len(chip_list1)):
            sum =0
            for m in range(8):
                sum += chip_list1[i][m]*chip_list1[k][m] #checks inner product of each chip seq with every other chip seq
            sum = sum / 8
            if sum == 0:
                pass
            else:
                print("Check, either Chip Sequence " + str([i+1]) + " or "+ str([k+1]) + " as they are not orthogonal")
        i +=1

#returns chip sequence of each active station
def bit_seq(stn_name):
    chip = []
    if stn_name == "a": info = file[1] #reads chip sequence for station a from trans.txt
    elif stn_name == "b": info = file[2]
    elif stn_name == "c": info = file[3]
    elif stn_name == "d": info = file[4]
    else: print("Check the \"trans.txt\" file. Enter the input data is correct format ")
    info = info.strip()

    #checks case: when line is blank, i.e., chip sequence not present
    if len(info) == 0:
        raise Exception("One of the chip sequence is not given")

    #checks case: if user wrongly entered chip sequence in format -> -1, +1, -1,
    if (info[-1]) == ',':
        raise Exception("No comma after the last station's bit name")

    info = info.split(",") #trim whitespaces & obtain a list of strings

    #both case: +1, -1, +1 or +1,-1,+1 should be okay
    for i in range(len(info)):
        info[i] = info[i].strip()

    #checks case: for chip sequence, 8 bits must be transmitted.
    if len(info) != 8:
        raise Exception("Each chip sequence must be 8 bits")

    #checks case: each chip sequence must contain only '+1' or '-1'
    for i in range(len(info)):
        if info[i] == "+1" or info[i] == "-1":
            pass
        else:
            raise Exception("Each chip sequence must contain only '+1' or '-1'")

    for i in info:
        chip.append(int(i)) #convert elements of chip seq from str to int type
    return chip

#returns the negation of a chip sequence
def not_gate(valu):
    neg_seq = []
    for i in valu:
        if i == -1: neg_seq.append(+1) #if value is -1 negate to +1
        elif i == 1: neg_seq.append(-1)
        else: print("Check the \"trans.txt\" file, & Enter Code Sequence for Stations in correct format")
    return neg_seq

#return list of lists, where each element contains a list of active chip sequence
def  transmit():
    stn_activ = file[6] #read active stations, from line 6 trans.txt
    stn_activ = stn_activ.strip()

    #checks case: when line 6 is blank, i.e., no station name
    if len(stn_activ) == 0:
        raise Exception("No station name given")

    stn_activ = stn_activ.casefold()

    #checks case: if user wrongly entered in format -> a, b,
    if (stn_activ[-1]) == ',':
        raise Exception("No comma after the last station name")

    stn_activ = stn_activ.split(",")

    #both case: a,b,c or a, b, c should be okay
    for i in range(len(stn_activ)):
        stn_activ[i] = stn_activ[i].strip()

    for i in range(len(stn_activ)):

        # checks case: each station is only alphabetic.
        if stn_activ[i].isalpha() == False:
            raise Exception("Stations name should only be alphabets")

        #checks case: each station is only single value
        if len(stn_activ[i]) != 1:
            raise Exception("For each station, enter a single alphabet")

        #checks case: each station name is only a, b, c, d
        if stn_activ[i] == 'a' or stn_activ[i] == 'b' or stn_activ[i] == 'c' or stn_activ[i] == 'd':
            pass
        else: raise Exception("Stations name can only be: a or b or c  or d")

    #check case: active stations are not duplicate, e.g. 'a, b, a, c'
    duplicate = []
    for i in stn_activ:
        if i in duplicate:
            raise Exception("Duplicate active stations")
        duplicate.append(i)

    #reads each active station's bit, from line 9 trans.txt
    stn_bit_str = file[9]
    stn_bit_str = stn_bit_str.strip()

    #checks case: when line 9 is blank, i.e., station's bit not present
    if len(stn_bit_str) == 0:
        raise Exception("No station's bit given")

    for i in range(len(stn_bit_str)):
        #checks case: station's bit can be '1' or '0' -> +1, +0 is not required
        if '+' in stn_bit_str[i]:
            raise Exception("No need to enter '+1' only value '1' is enough")

    #checks case: if user wrongly entered in format -> 1, 1, 0,
    if (stn_bit_str[-1]) == ',':
        raise Exception("No comma after the last station's bit name")

    stn_bit_str = stn_bit_str.split(",")

    #both case: 1, 0, 1 or 1,0,1 should be okay
    for i in range(len(stn_bit_str)):
        stn_bit_str[i] = stn_bit_str[i].strip()

    #checks case: for every active station, a bit must be transmitted.
    if len(stn_bit_str) != len(stn_activ):
        raise Exception("Each active station must transmit a bit")

    #checks case: each station's bit is only 1 or 0
    for i in range(len(stn_bit_str)):
        if stn_bit_str[i] == "1" or stn_bit_str[i] == "0":
            pass
        else:
            raise Exception("Station's bit can only be: 1 or 0")

    #stores chip seq for each station
    chip_seq = []
    for i in range(len(stn_activ)):
        try:
            if stn_bit_str[i] == "1":
                chip_seq.append(bit_seq(stn_activ[i])) #calls func bit_seq, & obtain resp. chip seq & then append
            elif stn_bit_str[i] == "0":
            #first call func. bit_seq, obtain chip seq, pass to func. not_gate, obtain negation & then append
                chip_seq.append(not_gate(bit_seq(stn_activ[i])))
            else:
                print("Please check the \"trans.txt\" file, & enter the bit inputs in the correct format")
        except Exception as e:
            print(e)
            exit(1)
    return(chip_seq)

#calculate the value S, i.e., linear addition of the individual chip sequence of active stations
def sum_seq(chip_seq):
    S=[]; i = 0
    while i < len(chip_seq[0]): #as each chip sequence is 8 bit only
        sum = 0
        for j in range(len(chip_seq)):
            sum += chip_seq[j][i] #linearly add chip sequence of active stations
        S.append(sum)
        i +=1
    return  S

#transmits S (code for the receiver to receive)
def transmit_S(S):
    S = str(S); S = S.replace('[',''); S = S.replace(']',''); #converts chip seq. from list to str
    S = S +'\n'

    #store the chip seq. in transmitter to trans.txt
    file[11] = S
    bit_sequence = open("trans.txt", "w")
    bit_sequence.writelines(file)
    bit_sequence.close()

    #transmit the sequence S to reciever, i.e.  write to receive.txt
    bit_sequence1 = open("receive.txt", "r")
    file1 = bit_sequence1.readlines()
    file1[8] = S
    bit_sequence1 = open("receive.txt", "w")
    bit_sequence1.writelines(file1)
    bit_sequence1.close()

#open file trans.txt in read mode
bit_sequence = open("trans.txt", "r")
file = bit_sequence.readlines()
try:
    isOrthogonal() #call function Walsch to check for orthogonality
except Exception as e:
    print(e)
    exit(1)
chip_seq = []
try:
    chip_seq = transmit()
except Exception as e:
    print(e)
    exit(1)
S = sum_seq(chip_seq)
transmit_S(S)
