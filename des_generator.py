import codecs

hex_to_bin_table = {
    '0' : '0000',  '1' : '0001',  '2' : '0010',  '3' : '0011',
    '4' : '0100',  '5' : '0101',  '6' : '0110',  '7' : '0111',
    '8' : '1000',  '9' : '1001',  'a' : '1010',  'b' : '1011',
    'c' : '1100',  'd' : '1101',  'e' : '1110',  'f' : '1111'
}

hex_to_char_table = {
    
    '30' : '0', '31' : '1', '32' : '2', '33' : '3', '34' : '4', '35' : '5', '36' : '6', '37' : '7', '38' : '8',
    '39' : '9', '61' : 'a', '62' : 'b', '63' : 'c', '64' : 'd', '65' : 'e', '66' : 'f', '67' : 'g', '68' : 'h',
    '69' : 'i', '6a' : 'j', '6b' : 'k', '6c' : 'l', '6d' : 'm', '6e' : 'n', '6f' : 'o', '70' : 'p', '71' : 'q',
    '72' : 'r', '73' : 's', '74' : 't', '75' : 'u', '76' : 'v', '77' : 'w', '78' : 'x', '79' : 'y', '7a' : 'z',
    '41' : 'A', '42' : 'B', '43' : 'C', '44' : 'D', '45' : 'E', '46' : 'F', '47' : 'G', '48' : 'H', '49' : 'I',
    '4a' : 'J', '4b' : 'K', '4c' : 'L', '4d' : 'M', '4e' : 'N', '4f' : 'O', '50' : 'P', '51' : 'Q', '52' : 'R',
    '53' : 'S', '54' : 'T', '55' : 'U', '56' : 'V', '57' : 'W', '58' : 'X', '59' : 'Y', '5a' : 'Z'
}

# initial permutation table
ip_table = [
    58,   50,   42,    34,    26,   18,    10,    2,
    60,   52,   44,    36,    28,   20,    12,    4,
    62,   54,   46,    38,    30,   22,    14,    6,
    64,   56,   48,    40,    32,   24,    16,    8,
    57,   49,   41,    33,    25,   17,     9,    1,
    59,   51,   43,    35,    27,   19,    11,    3,
    61,   53,   45,    37,    29,   21,    13,    5,
    63,   55,   47,    39,    31,   23,    15,    7
]

pc1_table = [
    57,   49,    41,   33,    25,    17,    9,
     1,   58,    50,   42,    34,    26,   18,
    10,    2,    59,   51,    43,    35,   27,
    19,   11,     3,   60,    52,    44,   36,
    63,   55,    47,   39,    31,    23,   15,
     7,   62,    54,   46,    38,    30,   22,
    14,    6,    61,   53,    45,    37,   29,
    21,   13,     5,   28,    20,    12,    4
]

pc2_table = [
    14,    17,   11,    24,     1,    5,
     3,    28,   15,     6,    21,   10,
    23,    19,   12,     4,    26,    8,
    16,     7,   27,    20,    13,    2,
    41,    52,   31,    37,    47,   55,
    30,    40,   51,    45,    33,   48,
    44,    49,   39,    56,    34,   53,
    46,    42,   50,    36,    29,   32
]

left_shift_table = [
    1, 1, 2, 2,
    2, 2, 2, 2,
    1, 2, 2, 2,
    2, 2, 2, 1,
]

# for decrypt, left shift must be reversed
# right_shift_table = left_shift_table.reverse()

expansion_table = [
    32,     1,    2,     3,     4,    5,
     4,     5,    6,     7,     8,    9,
     8,     9,   10,    11,    12,   13,
    12,    13,   14,    15,    16,   17,
    16,    17,   18,    19,    20,   21,
    20,    21,   22,    23,    24,   25,
    24,    25,   26,    27,    28,   29,
    28,    29,   30,    31,    32,    1
]

# expansion reversed for decryption
# reduction_table = [
#      1,    2,     3,     4,
#      5,    6,     7,     8,
#      9,   10,    11,    12,
#     13,   14,    15,    16,
#     17,   18,    19,    20,
#     21,   22,    23,    24,
#     25,   26,    27,    28,
#     29,   30,    31,    32,
# ]


