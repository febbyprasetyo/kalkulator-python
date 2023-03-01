from Hitung import Hitung

ulang = "LANJUT"
while ulang == "LANJUT" :
    a = input( ' Bilangan a : ' )
    b = input( ' Bilangan b : ' )

    objek = Hitung( a, b )

    print( ' Pilihan operasi ' )
    print( ' [1] kali ' )
    print( ' [2] bagi ' )
    print( ' [3] tambah ' )
    print( ' [4] kurang ' )
    operasi = input( 'Pilih ? ' )

    if operasi == '1' :
        hasil = objek.kali()
        print( ' Hasil Kali :' , hasil)
    elif operasi == '2' :
        hasil = objek.bagi()
        print( ' Hasil bagi :' , hasil)
    elif operasi == '3' :
        hasil = objek.tambah()
        print( ' Hasil tambah :' , hasil)
    elif operasi == '4' :
        hasil = objek.kurang()
        print( ' Hasil kurang :' , hasil)
    
    else :
        print( ' Tidak ada pilihan operasi ')
        print(' Program Selesai')
    
    ulang = input('Isi lagi? BERHENTI/ LANJUT : ')  
    