#0516 실습
from pathlib import Path
import json

#Q1
players_file = Path('players.json') #파일을 Path로 불러오기
contents = players_file.read_text(encoding = 'UTF-8')  #텍스트 읽어오기 / UTF-8은 한글프린트 오류 방지
items = json.loads(contents) #내용 불러오기

winner_rankers = [ ]
for k, v in items.items(): #k,v는 players.json에 이름과, 퀘스트 점수를 각각 의미
    if v['quest_A'] >= 80 and v['quest_B'] >= 80: #조건으로 winner_rankers에 이름을 더함.
        winner_rankers.append(k)
print(f"우수 랭커: {winner_rankers}")

#Q2
birthday_find = Path('pi.txt')
contents1 = birthday_find.read_text(encoding = 'UTF-8') 


birth = input("당신의 생일을 yymmdd형식으로 입력해주세요!: ")
if birth in contents1:
    print("당신의 생일은 pi의 첫 백만자리 안에 포함됩니다.")
else:
    print("당신의 생일은 pi의 첫 백만자리 안에 포함되지 않습니다.")

#Q3
cats_file = Path("cats.txt")
dogs_file = Path("dogs.txt")

cats_file.write_text("냥이,생강이,포포", encoding='UTF-8')
dogs_file.write_text("감자,고구마,당근", encoding='UTF-8')
while True:
    file_name = input("파일이름: ")
    file_path = Path(file_name)
    
    try:
        contents2 = file_path.read_text(encoding='UTF-8')
    except FileNotFoundError:
        print(f"{file_name} 파일이 존재하지 않습니다.")
    else:
        cat_name = contents2.split(",")
        for n in cat_name:
           print(n)
        break

#Q4
#json.dump() = json 데이터 파일로 저장
#json.dumps() = json 데이터 문자열로 저장
#json.load() = 파일에서 json 읽기
#json.loads() = 문자열에서 json 읽기
movie_review = Path("reviews.json")
if movie_review.exists():
    with open(movie_review, encoding='UTF-8') as p:
        reveiws = json.load(p)
else:
    reveiws = []
user_info = input("사용자 이름(user): ")
movie_info = input("영화 제목(movie): ")
rate_info = input("평정(rating): ")

if not rate_info.isdigit():
    raise ValueError("평점은 정수여야 합니다.")
if int(rate_info) < 1 or int(rate_info) > 5:
    raise ValueError("평점은 1부터 5 사이의 값이어야 합니다.")

new_review_info = {
    "user":user_info,
    "movie":movie_info,
    "rate":rate_info
}
reveiws.append(new_review_info)

with open(file_path, "w", encoding="UTF-8") as f:
    json.dump(reveiws, f, ensure_ascii=False, indent=4 )

print("리뷰가 저장되었습니다.")

