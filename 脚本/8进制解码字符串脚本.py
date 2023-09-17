dump = "0000000 051516 041523 043124 062173 062545 034463 063144 026467 0000020 034460 032060 032055 061070 026471 030470 030544 033455 0000040 030141 034066 034470 062067 032145 076467 000012 0000055"
octs = [("0o" + n) for n in  dump.split(" ") if n]
hexs = [int(n, 8) for n in octs]
result = ""
for n in hexs:
    if (len(hex(n)) > 4):
        swapped = hex(((n << 8) | (n >> 8)) & 0xFFFF)
        result += swapped[2:].zfill(4)
print(bytes.fromhex(result).decode())