sbox_table = [
    {

        '000000':'1110', '000010':'0100', '000100':'1101', '000110':'0001', '001000':'0010', '001010':'1111', '001100':'1011', '001110':'1000',
        '010000':'0011', '010010':'1010', '010100':'0110', '010110':'1100', '011000':'0101', '011010':'1001', '011100':'0000', '011110':'0111',
        '000001':'0000', '000011':'1111', '000101':'0111', '000111':'0100', '001001':'1110', '001011':'0010', '001101':'1101', '001111':'0001',
        '010001':'1010', '010011':'0110', '010101':'1100', '010111':'1011', '011001':'1001', '011011':'0101', '011101':'0011', '011111':'1000',
        '100000':'0100', '100010':'0001', '100100':'1110', '100110':'1000', '101000':'1101', '101010':'0110', '101100':'0010', '101110':'1011',
        '110000':'1111', '110010':'1100', '110100':'1001', '110110':'0111', '111000':'0011', '111010':'1010', '111100':'0101', '111110':'0000',
        '100001':'1111', '100011':'1100', '100101':'1000', '100111':'0010', '101001':'0100', '101011':'1001', '101101':'0001', '101111':'0111',
        '110001':'0101', '110011':'1011', '110101':'0011', '110111':'1110', '111001':'1010', '111011':'0000', '111101':'0110', '111111':'1101'
        
    },

    {

        '000000':'1111', '000010':'0001', '000100':'1000', '000110':'1110', '001000':'0110', '001010':'1011', '001100':'0011', '001110':'0100',
        '010000':'1001', '010010':'0111', '010100':'0010', '010110':'1101', '011000':'1100', '011010':'0000', '011100':'0101', '011110':'1010',
        '000001':'0011', '000011':'1101', '000101':'0100', '000111':'0111', '001001':'1111', '001011':'0010', '001101':'1000', '001111':'1110',
        '010001':'1100', '010011':'0000', '010101':'0001', '010111':'1010', '011001':'0110', '011011':'1001', '011101':'1011', '011111':'0101',
        '100000':'0000', '100010':'1110', '100100':'0111', '100110':'1011', '101000':'1010', '101010':'0100', '101100':'1101', '101110':'0001',
        '110000':'0101', '110010':'1000', '110100':'1100', '110110':'0110', '111000':'1001', '111010':'0011', '111100':'0010', '111110':'1111',
        '100001':'1101', '100011':'1000', '100101':'1010', '100111':'0001', '101001':'0011', '101011':'1111', '101101':'0100', '101111':'0010',
        '110001':'1011', '110011':'0110', '110101':'0111', '110111':'1100', '111001':'0000', '111011':'0101', '111101':'1110', '111111':'1001'
        
    },

    {

        '000000':'1010', '000010':'0000', '000100':'1001', '000110':'1110', '001000':'0110', '001010':'0011', '001100':'1111', '001110':'0101',
        '010000':'0001', '010010':'1101', '010100':'1100', '010110':'0111', '011000':'1011', '011010':'0100', '011100':'0010', '011110':'1000',
        '000001':'1011', '000011':'0111', '000101':'0000', '000111':'1001', '001001':'0011', '001011':'0100', '001101':'0110', '001111':'1010',
        '010001':'0010', '010011':'1000', '010101':'0101', '010111':'1110', '011001':'1100', '011011':'1011', '011101':'1111', '011111':'0001',
        '100000':'1101', '100010':'0110', '100100':'0100', '100110':'1001', '101000':'1000', '101010':'1111', '101100':'0011', '101110':'0000',
        '110000':'1011', '110010':'0001', '110100':'0010', '110110':'1100', '111000':'0101', '111010':'1010', '111100':'1110', '111110':'0111',
        '100001':'0001', '100011':'1010', '100101':'1011', '100111':'0000', '101001':'0110', '101011':'1001', '101101':'1000', '101111':'0111',
        '110001':'0100', '110011':'1111', '110101':'1110', '110111':'0011', '111001':'1011', '111011':'0101', '111101':'0010', '111111':'1100'
        
    },

    {

        '000000':'0111', '000010':'1101', '000100':'1110', '000110':'0011', '001000':'0000', '001010':'0110', '001100':'1001', '001110':'1010',
        '010000':'0001', '010010':'0010', '010100':'1000', '010110':'0101', '011000':'1011', '011010':'1100', '011100':'0100', '011110':'1111',
        '000001':'1101', '000011':'1000', '000101':'1101', '000111':'0101', '001001':'0110', '001011':'1111', '001101':'0000', '001111':'0011',
        '010001':'0100', '010011':'0111', '010101':'0010', '010111':'1100', '011001':'0001', '011011':'1010', '011101':'1110', '011111':'1001',
        '100000':'1010', '100010':'0110', '100100':'1001', '100110':'0000', '101000':'1100', '101010':'1011', '101100':'0111', '101110':'1101',
        '110000':'1111', '110010':'0001', '110100':'0011', '110110':'1101', '111000':'0101', '111010':'0010', '111100':'1000', '111110':'0100',
        '100001':'0011', '100011':'1111', '100101':'0000', '100111':'0110', '101001':'1010', '101011':'0001', '101101':'1101', '101111':'1000',
        '110001':'1001', '110011':'0100', '110101':'0101', '110111':'1011', '111001':'1100', '111011':'0111', '111101':'0010', '111111':'1110'
        
    },

    {

        '000000':'0010', '000010':'1100', '000100':'0100', '000110':'0001', '001000':'0111', '001010':'1010', '001100':'1011', '001110':'0110',
        '010000':'1000', '010010':'0101', '010100':'0011', '010110':'1111', '011000':'1101', '011010':'0000', '011100':'1110', '011110':'1001',
        '000001':'1110', '000011':'1011', '000101':'0010', '000111':'1100', '001001':'0100', '001011':'0111', '001101':'1101', '001111':'0001',
        '010001':'0101', '010011':'0000', '010101':'1111', '010111':'1010', '011001':'0011', '011011':'1001', '011101':'1000', '011111':'0110',
        '100000':'0100', '100010':'0010', '100100':'0001', '100110':'1011', '101000':'1010', '101010':'1101', '101100':'0111', '101110':'1000',
        '110000':'1111', '110010':'1001', '110100':'1100', '110110':'0101', '111000':'0110', '111010':'0011', '111100':'0000', '111110':'0100',
        '100001':'1011', '100011':'1000', '100101':'1100', '100111':'0111', '101001':'0001', '101011':'1110', '101101':'0010', '101111':'1101',
        '110001':'0110', '110011':'1111', '110101':'0000', '110111':'1001', '111001':'1010', '111011':'0100', '111101':'0101', '111111':'0011'
        
    },

    {

        '000000':'1100', '000010':'0001', '000100':'1010', '000110':'1111', '001000':'1001', '001010':'0010', '001100':'0110', '001110':'1000',
        '010000':'0000', '010010':'1101', '010100':'0011', '010110':'0100', '011000':'1110', '011010':'0111', '011100':'0101', '011110':'1011',
        '000001':'1010', '000011':'1111', '000101':'0100', '000111':'0010', '001001':'0111', '001011':'1100', '001101':'1001', '001111':'0101',
        '010001':'0110', '010011':'0001', '010101':'1101', '010111':'1110', '011001':'0000', '011011':'1011', '011101':'0011', '011111':'1000',
        '100000':'1001', '100010':'1110', '100100':'1111', '100110':'0101', '101000':'0010', '101010':'1000', '101100':'1100', '101110':'0011',
        '110000':'0111', '110010':'0000', '110100':'0100', '110110':'1010', '111000':'0001', '111010':'1101', '111100':'1011', '111110':'0110',
        '100001':'0100', '100011':'0011', '100101':'0010', '100111':'1100', '101001':'1001', '101011':'0101', '101101':'1111', '101111':'1010',
        '110001':'1011', '110011':'1110', '110101':'0001', '110111':'0111', '111001':'0110', '111011':'0000', '111101':'1000', '111111':'1101'
        
    },

    {

        '000000':'0100', '000010':'1011', '000100':'0010', '000110':'1110', '001000':'1111', '001010':'0000', '001100':'1000', '001110':'1101',
        '010000':'0011', '010010':'1100', '010100':'1001', '010110':'0111', '011000':'0101', '011010':'1010', '011100':'0110', '011110':'0001',
        '000001':'1101', '000011':'0000', '000101':'1011', '000111':'0111', '001001':'0100', '001011':'1001', '001101':'0001', '001111':'1010',
        '010001':'1110', '010011':'0011', '010101':'0101', '010111':'1100', '011001':'0010', '011011':'1111', '011101':'1000', '011111':'0110',
        '100000':'0001', '100010':'0100', '100100':'1011', '100110':'1101', '101000':'1100', '101010':'0011', '101100':'0111', '101110':'1110',
        '110000':'1010', '110010':'1111', '110100':'0110', '110110':'1000', '111000':'0000', '111010':'0101', '111100':'1001', '111110':'0010',
        '100001':'0110', '100011':'1011', '100101':'1101', '100111':'1000', '101001':'0001', '101011':'0100', '101101':'1010', '101111':'0111',
        '110001':'1001', '110011':'0101', '110101':'0000', '110111':'1111', '111001':'1110', '111011':'0010', '111101':'0011', '111111':'1100'
        
    },

    {

        '000000':'1101', '000010':'0010', '000100':'1000', '000110':'0100', '001000':'0110', '001010':'1111', '001100':'1011', '001110':'0001',
        '010000':'1010', '010010':'1001', '010100':'0011', '010110':'1110', '011000':'0101', '011010':'0000', '011100':'1100', '011110':'0111',
        '000001':'0001', '000011':'1111', '000101':'1101', '000111':'1000', '001001':'1010', '001011':'0011', '001101':'0111', '001111':'0100',
        '010001':'1100', '010011':'0101', '010101':'0110', '010111':'1011', '011001':'0000', '011011':'1110', '011101':'1001', '011111':'0010',
        '100000':'0111', '100010':'1011', '100100':'0100', '100110':'0001', '101000':'1001', '101010':'1100', '101100':'1110', '101110':'0010',
        '110000':'0000', '110010':'0110', '110100':'1010', '110110':'1101', '111000':'1111', '111010':'0011', '111100':'0101', '111110':'1000',
        '100001':'0010', '100011':'0001', '100101':'1110', '100111':'0111', '101001':'0100', '101011':'1010', '101101':'1000', '101111':'1101',
        '110001':'1111', '110011':'1100', '110101':'1001', '110111':'0000', '111001':'0011', '111011':'0101', '111101':'0110', '111111':'1011'
        
    },
]

