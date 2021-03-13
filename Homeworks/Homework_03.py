import pandas as pd

student_01 = []
student_02 = []
student_03 = []
student_04 = []
student_05 = []

for i in range(1):
    ders_data_01 = float(input("1.Öğrencinin Ders Notu: "))
    ders_data_02 = float(input("1.Öğrencinin Proje Notu: "))
    ders_data_03 = float(input("1.Öğrencinin Final Notu: "))
    print("-"*30)
    ders_data_04 = float(input("2.Öğrencinin Ders Notu: "))
    ders_data_05 = float(input("2.Öğrencinin Proje Notu: "))
    ders_data_06 = float(input("2.Öğrencinin Final Notu: "))
    print("-"*30)
    ders_data_07 = float(input("3.Öğrencinin Ders Notu: "))
    ders_data_08 = float(input("3.Öğrencinin Proje Notu: "))
    ders_data_09 = float(input("3.Öğrencinin Fİnal Notu: "))
    print("-"*30)
    ders_data_10 = float(input("4.Öğrencinin Ders Notu: "))
    ders_data_11 = float(input("4.Öğrencinin Proje Notu: "))
    ders_data_12 = float(input("4.Öğrencinin Final Notu: "))
    print("-"*30)
    ders_data_13 = float(input("5.Öğrencinin Ders Notu: "))
    ders_data_14 = float(input("5.Öğrencinin Proje Notu: "))
    ders_data_15 = float(input("5.Öğrencinin Final Notu: "))
    
    student_01.append(ders_data_01)
    student_01.append(ders_data_02)
    student_01.append(ders_data_03)
    student_02.append(ders_data_04)
    student_02.append(ders_data_05)
    student_02.append(ders_data_06)
    student_03.append(ders_data_07)
    student_03.append(ders_data_08)
    student_03.append(ders_data_09)
    student_04.append(ders_data_10)
    student_04.append(ders_data_11)
    student_04.append(ders_data_12)
    student_05.append(ders_data_13)
    student_05.append(ders_data_14)
    student_05.append(ders_data_15)

#passingGrade =(dersnot*0.3)+(projenot*0.3)+(final*0.4)

student_01_Grade = int((student_01[0]*0.3)+(student_01[1]*0.3)+(student_01[2]*0.4))
student_02_Grade = int((student_02[0]*0.3)+(student_02[1]*0.3)+(student_02[2]*0.4))
student_03_Grade = int((student_03[0]*0.3)+(student_03[1]*0.3)+(student_03[2]*0.4))
student_04_Grade = int((student_04[0]*0.3)+(student_04[1]*0.3)+(student_04[2]*0.4))
student_05_Grade = int((student_05[0]*0.3)+(student_05[1]*0.3)+(student_05[2]*0.4))
print("-"*64)

student_01_durum = "Kaldı" if student_01_Grade<45 else "Geçti"
student_02_durum = "Kaldı" if student_02_Grade<45 else "Geçti"
student_03_durum = "Kaldı" if student_03_Grade<45 else "Geçti"
student_04_durum = "Kaldı" if student_04_Grade<45 else "Geçti"
student_05_durum = "Kaldı" if student_05_Grade<45 else "Geçti"

students = {"Students":["1. Öğrenci","2. Öğrenci","3. Öğrenci","4. Öğrenci","5. Öğrenci"],
            "Midtern":[student_01[0],student_02[0],student_03[0],student_04[0],student_05[0]],
            "Project":[student_01[1],student_02[1],student_03[1],student_04[1],student_05[1]],
            "Final":[student_01[2],student_02[2],student_03[2],student_04[2],student_05[2]],
            "PassGrade":[student_01_Grade,student_02_Grade,student_03_Grade,student_04_Grade,student_05_Grade],
            "PassingStatus":[student_01_durum,student_02_durum,student_03_durum,student_04_durum,student_05_durum]}

df1 = pd.DataFrame(students)
df = df1.sort_values("PassGrade",ascending=False)
print(df)
