##Question Three
physic=int(input("Enter Physics number:"))
chemistry=int(input("Enter Chemistry number"))
bio=int(input("Enter Bio number:"))
math=int(input("Enter Math number:"))
computer=int(input('Enter Computer number:'))

sum=physic+chemistry+bio+math+computer
percentage=(sum//500)*100
if percentage>=90 and percentage<=100:
    print("Grade A")
elif  percentage>=80 and percentage<90:
    print("Grade B")
elif percentage>=70 and percentage<80:
    print("Grade C")
elif percentage>=60 and percentage<70:
    print("Grade D")
elif percentage>=40 and percentage<60:
    print("Grade E")
else:
    print("Grade F")                     