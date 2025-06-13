#1) 0으로 나누는 예외
#2)try-except 블록
#3)예외를 처리해야하는 이유
#4)try-except-else
#5)try-except-finally
#6)FileNotFoundError 예외처리
#7)조용히 실패하기

#1,2)
try:
    print(5/0)
except ZeroDivisionError:
    print("You can\'t divide by zero.")

#=============================================================#

#3,4)
print("A simple divider")
while True:
    first = input("First number: ")
    second = input("Second number: ")
    try:
        answer = int(first) / int(second)
    except ZeroDivisionError:
        print("You can\'t divide by zero.")
        break
    else:
        print(answer)
        break
#아래위 SAME!!
print("A simple divider")
while True:
    first = input("First number: ")
    second = input("Second number: ")
    try:
        answer = int(first) / int(second)
        print(answer)
        break
    except ZeroDivisionError:
        print("You can\'t divide by zero.")
        break

#5)
print("A simple divider")
while True:
    first = input("First number: ")
    second = input("Second number: ")
    try:
        answer = int(first) / int(second)
        print(answer)
        break
    except ZeroDivisionError:
        print("You can\'t divide by zero.")
        break
    finally:
        print('Next?')
        break

#=============================================================#

#6)
from pathlib import Path
try:
    text_file = Path('file.txt')
    contents = text_file.read_text()
    print(contents)
except FileNotFoundError:
    print('No such file!')

#7)
try:
    text_file = Path('file.txt')
    contents = text_file.read_text()
    print(contents)
except FileNotFoundError:
    pass


