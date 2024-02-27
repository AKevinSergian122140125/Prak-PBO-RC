num_students = int(input("Masukkan Nomor Siswa   :  "))

student_data ={}

for students in range(num_students) :
   name = input("Masukan Nama    : ")
   grade = int(input("Maukan Nilai    : "))
   student_data[name] = grade
   print("Data Berhasil Ditambahkan!\n")

   print("Data Pelajar :\n")

   for name, grade in student_data.items():
        print(f"{name} : {grade}")
