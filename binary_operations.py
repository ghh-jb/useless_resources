def eight_bit_binary(binary:str) -> str:
    return  "0" * (8-len(binary)) + binary

def gParityBit(binary:str) -> int:
    One_cnt = binary.count("1")
    bit = (One_cnt % 2)
    return bit
