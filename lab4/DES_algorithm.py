P = [
    16, 7, 20, 21, 
    29, 12, 28, 17,
    1, 15, 23, 26, 
    5, 18, 31, 10,
    2, 8, 24, 14, 
    32, 27, 3, 9,
    19, 13, 30, 6, 
    22, 11, 4, 25
]

def permute_P(input_block):
    permuted_block = ""
    for p in P:
        permuted_block += input_block[p - 1]
    return permuted_block

S_values = input("Enter S-values (32 bits): ")
Li_minus_1 = input("Enter Li-1 (32 bits): ")

if len(S_values) != 32 or len(Li_minus_1) != 32:
    print("Both S-values and Li-1 should be 32 bits long.")
else:
    f_result = S_values

    f_permuted = permute_P(f_result)

    f_permuted_with_blocks = ' '.join([f_permuted[i:i+4] for i in range(0, 32, 4)])

    print("f using the P permutation table: " + f_permuted_with_blocks)

    Ri = ""
    for i in range(32):
        Ri += str(int(Li_minus_1[i]) ^ int(f_permuted[i]))

    Ri_with_blocks = ' '.join([Ri[i:i+4] for i in range(0, 32, 4)])

    print("Resulting Ri: " + Ri_with_blocks)
