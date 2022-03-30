print("Program Menginap di Hotel")
print("           : Superior        : Deluxe           : Premium        :")
print("-----------:-----------------:------------------:----------------:")
print("1-2 Hari   : 100.000/night   : 150.000/night    : 200.000/night  :")
print("3-4 Hari   : 90.000/night    : 135.000/night    : 180.000/night  :")
print(">5 Hari    : 80.000/night    : 120.000/night    : 160.000/night  :")
print("-----------:-----------------:------------------:----------------:")
print("TIPE KAMAR")
print("1. SUPERIOR")
print("2. DELUXE")
print("3. PREMIUM")

tipe_kamar = input("MASUKKAN TIPE KAMAR : ")
lama_inap = int(input("LAMA WAKTU PENGINAPAN : "))

if tipe_kamar == "1":
    if lama_inap <= 2:
        total_harga = 100000
    elif lama_inap <= 4:
        total_harga = 90000
    elif lama_inap >= 5:
        total_harga = 80000*lama_inap
    else:
        total_harga = 50000*lama_inap

if tipe_kamar == "2":
    if lama_inap <= 2:
        total_harga = 150000
    elif lama_inap <= 4:
        total_harga = 135000
    elif lama_inap >= 5:
        total_harga = 120000*lama_inap
    else:
        total_harga = 75000*lama_inap

if tipe_kamar == "3":
    if lama_inap <= 2:
        total_harga = 200000
    elif lama_inap <= 4:
        total_harga = 180000
    elif lama_inap >= 5:
        total_harga = 160000*lama_inap
    else:
        total_harga = 10000*lama_inap

print("TIPE KAMAR : ", (tipe_kamar))
print("LAMA INAP : ", (lama_inap))
print("TOTAL HARGA : ", (total_harga))

home = input("Ingin memesan lagi (Y/N) ? ")
back = print("")

if home == "Y":
    
    print("TIPE KAMAR")
    print("1. SUPERIOR")
    print("2. DELUXE")
    print("3. PREMIUM")

    tipe_kamar = input("MASUKKAN TIPE KAMAR : ")
    lama_inap = int(input("LAMA WAKTU PENGINAPAN : "))

    if tipe_kamar == "1":
        if lama_inap <= 2:
            total_harga = 100000
        elif lama_inap <= 4:
            total_harga = 90000
        elif lama_inap >= 5:
            total_harga = 80000*lama_inap
        else:
            total_harga = 50000*lama_inap

    if tipe_kamar == "2":
        if lama_inap <= 2:
            total_harga = 150000
        elif lama_inap <= 4:
            total_harga = 135000
        elif lama_inap >= 5:
            total_harga = 120000*lama_inap
        else:
            total_harga = 75000*lama_inap

    if tipe_kamar == "3":
        if lama_inap <= 2:
            total_harga = 200000
        elif lama_inap <= 4:
            total_harga = 180000
        elif lama_inap >= 5:
            total_harga = 160000*lama_inap
        else:
            total_harga = 10000*lama_inap

    print("TIPE KAMAR : ", (tipe_kamar))
    print("LAMA INAP : ", (lama_inap))
    print("TOTAL HARGA : ", (total_harga))

    home = input("Ingin memesan lagi (Y/N) ? ")
    back = print("")
else:
    back

if home == "Y":
    
    print("TIPE KAMAR")
    print("1. SUPERIOR")
    print("2. DELUXE")
    print("3. PREMIUM")

    tipe_kamar = input("MASUKKAN TIPE KAMAR : ")
    lama_inap = int(input("LAMA WAKTU PENGINAPAN : "))

    if tipe_kamar == "1":
        if lama_inap <= 2:
            total_harga = 100000
        elif lama_inap <= 4:
            total_harga = 90000
        elif lama_inap >= 5:
            total_harga = 80000*lama_inap
        else:
            total_harga = 50000*lama_inap

    if tipe_kamar == "2":
        if lama_inap <= 2:
            total_harga = 150000
        elif lama_inap <= 4:
            total_harga = 135000
        elif lama_inap >= 5:
            total_harga = 120000*lama_inap
        else:
            total_harga = 75000*lama_inap

    if tipe_kamar == "3":
        if lama_inap <= 2:
            total_harga = 200000
        elif lama_inap <= 4:
            total_harga = 180000
        elif lama_inap >= 5:
            total_harga = 160000*lama_inap
        else:
            total_harga = 10000*lama_inap

    print("TIPE KAMAR : ", (tipe_kamar))
    print("LAMA INAP : ", (lama_inap))
    print("TOTAL HARGA : ", (total_harga))

    home = input("Ingin memesan lagi (Y/N) ? ")
    back = print("")
else:
    back

