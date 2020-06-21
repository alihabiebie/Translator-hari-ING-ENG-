loop = True
hari = {
    "Senin" : "Monday", 
    "Selasa" : "Tuesday",
    "Rabu" : "Wednesday",
    "Kamis" : "Thursday",
    "Jumat" : "Friday",
    "Sabtu" : "Saturday",
    "Minggu" : "Sunday"
}

print("====================================")
print("==Aplikasi Translator Hari IND/ENG==")
print("=IND/ENG Day Translator Application=")
print("====================================")
print("===============MENU=================")
print("= 1.        IND to ENG             =")
print("= 2.        ENG to IND             =")
print("= 3.          Keluar               =")
while(loop):
    try:
        menu = int(input("Masukkan menu yang dipilih/Enter the selected menu: "))
        if menu == 1:
            ind = input("Masukkan Nama Hari: ").title()
            print("Hari", ind, "Dalam bahasa inggris adalah", hari[ind])
        elif menu == 2:
            eng = input("Please Input the Name of the day: ").title()
            transpose = hari.items()
            for key,value in transpose:
                if eng == value:
                    print(eng, "in bahasa is", key)
                    break
        elif menu == 3:
            print("Terima Kasih Telah Menggunakan Apllikasi ini/Thank you for using this Application")
            loop = False
        else:
            print("Menu yang kamu masukan tidak tersedia/ The menu you entered is not available")
    except:
        print("Menu yang kamu masukan tidak tersedia/ The menu you entered is not available")