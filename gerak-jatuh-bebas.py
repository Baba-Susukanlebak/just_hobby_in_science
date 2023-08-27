#codename = Baba Susukanlebak

#diharapkan dalam satuan SI
#input data
nilai_g = 9.81 #m/s**2
nilai_t = float(input("tentunkan nilai waktu : " ))

#rumus umum gerak jatuh bebas
nilai_h = 1/2*(nilai_g*(nilai_t**2))

#menampilkan output
print("nilai ketinggian ialah ", nilai_h, "m")