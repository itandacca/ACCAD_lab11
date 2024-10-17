student_name =input("Enter your name: ")
section = input("Enter your section: ")

prelim =  float(input("Enter prelim grade: "))
if prelim < 40 or prelim > 100: 
    print("Invalid input. Must be between 40 and 100")
    
else:
    midterm = float(input("Enter midterm grade:"))
    if midterm < 40 or midterm > 100:
        print("Invalid input. Must be between 40 and 100")
        
    else:
        finals = float(input("Enter finals grade:"))
        if finals <40 or finals > 100:
            print("Invalid input. Must be between 40 and 100")
            
        else:
            finalGrade = (prelim * 0.3333) + (midterm * 0.3333) + (finals * 0.3333)
            finalGrade = round(finalGrade)
            print("Hello your final grade is:" , finalGrade)


        if 99 <= finalGrade <= 100: 
            print("Your GPA is 1.0")
            
        elif 96 <= finalGrade <= 98:
            print("Your GPA is 1.25")
        
        elif 93 <= finalGrade <= 95:
            print("Your GPA is 1.5")
            
        elif 90 <= finalGrade <= 92:
            print("Your GPA is 1.75")
            
        elif 87<= finalGrade <= 89:
            print("Your GPA is 2.0")
            
        elif 84 <= finalGrade <= 86:
            print("Your GPA is 2.25")
            
        elif 81 <= finalGrade <= 83:
            print("Your GPA is 2.5")
        
        elif 78 <= finalGrade <= 80:
            print("Your GPA is 2.75")
            
        elif 75 <= finalGrade <= 77:
            print("Your GPA is 3.0")
            
        elif finalGrade <= 74: 
            print("Your GPA is 5.0") 
            
        else:
            print("Invalid input. Must be between 40 and 100")