from pathlib import Path
import json

#Q5 원주율을 백만번째 자리까지 작성했을때, 특정 숫자가 몇 번 나오는지를 알고자 한다. 다음과 같이 동작하도록 하라.
pi_circle = Path('pi.txt')
contents = pi_circle.read_text(encoding='UTF-8')
while True:
    number = input("A number to search? ")
    if number == 'quit':
        print("Finished")
        break
    else:
        number_of_input = contents.count(number)
        print(number_of_input)

#Q6 특정한 파일을 입력받아서, 어떤 단어가 텍스트 속에 몇번 나오는지를 탐색하는 프로그램을 작성해라.(단어구분은 띄어스기로 한다.)
while True:
    input_file = input("File to read? ")
    specific_file = Path(input_file)
    contents1 = specific_file.read_text(encoding='UTF-8')
    words = contents1.split(" ")
    text1 = input("Word to search?  ")
    number_of_text1 = words.count(text1)
    print(f"Number: {number_of_text1}") 
    
