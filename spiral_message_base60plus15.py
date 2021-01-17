base60_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
               'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,
               'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
               'Y': 24, 'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31,
               'g': 32, 'h': 33, 'i': 34, 'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39,
               'o': 40, 'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47,
               'w': 48, 'x': 49, '0': 50, '1': 51, '2': 52, '3': 53, '4': 54, '5': 55,
               '6': 56, '7': 57, '8': 58, '9': 59}

hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def read_message(m, dict):
    count = 0
    queue = []
    result = []
    base_len = len(dict.values())

    for c in m:
        count += 1

        if count == 1:
            queue.append(c)

        if count == 2:
            for n in queue:
                if n == '0':
                    result.append(dict[c])
                if n == '1':
                    result.append(dict[c] + base_len)
                if n == '2':
                    result.append(dict[c] + (base_len * 2))
                if n == '3':
                    result.append(dict[c] + (base_len * 3))
                if n == '4':
                    result.append(hex_dict[c] + (base_len * 4))

            queue.clear()
            count = 0

    return result


m = "3N3p2l361b3v26331W492a3g4704333W213M0F0X1g2H0x1R1n3I2r0P2U162L2D1t1s3H0d0s1K2D051K1O0S1D3o1L3J1G4D0G0L0x" \
    "1Q2p2a1K4E1w2Q191k3G240p224F0P3C3J1D2n1m2i1J3P2v1s2O0k1M2M0w3L3D2r0S1p153V3e3I0n3u1O0u0Z3g2U1C0Y1N3n0W3Q" \
    "22130V3c0E340W1t1D2N3H470s2p0Z340g3v1Q0s0D0K2h3D3L2x1Q202n2L1C2p0A293r0D450k2e2W253U1W2r462s2X393p0X0E1q" \
    "0q4B49483r3b3C1M1j0l4A48403m4E0s2s1v3T0I3t2B2k2t2O0e2l1L282a0J1L0c3C2o0X002Z2d1T2u1t1j0l1o1E3T183E1G270L" \
    "0v2t06111A2U4B1O2M3d2S0x0w0q0p2V180q1D492O001v2t1k3s3G213w0W292r2O2L0g3Y0M0u3i3C1r2c2q3o300a391K"

print(read_message(m, base60_dict))
