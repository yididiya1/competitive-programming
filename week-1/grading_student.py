def gradingStudents(grades):
    list = [];
    for i in grades:
        qoutient = int(i/5) + 1
        print(qoutient)
        number = 5 * qoutient
        if(number < 40):
            list.append(i)
        elif(number-i < 3):
            list.append(number)
        else:
            list.append(i)
    return list
