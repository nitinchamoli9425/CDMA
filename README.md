# Details #
* Programming Language: Python
* Scripts: Transmitter.py, Receiver.py
* Data is read from two text files, trans.txt for Transmitter.py & receive.txt for Receiver.py
* Chip sequences are entered in the text file, and it is ASSUMED that both sender & receiver have the same chip sequence information for any station.
* User needs to input following data in a text file in a specified format ONLY: 

    | File name  | Data | Format sample
    | ------------- | ------------- |------------- 
    |  trans.txt | Chip Sequence  | -1, -1, +1, -1, +1, +1, +1, -1
    | trans.txt  | Active Stations  | a, c, d
    | trans.txt  | Bit to be sent  | 0, 1, 1
    | receive.txt | Chip Sequence  | -1, -1, +1, -1, +1, +1, +1, -1
    | receive.txt  | Station to listen  | c
* Note: For e.g., Data input for active stations at transmitter, can only be in format "a, b, c, d" or "a,b,c,d", inputs like "abcd", "a.b.c.1" will be considered INVALID.

# Guidelines to follow: #
#### For running the program: ####
* During first time run, ALWAYS first run Transmitter.py file, then Receiver.py
* Whenever any data input is changed, ALWAYS first run Transmitter.py then Receive.py  
* If chip sequence for a station is changed in trans.txt, change the chip sequence for the same station in receive.txt
#### For entering user inputs: ####
* User needs to input required data in trans.txt and receive.txt
* It is ASSUMED that the user will input data in the required format at the specified line ONLY.

# Approach  
#### Transmitter side ### 
* All the chip sequences are read from trans.txt and checked for orthogonality.
* The bits transmitted by each active station is read from trans.txt.
* If bit 0 is transmitted then the respective chip sequence is read from trans.txt and negated.
* If bit 1 is transmitted then the respective chip sequence is read.
* Finally, all the chip sequences are linearly added, to get sequence S.
* S is written in both trans.txt & receive.txt.

#### Receiver Side ####

* The sequence S is read from receive.txt.
* The station receiver wants to listen is read from receive.txt
* The inner product of S with the interested station is obtained
* If:
    | Inner product  | Bit Received |
    | ------------- | ------------- |
    | -1  | 0  |
    | 1  | 1  |
    | 0  | not active  |

# Problem Description
This project implements CDMA (Code Division Multiple Access) concept. There can be maximum 4 stations at the transmitter side (namely: a, b, c, d), each station can transmit only 1 bit at a time (either 0 or 1).
In order to transmit a bit, each station is assigned a chip sequence of 8 bits, containing only -1 or 1 (e.g., -1, -1, +1, -1, +1, +1, +1, -1).
These chip sequences are orthogonal, i.e., the inner product of each chip sequence with itself is 1, and the inner product of each chip sequence with any other chip sequence is 0.
Any number of stations can be active at a given time, e.g., only station a can be active or a, b, c, d can be active. 
The linear addition of the active station's chip sequence is sent to the receiver.
The receiver receives this added sequence and choose which station it wants to listen to.
In order to interpret the bit sent, the receiver computes the inner product of the received sequence from sender with the chip sequence of the station it is interested in. If the value of this inner product is 1 -> bit received 1, -1 -> 0, 0 -> no bit received as station is inactive.
