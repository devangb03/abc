with open('names.txt','r') as file:
    with open('emails.txt','w') as file2:
        a = file.readlines()
        print(a)
        for i in range(0,99): 
            b = a[i]
            fullname=b.split()
            surname=fullname[0]
            middlename=fullname[2]
            firstname=fullname[1]
            email=""
            email += (surname+firstname[0]+middlename[0]+'@rknec.edu\n')
            file2.write(email)
            print(email)