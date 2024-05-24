test_grade = int(input())

if 90 <= test_grade <= 100:
    print('A')
elif 80 <= test_grade <= 89:
    print('B')
elif 70 <= test_grade <= 79:
    print('C')    
elif 60 <= test_grade <= 69:
    print('D')
else:
    print('F')