pbox_table = [
    16,   7,  20,  21,
    29,  12,  28,  17,
     1,  15,  23,  26,
     5,  18,  31,  10,
     2,   8,  24,  14,
    32,  27,   3,   9,
    19,  13,  30,   6,
    22,  11,   4,  25
]

invers_permutation_table = [
    40,    8,    48,    16,    56,    24,    64,    32,
    39,    7,    47,    15,    55,    23,    63,    31,
    38,    6,    46,    14,    54,    22,    62,    30,
    37,    5,    45,    13,    53,    21,    61,    29,
    36,    4,    44,    12,    52,    20,    60,    28,
    35,    3,    43,    11,    51,    19,    59,    27,
    34,    2,    42,    10,    50,    18,    58,    26,
    33,    1,    41,     9,    49,    17,    57,    25
]


## GENERATE KEY FUNCTION ##
def generate_key(key_input: str):
    hex_key = []
    bin_key = []
    # str_key = []
    # key_list = key_input
    
    # temp for 16 key output
    KEY = []
    # Check
    print('key_list: ', key_input)
    
    # convert string per char into hex
    hex_key = []
    for key in range(len(key_input)):
        for hex in hex_to_char_table:
            if key_input[key] == hex_to_char_table[hex]:
                hex_key.append(hex)
    hex_key_string = ''.join(hex_key)   # translate hex_key into string format
    # Check
    print('hex_key : ' + ''.join(hex_key))
    
    # convert hex per char into binary
    for hex_element in hex_key_string:
        # check
        print('hex_element : ' + hex_element)
        for bin_convert in hex_to_bin_table:
            if bin_convert == hex_element:
                bin_key.append(hex_to_bin_table[bin_convert])
            else:
                continue
    bin_key_string = ''.join(bin_key)
    # Check
    print('binary key: ' + bin_key_string)   # result hext to binary
    
    # empty this list
    # str_key = []
    # bin_key = bin_key_string.split()    # list format
    
    
    # check
    # print("bin_key_ : " + bin_key_string[1:8])
    
    # PC1 TABLE OPERATION
    pc1_key = []
    for pc1 in range(len(pc1_table)):
        # check
        print("pc1 : ", pc1_table[pc1])
        for binkey_el in range(len(bin_key_string)):
            #  check
            # print('binkey_el: ' + binkey_el)
            if (binkey_el == pc1_table[pc1] - 1):
                print("bin_key_string[binkey_el] : ", bin_key_string[binkey_el])
                pc1_key.append(bin_key_string[binkey_el])
                #  check
                print('=binkey_el : ', binkey_el)
                # check
                print('==pc1_table[pc1] - 1 : ', pc1_table[pc1] - 1)
            else:
                # # check
                # print("=continue=")
                continue
            
    # check
    print("pc1_key : ", pc1_key)
        
    pc1_key_string = ''.join(pc1_key)
    # check and result for soon
    print("key after permuted with PC1 table: " + pc1_key_string)   #result after permuted with PC1 table
    
    # KL = {
    #     '0':None,
    #     '1':None,  '2':None,  '3':None,  '4':None,  '5':None,  '6':None,  '7':None,  '8':None,
    #     '9':None, '10':None, '11':None, '12':None, '13':None, '14':None, '15':None, '16':None
    #     }
    # KR = {
    #     '0':None,
    #     '1':None,  '2':None,  '3':None,  '4':None,  '5':None,  '6':None,  '7':None,  '8':None,
    #     '9':None, '10':None, '11':None, '12':None, '13':None, '14':None, '15':None, '16':None
    # }
    
    # init 16 + 1 temp for keys
    # KL = dict.fromkeys(range(17))
    # KR = dict.fromkeys(range(17))
    KL_string = [
        # None,
        # None, None, None, None, None, None, None, None,
        # None, None, None, None, None, None, None, None,
        ]
    KR_string = [
        # None,
        # None, None, None, None, None, None, None, None,
        # None, None, None, None, None, None, None, None,
    ]
    
    
    # Split key into half (KL0 and KR0) [lengt of key after permut is 56 so 28 left & 28 right]
    # KL.append(pc1_key[:28])
    # KR.append(pc1_key[28:])
    KL_string.append(''.join(pc1_key[:28]))
    KR_string.append(''.join(pc1_key[28:]))
 
    # check and result for soon (list format)   
    print("KL0 after PC1 : ", KL_string[0])
    print("KR0 after PC1 : ", KR_string[0])
    
    # ITERABLE 16 ROUNDS
    for i in range(16):
        #  check
        print(" == iteration : " + str(i+1))
        # LEFT SHIFT
        if (left_shift_table[i] == 1):
            KL_shift = KL_string[i][1:28] + KL_string[i][0]
            KR_shift = KR_string[i][1:28] + KR_string[i][0]
            
            KL_string.append(KL_shift)
            KR_string.append(KR_shift)
            
            # KL.append(KL_shift)
            # KR.append(KR_shift)
            # KL[i + 1] = KL_shift
            # KR[i + 1] = KR_shift
            
            # check
            
            
            # concate left and right key
            key_cat_temp = KL_string[i+1] + KR_string[i+1]    # this is important
            # check
            print("=== KL : " + ''.join(KL_shift))
            print("=== KR : " + ''.join(KR_shift))
            print("KL_string-" + str(i+1) + " : " + KL_string[i+1])
            print("KR_string-" + str(i+1) + " : " + KR_string[i+1])
            print("key-" + str(i+1) + " : " + key_cat_temp)
            
            # REHAT SEJENAK, NANTI LANJUT CEK
            
            # KEY OPS WITH PC2 TABLE
            pc2_key_temp = []
            
            for pc2 in range(len(pc2_table)):
                for keycat_el in range(len(key_cat_temp)):
                    if (keycat_el == pc2_table[pc2] - 1):
                        pc2_key_temp.append(key_cat_temp[keycat_el])
            pc2_key_temp_string = ''.join(pc2_key_temp)
            KEY.append(pc2_key_temp_string)
            print("key after PC2 : " +  pc2_key_temp_string)
            
            
        elif (left_shift_table[i] == 2):
            KL_shift = KL_string[i][2:28] + KL_string[i][0] + KL_string[i][1]
            KR_shift = KR_string[i][2:28] + KR_string[i][0] + KR_string[i][1]
            # KL.append(KL_shift)
            # KR.append(KR_shift)
            KL_string.append(KL_shift)
            KR_string.append(KR_shift)
            
            # concate left and right key
            key_cat_temp = KL_string[i+1] + KR_string[i+1]    # this is important
            print("=== KL : " + ''.join(KL_shift))
            print("=== KR : " + ''.join(KR_shift))
            print("KL_string-" + str(i+1) + " : " + KL_string[i+1])
            print("KR_string-" + str(i+1) + " : " + KR_string[i+1])
            print("key-" + str(i+1) + " : " + key_cat_temp)
            
            # KEY OPS WITH PC2 TABLE
            pc2_key_temp = []
            for pc2 in range(len(pc2_table)):
                for keycat_el in range(len(key_cat_temp)):
                    if (keycat_el == pc2_table[pc2] - 1):
                        pc2_key_temp.append(key_cat_temp[keycat_el])
            pc2_key_temp_string = ''.join(pc2_key_temp)
            KEY.append(pc2_key_temp_string)
            # check
            print("key after PC2 : " +  pc2_key_temp_string)

    print("=====list of keys=====")
    for k in range(len(KEY)):
        # check
        print("KEY-" + str(k+1) + " : " + KEY[k])
    
    return KEY



