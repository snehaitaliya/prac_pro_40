#A Student Management System is a software application used to maintain student information such as roll number, name, course, marks, attendance, and other academic records. It allows users to perform operations like adding, updating,searching, displaying, and deleting student records. This practical demonstrates the use of Object-Oriented Programming (OOP), file handling, and data management in Python.'

def add_student():
    f=open("student.txt","a")

    roll=int(input("Enter Roll No. : "))
    name=input("Enter Name : ")
    s1=int(input("Enter Marks Of S1 : "))
    s2=int(input("Enter Marks Of S2 : "))
    s3=int(input("Enter Marks Of S3 : "))
    s4=int(input("Enter Marks Of S4 : "))
    s5=int(input("Enter Marks Of S5 : "))

    total=s1+s2+s3+s4+s5
    avg=total/5
    print("Total : ",total)
    print("Average : ",avg)

    m=max(s1,s2,s3,s4,s5)
    mi=min(s1,s2,s3,s4,s5)

    if avg>90:
        Grade="A"
    elif avg>80:
        Grade="B"
    elif avg>60:
        Grade="C"
    elif avg>=33:
        Grade="D"
    else:
        Grade="Fail"

    cnt=0
    if s1<35:
        cnt+=1
    if s2<35:
        cnt+=1
    if s3<35:
        cnt+=1
    if s4<35:
        cnt+=1
    if s5<35:
        cnt+=1

    if cnt==0:
        result="Pass"
    elif cnt<=2:
        result="ATKT"
    else:
        result="Fail"

    if f.tell()==0:
        f.write(f"Roll\tName\tS1\tS2\tS3\tS4\tS5\tMin\tMax\tTotal\tPer\t  Grade\tResult\n")    
    f.write(f"{roll}\t\t{name}\t{s1}\t{s2}\t{s3}\t{s4}\t{s5}\t{mi}\t{m}\t{total}\t\t{avg:.2f}\t{Grade}\t{result}\n")
    f.close()

def update_student():
    f=open("student.txt","r")
    data=f.readlines()
    f.close()

    roll=int(input("Enter Roll No. to Update : "))
    found=False

    for i in range(len(data)):
        if data[i].split("\t")[0]==str(roll):
            found=True
            print("Student Record Found.")
            roll=int(input("Enter Roll No. : "))
            name=input("Enter New Name : ")
            s1=int(input("Enter New Marks Of S1 : "))
            s2=int(input("Enter New Marks Of S2 : "))
            s3=int(input("Enter New Marks Of S3 : "))
            s4=int(input("Enter New Marks Of S4 : "))
            s5=int(input("Enter New Marks Of S5 : "))

            total=s1+s2+s3+s4+s5
            avg=total/5
            print("Total : ",total)
            print("Average : ",avg)

            m=max(s1,s2,s3,s4,s5)
            mi=min(s1,s2,s3,s4,s5)

            if avg>90:
                Grade="A"
            elif avg>80:
                Grade="B"
            elif avg>60:
                Grade="C"
            elif avg>=33:
                Grade="D"
            else:
                Grade="Fail"

            cnt=0
            if s1<35:
                cnt+=1
            if s2<35:
                cnt+=1
            if s3<35:
                cnt+=1
            if s4<35:
                cnt+=1
            if s5<35:
                cnt+=1

            if cnt==0:
                result="Pass"
            elif cnt<=2:
                result="ATKT"
            else:
                result="Fail"

            data[i]=f"{roll}\t\t{name}\t{s1}\t{s2}\t{s3}\t{s4}\t{s5}\t{mi}\t{m}\t{total}\t\t{avg:.2f}\t{Grade}\t{result}\n"
            break

    if not found:
        print("Student Record Not Found.")

    f=open("student.txt","w")
    f.writelines(data)
    f.close()

def search_student():
    f=open("student.txt","r")
    data=f.readlines()
    f.close()

    roll=int(input("Enter Roll No. to Search : "))
    found=False

    for i in range(len(data)):
        if data[i].split("\t")[0]==str(roll):
            found=True
            print("Student Record Found.")
            print(data[i])
            break

    if not found:
        print("Student Record Not Found.")

def delete_student():
    f=open("student.txt","r")
    data=f.readlines()
    f.close()

    roll=int(input("Enter Roll No. to Delete : "))
    found=False

    for i in range(len(data)):
        if data[i].split("\t")[0]==str(roll):
            found=True
            print("Student Record Found.")
            del data[i]
            break

    if not found:
        print("Student Record Not Found.")

    f=open("student.txt","w")
    f.writelines(data)
    f.close()

def display_students():
    f=open("student.txt","r")
    data=f.readlines()
    f.close()

    print("Student Records : ")
    for i in range(len(data)):
        print(data[i])

def main():
    while True:
        print("1. Add Student Record")
        print("2. Update Student Record")
        print("3. Search Student Record")
        print("4. Delete Student Record")
        print("5. Display All Student Records")
        print("6. Exit")

        choice=int(input("Enter Your Choice : "))

        if choice==1:
            add_student()
        elif choice==2:
            update_student()
        elif choice==3:
            search_student()
        elif choice==4:
            delete_student()
        elif choice==5:
            display_students()
        elif choice==6:
            break
        else:
            print("Invalid Choice.")

if __name__=="__main__":
    main()