if home == "Y":
    
    print("TIPE KAMAR")
    print("1. SUPERIOR")
    print("2. DELUXE")
    print("3. PREMIUM")

    tipe_kamar = input("MASUKKAN TIPE KAMAR : ")
    lama_inap = int(input("LAMA WAKTU PENGINAPAN : "))

    if tipe_kamar == "1":
        if lama_inap <= 2:
            total_harga = 100000
        elif lama_inap <= 4:
            total_harga = 90000
        elif lama_inap >= 5:
            total_harga = 80000*lama_inap
        else:
            total_harga = 50000*lama_inap

    if tipe_kamar == "2":
        if lama_inap <= 2:
            total_harga = 150000
        elif lama_inap <= 4:
            total_harga = 135000
        elif lama_inap >= 5:
            total_harga = 120000*lama_inap
        else:
            total_harga = 75000*lama_inap

    if tipe_kamar == "3":
        if lama_inap <= 2:
            total_harga = 200000
        elif lama_inap <= 4:
            total_harga = 180000
        elif lama_inap >= 5:
            total_harga = 160000*lama_inap
        else:
            total_harga = 10000*lama_inap

    print("TIPE KAMAR : ", (tipe_kamar))
    print("LAMA INAP : ", (lama_inap))
    print("TOTAL HARGA : ", (total_harga))

    home = input("Ingin memesan lagi (Y/N) ? ")
    back = print("")
else:
    back

if home == "Y":
    
    print("TIPE KAMAR")
    print("1. SUPERIOR")
    print("2. DELUXE")
    print("3. PREMIUM")

    tipe_kamar = input("MASUKKAN TIPE KAMAR : ")
    lama_inap = int(input("LAMA WAKTU PENGINAPAN : "))

    if tipe_kamar == "1":
        if lama_inap <= 2:
            total_harga = 100000
        elif lama_inap <= 4:
            total_harga = 90000
        elif lama_inap >= 5:
            total_harga = 80000*lama_inap
        else:
            total_harga = 50000*lama_inap

    if tipe_kamar == "2":
        if lama_inap <= 2:
            total_harga = 150000
        elif lama_inap <= 4:
            total_harga = 135000
        elif lama_inap >= 5:
            total_harga = 120000*lama_inap
        else:
            total_harga = 75000*lama_inap

    if tipe_kamar == "3":
        if lama_inap <= 2:
            total_harga = 200000
        elif lama_inap <= 4:
            total_harga = 180000
        elif lama_inap >= 5:
            total_harga = 160000*lama_inap
        else:
            total_harga = 10000*lama_inap

    print("TIPE KAMAR : ", (tipe_kamar))
    print("LAMA INAP : ", (lama_inap))
    print("TOTAL HARGA : ", (total_harga))

    home = input("Ingin memesan lagi (Y/N) ? ")
    back = print("")
else:
    back

if home == "Y":
    
    print("TIPE KAMAR")
    print("1. SUPERIOR")
    print("2. DELUXE")
    print("3. PREMIUM")

    tipe_kamar = input("MASUKKAN TIPE KAMAR : ")
    lama_inap = int(input("LAMA WAKTU PENGINAPAN : "))

    if tipe_kamar == "1":
        if lama_inap <= 2:
            total_harga = 100000
        elif lama_inap <= 4:
            total_harga = 90000
        elif lama_inap >= 5:
            total_harga = 80000*lama_inap
        else:
            total_harga = 50000*lama_inap

    if tipe_kamar == "2":
        if lama_inap <= 2:
            total_harga = 150000
        elif lama_inap <= 4:
            total_harga = 135000
        elif lama_inap >= 5:
            total_harga = 120000*lama_inap
        else:
            total_harga = 75000*lama_inap

    if tipe_kamar == "3":
        if lama_inap <= 2:
            total_harga = 200000
        elif lama_inap <= 4:
            total_harga = 180000
        elif lama_inap >= 5:
            total_harga = 160000*lama_inap
        else:
            total_harga = 10000*lama_inap

    print("TIPE KAMAR : ", (tipe_kamar))
    print("LAMA INAP : ", (lama_inap))
    print("TOTAL HARGA : ", (total_harga))

    home = input("Ingin memesan lagi (Y/N) ? ")
    back = print("")
else:
    back

if home == "Y":
    
    print("TIPE KAMAR")
    print("1. SUPERIOR")
    print("2. DELUXE")
    print("3. PREMIUM")

    tipe_kamar = input("MASUKKAN TIPE KAMAR : ")
    lama_inap = int(input("LAMA WAKTU PENGINAPAN : "))

    if tipe_kamar == "1":
        if lama_inap <= 2:
            total_harga = 100000
        elif lama_inap <= 4:
            total_harga = 90000
        elif lama_inap >= 5:
            total_harga = 80000*lama_inap
        else:
            total_harga = 50000*lama_inap

    if tipe_kamar == "2":
        if lama_inap <= 2:
            total_harga = 150000
        elif lama_inap <= 4:
            total_harga = 135000
        elif lama_inap >= 5:
            total_harga = 120000*lama_inap
        else:
            total_harga = 75000*lama_inap

    if tipe_kamar == "3":
        if lama_inap <= 2:
            total_harga = 200000
        elif lama_inap <= 4:
            total_harga = 180000
        elif lama_inap >= 5:
            total_harga = 160000*lama_inap
        else:
            total_harga = 10000*lama_inap

    print("TIPE KAMAR : ", (tipe_kamar))
    print("LAMA INAP : ", (lama_inap))
    print("TOTAL HARGA : ", (total_harga))

    home = input("Ingin memesan lagi (Y/N) ? ")
    back = print("")