## ENCODE FUNCTION ##
def encrypt(plain_text: str, key: str):
    print("===== ENCRYPTING =====")
    hex_text = []
    bin_text = []
    cypher_text = None
    # 1. convert message to hex
    # Check
    print('plain_text : ' + plain_text)
    
    # 1.2. Convert string per char into hex
    hex_text = []
    for text in range(len(plain_text)):
        for char in hex_to_char_table:
            # check
            # print("plain_text[text] = ", plain_text[text])
            # print("char: ", char)
            if (plain_text[text] == hex_to_char_table[char]):
                hex_text.append(char)
    # Check
    hex_text_string = ''.join(hex_text)   # translate hex_key into string format
    print('hex_text_string : ' + hex_text_string)
    
    # REHAT SEJENAK, HABIS INI LANJUT BAGIAN HEX_TEXT CONVERT KE BIN_TEXT
    
    # 2. Convert hex per char into binary
    for hex_element in hex_text_string:
        # check
        print('hex_element : ' + hex_element)
        for bin_convert in hex_to_bin_table:
            # 2.2. Check if hex2bin table equals hex elemnt per char
            if bin_convert == hex_element:
                bin_text.append(hex_to_bin_table[bin_convert])
            else:
                continue
    bin_text_string = ''.join(bin_text)
    # Check
    print('binary text : ' + bin_text_string)   # result hext to binary
    
    # 3. Initial permutation ops
    ip_text = []
    for ip in range(len(ip_table)):
        for bin in range(len(bin_text)):
            # 3.2. initial permutation by text index
            if (bin == ip_table[ip] - 1):
                ip_text.append(bin_text[bin])
                
                # check
                print("bin : ", bin)
                print("ip_table[ip] - 1 : ", ip_table[ip] - 1)
    ip_text_string = ''.join(ip_text)
    # check
    print('plain text after initial permuted : ' + ip_text_string)
    
    # 4. Slice into half (L0 & R0)
    L = [''] * 17
    R = [''] * 17
    
    L[0] = ip_text_string[:32]
    R[0] = ip_text_string[32:]
    
    # check
    print("L-0 : " + L[0])
    print("R-0 : " + R[0])
    
    
    
    # check right shift table
    # print("right_shift_table : ", left_shift_table)       
    
    # Calling generate_key function 
    K = generate_key(key)
    # print("K : ", K)
    
    ## FEISTEL FUNCTION ##
    
    ## LOOPING 16 ROUND (ENCYPHERING) ##
    for iter in range(16):
        # check
        print("L-" + str(iter+1) + " = ", R[iter])
        R_expanded = []
        
        # check
        # print("K_string", K[iter])
        
        # check string
        # R_string = R[iter]
        print("length of R_string : ", len(R[iter]), R[iter], type(R[iter]))
        
        # 5. Right text expanded with expansion table ops
        for x in range(len(expansion_table)):
            # check
            # print("R_string", R[iter])
            
            for r in range(len(R[iter])):
                if (r == expansion_table[x] - 1):
                    R_expanded.append(R[iter][r])
                    
                    # check
                    # print("k-" + str(r+1) + " : " + str(r))
                    # print("expansion_table[x] - 1 : ", expansion_table[x] - 1)
        
        R_expanded_string = ''.join(R_expanded)    
        # check
        print("==> R_expanded_string : ", R_expanded_string)
                
        ## REHAT SEJENAK, NANTI LANJUT BAGIAN MASUKKAN EXPANDED R[iter] DAN DI XOR DENAGN KEY[ITER]
        ## LALU MASUKKAN KE VARIABEL "A"
    
        # not yet fix
        # 6. XOR ops expanded R_text[i-1] with K[i]
        R_text_xor_string = ''
        R_text_xor = []
        key_round = K[iter]
        
        # check
        print("R_expanded_string: ", R_expanded_string)
        
        for i in range(48):
            if (R_expanded_string[i] == key_round[i]):
                R_text_xor.append('0')
            elif(R_expanded_string[i] != key_round[i]):
                R_text_xor.append('1')
              
        # this is A[iter]
        R_text_xor_string = ''.join(R_text_xor)
        # # check
        print('R_text_xor_string[' + str(iter+1) + "] = " + R_text_xor_string)
        
        # 7. Convert into A[iter] (6 basis binary)
        A = [(R_text_xor_string[el:el+6]) for el in range(0, len(R_text_xor_string), 6)]
        # check
        print("==> A = ", A)
            
        
        # 8. S Box ops for R_text_xor_string (A1[iter])
        A_sbox = []
        for A_element in range(len(A)):
            # check
            print("A_element : ", A[A_element])
            A_sbox_get = sbox_table[A_element].get(A[A_element])
            A_sbox.append(A_sbox_get)
            # check
            print("A_sbox_get: ", A_sbox_get)
            
            # for sbox_element in range(len(sbox_table)):
            #     for sbox_element_inner in range(len(sbox_table[sbox_element])): 
            #         sbox_key = sbox_table[sbox_element].keys()   
            #         print("sbox_element_inner : ", sbox_key)
            #         if (sbox_key == A[A_element]):
            #             A_sbox.append(sbox_table[sbox_element].values())
            #         else:
            #             continue
        # check
        print("A_sbox : ", A_sbox)    
        
        # S BOX DONE, REHAT DULU NTAR LANJUT P BOX VARIABELNYA JADI "B"
        
        # 9. Ops A_sbox with P BOX
        A_sbox_string = ''.join(A_sbox)
        B_pbox = []
        for pbox in range(len(pbox_table)):
            for A_sbox_element in range(len(A_sbox_string)):
                if (A_sbox_element == pbox_table[pbox] - 1):
                    B_pbox.append(A_sbox_string[A_sbox_element])
                else:
                    continue
        B_pbox_string = ''.join(B_pbox)
        # check
        print("B_pbox: ", B_pbox)
        # check
        print("B_pbox_string: " + B_pbox_string)
        
        # L_string[iter + 1] = ''
        # 10. Ops XOR B_pbox_string with L[iter] => L[iter] is L[i - 1]
        # 32 bit of R_pbox and L_string
        R[iter + 1] = ''
        R_pbox = []
        L_iter = L[iter]
        for i_element in range(32):
            if (L_iter[i_element] == B_pbox_string[i_element]):
                R_pbox.append('0')
            elif (L_iter[i_element] != B_pbox_string[i_element]):
                R_pbox.append('1')
        R_pbox_string = ''.join(R_pbox)
        # check
        print("R_pbox_string = " + R_pbox_string)
        
        # 11. Add L[iter + 1] from R[iter] with all of its computation
        L[iter + 1] = R_pbox_string
        # check
        print("L = " + L[iter + 1])
        
        # 12. Add R[iter + 1] from L[iter]
        R[iter + 1] = L[iter]
        # check
        print("R = " + R[iter + 1])
        
        # 13. Concate L & R
        # wait check if iter == 15 (16th round), swap into R & L then concate
        # then ops with invers permutation table
        if (iter == 15):
            swap_text_join = []
            
            R_swap = L[iter + 1]
            L_swap = R[iter + 1]
            
            join_temp = L_swap + R_swap 
            swap_text_join.append(join_temp)
            swap_text_join_string = ''.join(swap_text_join)
            # check
            print("L_swap: " + L_swap)
            print("R_swap: " + R_swap)
            print("swap_text_join_string = " + swap_text_join_string)
            
            
            # 14. Invers permutation ops with swap_text_join_string
            invers_permutation = []
            # cypher_text = ''
            for ip in range(len(invers_permutation_table)):
                for el in range(len(swap_text_join_string)):
                    if (el == invers_permutation_table[ip] - 1):
                        invers_permutation.append(swap_text_join_string[el])
            invers_permutation_string = ''.join(invers_permutation)
            # check
            print('invers_permutation_string : ' + invers_permutation_string)
            
            ## REHAT SEJENAK, HABIS INI LANJUT KONVERSI BINARY KE HEX ##
            
            # 15. Convert binary to hex
            final_bin_text = []
            bin_4basis = [(invers_permutation_string[el : el + 4]) for el in range(0, len(invers_permutation_string), 4)]
            # check
            print('bin_4basis = ', bin_4basis)
            for bin in range(len(bin_4basis)):
                for hex_bin_value in hex_to_bin_table:
                    # print(hex_bin_value)
                    if (bin_4basis[bin] == hex_to_bin_table[hex_bin_value]):
                        # check
                        print("bin_4basis : ", bin_4basis[bin])
                        print("hex_bin_value : ", hex_to_bin_table[hex_bin_value])
                        print("hex_bin_key : ", hex_bin_value)
                        
                        final_bin_text.append(hex_bin_value)
            # Check
            final_bin_text_string = ''.join(final_bin_text)
            print("final_bin_text : ", final_bin_text_string)

            # print(bytes.fromhex('5e1af11ffa33bcda').decode('ascii'))
            # 16. Decode hex into ascii
            # byte_data = [int(final_bin_text_string[i:i+2], 16) for i in range(0, len(final_bin_text_string), 2)]
            # test
            # temp_str = "0x68656c6f"[2:]
            cypher_text = final_bin_text_string
            # print("byte_data : ", byte_data)
            # cypher_text = byte_data.decode('utf-8')
            # check
            # print("cypher_text : ", cypher_text)
            
    return [plain_text, key, cypher_text]    


