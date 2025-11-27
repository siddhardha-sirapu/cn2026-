def crc_encode():
    polynomial = input("ENTER POLYNOMIAL: ")
    frame = input("ENTER THE FRAME: ")

    m = len(polynomial)
    n = len(frame)

    for i in range(m):
        if polynomial[i] == '1':
            polynomial = polynomial[i:]
            m = len(polynomial)
            break

    polynomial = list(polynomial)

    cl = m + n - 1
    c = list(frame) + ['0'] * (cl - n)  

    for i in range(n):
        if c[i] == '1':
            for j in range(m):
                c[i + j] = '0' if polynomial[j] == c[i + j] else '1'

    c[:n] = frame

    message = ''.join(c)
    print(f"\nTHE MESSAGE IS: {message}")

crc_encode()