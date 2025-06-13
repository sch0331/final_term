# 파일에서 예외를 처리하는 방법, 파일에서 읽기/쓰기/예외/데이터 저장
#파일에서 읽기 : 파일 전체 읽기, 파일 경로, 한 행씩 읽기 - python 기본 라이브러리 제공 pathlib과 Path 객체 사용
from pathlib import Path


#===================#파일 읽기#====================#
#파일 전체 읽기
text_file = Path('file.txt')
contents = text_file.read_text()
print(contents)

#상대 경로 : text_file = Path('files/file.txt')
#절대 경로 : text_file = Path('C:/files/file.txt')

#파일 모두 읽고 행을 나누기
text_file1 = Path('file.txt')
contents1 = text_file1.read_text()
lines = contents1.splitlines() #splitlines로 행 나누기!
print(lines)

#파일을 읽고 한 행씩 읽기(한 줄씩 읽어들이기)
text_file2 = Path('file.txt')
with text_file2.open('rt') as fp:
    for line in fp.readlines():
        print("WTF!")

#================#파일에 쓰기#================#
#빈파일에 쓰기, 여러행 쓰기, 파일에 이어 붙이기

#읽는 것은 read, 쓰는 것은 write
out_file = Path('output.txt')
out_file.write_text('An output message')

#여러 줄은 항상 _lines
out_file1 = Path('output.txt')
lines = ["Line 4\n", "Line 5\n"]
with out_file.open('w+t') as wp:  #w+t write/text 모드로 읽기,쓰기 둘다 가능.
    wp.writelines(lines)

#아래위 same

#여러 줄 작성 + 반복해서 쓰기
out_file2 = Path('output.txt')
lines = ["Line 4\n", "Line 5\n"]
with out_file2.open('w+t') as wp:
    for line in lines:
        wp.write(line)


#파일에 이어붙이기 - a+t를 사용해야함.(a = append)
out_file3 = Path('output.txt')
lines = ["Line 4\n", "Line 5\n"]
with out_file.open('a+t') as wp:
    wp.writelines(lines)

#아래위 same

#파일에 이어붙이기 - a+t를 사용해야함.(a = append)-for문
out_file4 = Path('output.txt')
lines = ["Line 4\n", "Line 5\n"]
with out_file.open('a+t') as wp:
    for line in lines:
        wp.write(line)
