def convert(s):
    new = ""

    for x in s:
        new += x

    return new

def split_message(m):
    count = 0
    result = [[], [], [], [], []]
    queue = []

    for c in m:
        count += 1

        if count == 1:
            queue.append(c)

        if count == 2:
            for n in queue:
                for i in range(0, 5):
                    if n == '{}'.format(i):
                        result[i].append(c)

            queue.clear()
            count = 0

    for i in result:
        print(convert(i))


m = "3N3p2l361b3v26331W492a3g4704333W213M0F0X1g2H0x1R1n3I2r0P2U162L2D1t1s3H0d0s1K2D051K1O0S1D3o1L3J1G4D0G0L0x" \
    "1Q2p2a1K4E1w2Q191k3G240p224F0P3C3J1D2n1m2i1J3P2v1s2O0k1M2M0w3L3D2r0S1p153V3e3I0n3u1O0u0Z3g2U1C0Y1N3n0W3Q" \
    "22130V3c0E340W1t1D2N3H470s2p0Z340g3v1Q0s0D0K2h3D3L2x1Q202n2L1C2p0A293r0D450k2e2W253U1W2r462s2X393p0X0E1q" \
    "0q4B49483r3b3C1M1j0l4A48403m4E0s2s1v3T0I3t2B2k2t2O0e2l1L282a0J1L0c3C2o0X002Z2d1T2u1t1j0l1o1E3T183E1G270L" \
    "0v2t06111A2U4B1O2M3d2S0x0w0q0p2V180q1D492O001v2t1k3s3G213w0W292r2O2L0g3Y0M0u3i3C1r2c2q3o300a391K"

split_message(m)

# 4FXxPds5SGLxpPkwSnuZYWVEWsZgsDKADkXEqlsIeJcX0lLv6xwqpq0WgMua
# bWgRn6tsKKODLGQKw9kDmJsMp5OCN3tDQQCWqMjvLLTtjoE8G1AO8DvkrK
# l6a1HrULDDpaQ42nivOMrU2Nphx0nLp9eW5rsXsBktOl8aoZdu7tUMSVOt19rOLcq
# Np6v3g3WMIHoJGCJPLDVeIugnQc4H4vDLrU9prbCmTtCTEdsGwYiCo09
# 97DEF756B98A80EB9