else:
    back

if home == "Y":
    
    print("TIPE KAMAR")
    print("1. SUPERIOR")
    print("2. DELUXE")
    print("3. PREMIUM")

    tipe_kamar = input("MASUKKAN TIPE KAMAR : ")
    lama_inap = int(input("LAMA WAKTU PENGINAPAN : "))

    if tipe_kamar == "1":
        if lama_inap <= 2:
            total_harga = 100000
        elif lama_inap <= 4:
            total_harga = 90000
        elif lama_inap >= 5:
            total_harga = 80000*lama_inap
        else:
            total_harga = 50000*lama_inap

    if tipe_kamar == "2":
        if lama_inap <= 2:
            total_harga = 150000
        elif lama_inap <= 4:
            total_harga = 135000
        elif lama_inap >= 5:
            total_harga = 120000*lama_inap
        else:
            total_harga = 75000*lama_inap

    if tipe_kamar == "3":
        if lama_inap <= 2:
            total_harga = 200000
        elif lama_inap <= 4:
            total_harga = 180000
        elif lama_inap >= 5:
            total_harga = 160000*lama_inap
        else:
            total_harga = 10000*lama_inap

    print("TIPE KAMAR : ", (tipe_kamar))
    print("LAMA INAP : ", (lama_inap))
    print("TOTAL HARGA : ", (total_harga))

    home = input("Ingin memesan lagi (Y/N) ? ")
    back = print("")
else:
    back

if home == "Y":
    
    print("TIPE KAMAR")
    print("1. SUPERIOR")
    print("2. DELUXE")
    print("3. PREMIUM")

    tipe_kamar = input("MASUKKAN TIPE KAMAR : ")
    lama_inap = int(input("LAMA WAKTU PENGINAPAN : "))

    if tipe_kamar == "1":
        if lama_inap <= 2:
            total_harga = 100000
        elif lama_inap <= 4:
            total_harga = 90000
        elif lama_inap >= 5:
            total_harga = 80000*lama_inap
        else:
            total_harga = 50000*lama_inap

    if tipe_kamar == "2":
        if lama_inap <= 2:
            total_harga = 150000
        elif lama_inap <= 4:
            total_harga = 135000
        elif lama_inap >= 5:
            total_harga = 120000*lama_inap
        else:
            total_harga = 75000*lama_inap

    if tipe_kamar == "3":
        if lama_inap <= 2:
            total_harga = 200000
        elif lama_inap <= 4:
            total_harga = 180000
        elif lama_inap >= 5:
            total_harga = 160000*lama_inap
        else:
            total_harga = 10000*lama_inap

    print("TIPE KAMAR : ", (tipe_kamar))
    print("LAMA INAP : ", (lama_inap))
    print("TOTAL HARGA : ", (total_harga))

    home = input("Ingin memesan lagi (Y/N) ? ")
    back = print("")
else:
    back

if home == "Y":
    
    print("TIPE KAMAR")
    print("1. SUPERIOR")
    print("2. DELUXE")
    print("3. PREMIUM")

    tipe_kamar = input("MASUKKAN TIPE KAMAR : ")
    lama_inap = int(input("LAMA WAKTU PENGINAPAN : "))

    if tipe_kamar == "1":
        if lama_inap <= 2:
            total_harga = 100000
        elif lama_inap <= 4:
            total_harga = 90000
        elif lama_inap >= 5:
            total_harga = 80000*lama_inap
        else:
            total_harga = 50000*lama_inap

    if tipe_kamar == "2":
        if lama_inap <= 2:
            total_harga = 150000
        elif lama_inap <= 4:
            total_harga = 135000
        elif lama_inap >= 5:
            total_harga = 120000*lama_inap
        else:
            total_harga = 75000*lama_inap

    if tipe_kamar == "3":
        if lama_inap <= 2:
            total_harga = 200000
        elif lama_inap <= 4:
            total_harga = 180000
        elif lama_inap >= 5:
            total_harga = 160000*lama_inap
        else:
            total_harga = 10000*lama_inap

    print("TIPE KAMAR : ", (tipe_kamar))
    print("LAMA INAP : ", (lama_inap))
    print("TOTAL HARGA : ", (total_harga))

    home = input("Ingin memesan lagi (Y/N) ? ")
    back = print("")
else:
    back
