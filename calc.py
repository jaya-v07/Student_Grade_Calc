num = []
print("Enter the marks of 5 subjects : ")
for i in range(5):
    value = int(input())
    num.append(value)
print("________________________________\n")
print(" The total marks of 5 subjects is : ", sum(num))
avg = 0;
for i in range(5):
    avg = avg + num[i];
avg = avg / 5;
print("the average marks: ", avg);
print("The Student's Grade is : ")
if avg >= 90:
    print("Grade A")
elif avg >= 75:
    print("Grade B")
elif avg >= 50:
    print("Grade C")
elif avg <= 50:
    print("Grade F")

