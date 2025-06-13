# json.dump() = json 데이터 파일로 저장
#json.dumps() = json 데이터 문자열로 저장
#json.load() = 파일에서 json 읽기
#json.loads() = 문자열에서 json 읽기
from pathlib import Path
import json


#내보내기
numbers = [1, 2, 3, 4]
json_file = Path('numbers.json')
contents = json.dumps(numbers)
json_file.write_text(contents) #dumps + write
#각각 아래 두줄은 same
with json_file.open('w+t') as fp:
    json.dump(numbers, fp) #dump + open



#읽기
json_file1= Path('numbers.json')
contents1 = json_file1.read_text()
numbers = json.loads(contents1)
#각각 아래 두줄은 same
with json_file1.open('rt') as fp:
    numbers = json.dump(fp)