## DECRYPT FUNCTION ##
def decrypt(cypher_hex: str, key: str):
    # 0. Make key in reverse order
    key_temp = generate_key(key)
    key_reverse = list(reversed(key_temp))
    # check
    print("key_reverse: ", key_reverse)
    
    # Global variable for return
    plain_text = None
    plain_text_string = None
    
    # 1. Convert cypher_hex to binary
    cypher_bin = []
    for hex in range(len(cypher_hex)):
        print("hex: ", hex)
        for k, val in hex_to_bin_table.items():
            # print("k: ", k)
            # print("val: ", val)
            if (cypher_hex[hex] == k):
                print("hexbin_k: ", k)
                cypher_bin.append(val)
    cypher_bin_string = ''.join(cypher_bin)
    # check
    print("cypher_bin_string: " + cypher_bin_string)
    
    # 2. Ops cypher_bin_string with initial permutation matrix table
    ip_bin = []
    # cypher_text = ''
    for ip in range(len(ip_table)):
        for el in range(len(cypher_bin_string)):
            if (el == ip_table[ip] - 1):
                ip_bin.append(cypher_bin_string[el])
    ip_bin_string = ''.join(ip_bin)
    # check
    print('ip_bin_string    : ' + ip_bin_string)
    
    # ini setelah invers
    # 3. Split into half (L & R), 32 bit & and swap
    L = [''] * 17
    R = [''] * 17
    # divide & swap
    L[0] = ip_bin_string[32:]
    R[0] = ip_bin_string[:32]
    # check
    print("L[0] : ", L[0])
    print("R[0] : ", R[0])
    
    # looping through 16 keys
    for iter in range(16):
        # check
        print("==> d_iter : ", str(iter + 1))
        
        # 4. Append R[i] into L[i + 1]
        L[iter + 1] = R[iter]
        
        # ops left side reverse for decrypting (for R[n-1] value)
        # 5. Expand L with expansion table (length is 32 bit to 48 bit)
        R_iter_string = R[iter]
        R_expand = []
        for exp_i in range(len(expansion_table)):
            # check
            # print("iter-" + str(exp_i))
            for r in range(len(R_iter_string)):
                if (r == expansion_table[exp_i] - 1):
                    R_expand.append(R_iter_string[r])
        R_expand_string = ''.join(R_expand)
        # check
        print("R_expand_string : " + R_expand_string)
        
        # 6. XOR reverse key with R_expand_string
        R_xor_key = []
        key_round = key_reverse[iter]
        for xor_i in range(48):
            if(R_expand_string[xor_i] == key_round[xor_i]):
                R_xor_key.append('0')
            elif(R_expand_string[xor_i] != key_round[xor_i]):
                R_xor_key.append('1')
        R_xor_key_string = ''.join(R_xor_key)
        # check
        print("R_xor_key_string = " + R_xor_key_string)
        
        # REHAT SEJENAK, HABIS INI LANJUT OPS S BOX DENGAN R_xor_key_string
         
        # 7. Convert into A[iter] (6 basis binary)
        A = [(R_xor_key_string[el:el+6]) for el in range(0, len(R_xor_key_string), 6)]
        # check
        print("==> A = ", A)
        
        # 8. OPS S BOX with R_xor_key_string (32 bit => 8 * 4 bit)
        A_sbox = []
        for A_element in range(len(A)):
            # check
            print("A_element : ", A[A_element])
            A_sbox_get = sbox_table[A_element].get(A[A_element])
            A_sbox.append(A_sbox_get)
            # check
            print("A_sbox_get: ", A_sbox_get)
        A_sbox_string = ''.join(A_sbox)
        # check
        print("A_sbox_string = " + A_sbox_string)
        
        # 9. Ops A_sbox_string with P BOX table
        B_pbox = []
        for pbox_element in range(len(pbox_table)):
            for A_sbox_element in range(len(A_sbox_string)):
                if (A_sbox_element == pbox_table[pbox_element] - 1):
                    B_pbox.append(A_sbox_string[A_sbox_element])
        B_pbox_string = ''.join(B_pbox)
        # check
        print("B_pbox_string = " + B_pbox_string)
        
        # 10. Ops B_pbox_string XOR with L[iter] as R_prev
        R_prev = L[iter]
        L_next = []
        for i in range(32):
            if (R_prev[i] == B_pbox_string[i]):
                L_next.append('0')
            elif (R_prev[i] != B_pbox_string[i]):
                L_next.append('1')
        L_next_string = ''.join(L_next)
        # check
        print(R_prev)
        print("L_next = " + L_next_string)
        
        # 11. add L_next_string into R[iter + 1]
        R[iter + 1] = L_next_string
        
        # Check if last iteration of 16, then combine R[15] + L[15]
        if (iter == 15):
            # 12. swap position to R + L
            temp_plain = R[iter + 1] + L[iter + 1]
            # check
            print("temp_plain = " + temp_plain)
            
            
            # 13. invers temp_plain
            plain_invers = []
            for invers in range(len(invers_permutation_table)):
                for plain_el in range(len(temp_plain)):
                    if (plain_el == invers_permutation_table[invers] - 1):
                        plain_invers.append(temp_plain[plain_el])
                    else:
                        continue
            plain_invers_string = ''.join(plain_invers)
            # check
            print("plain_invers_string = " + plain_invers_string)
            
            # 14. Divide plain_invers_string into 4 bit biner
            plain_binhex = [(plain_invers_string[el:el + 4]) for el in range(0, len(plain_invers_string), 4)]
            # check
            print("plain_binhex = ", plain_binhex)
            
            # 15. Convert plain_binhex into hex
            plain_hex = []
            for biner in range(len(plain_binhex)):
                for hexbin in hex_to_bin_table:
                    if (plain_binhex[biner] == hex_to_bin_table[hexbin]):
                        plain_hex.append(hexbin)
            plain_hex_string = ''.join(plain_hex)
            print("plain_hex_string = " + plain_hex_string)
            
            # 16. Convert hex into char and add to return value variable
            hex_list = [(plain_hex_string[el:el + 2]) for el in range(0, len(plain_hex_string), 2)]
            plain_text = []
            print("hex_list : ", hex_list, "length : ", len(hex_list))
            for hex_list_el in range(len(hex_list)):
                print('hex_list[hex_el] : ', hex_list[hex_list_el])
                
                for hexchar in hex_to_char_table:
                    # check
                    # print('hex_list[hex_el] : ', hex_list[hex_el])
                    # print("hexchar : ", hexchar)
                    if (hex_list[hex_list_el] == hexchar):
                        plain_text.append(hex_to_char_table[hexchar])
                        
            plain_text_string = ''.join(plain_text)
            # plain_new = bytes.fromhex(''.join(hex_list)).decode('utf-8')
            # check
            print("plain_text_string = ", plain_text_string)
    return [cypher_hex, key, plain_text_string]    
                
        


# # ## DECRYPT FUNCTION ##
# def decrypt(cypher_hex: str, key: str):
#     key_reverse = list(reversed(key))
#     key_reverse_string = ''.join(key_reverse)
#     cypher_text, keygen, plain_text = encrypt(cypher_hex, key)
#     decoded_plain_text = bytes.fromhex(plain_text)
#     print("key = ", key)
#     print("key_reverse_string = ", key_reverse_string)
#     print("cypher_text = ", cypher_text)
#     print("keygen = ", keygen)
#     print("plain_text = ", bytes.fromhex(plain_text).decode("utf-8"))
    


# if __name__ == '__main__':
#     decrypt('636f6d7075746572', 'computer')
    # encrypt('computer', 'computer')
#     # generate_key('computer')
    
    
    
## references ##

# https://www.geeksforgeeks.org/python-split-string-in-groups-of-n-consecutive-characters/
# 
    
    
    