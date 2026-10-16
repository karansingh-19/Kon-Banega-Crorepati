#Assignment :- Kon Banega Crorepati
        
questions = [ 
    ["Which language was used to create fb?", "Python", "French", "Javascript", "Php", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript", "Php", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript", "Php", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript", "Php", "None", 4] 
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

money = 0  # Initialized the money variable

for i in range(0, len(questions)):
    question = questions[i]  # Fixed: changed 'question[i]' to 'questions[i]'
    print(f"Question for Rs. {levels[i]}")
    print(questions[i])
    print(f"a. {question[1]}      b. {question[2]}")
    print(f"c. {question[3]}      d. {question[4]}")
    
    reply = int(input("Enter your answer (1-4): "))
    
    # Fixed: Compare reply to the last item of the current question loop (question[-1])
    if reply == question[-1]:
        print(f"Correct answer and you have won {levels[i]}")  # Fixed: changed 'level[i]' to 'levels[i]'
        if i == 4:
            money = 10000
        elif i == 9:  # Fixed: changed 'else if' to Python's 'elif'
            money = 320000
    else:  # Fixed: Aligned 'else' properly with the correct indentation
        print("Wrong answer!")
        break  # Fixed: Removed the trailing period '.' from break