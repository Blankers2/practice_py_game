'''
오류 식별 로그
- is_dev_mode 설정한 스탭이 실행이 안됨
	- is_dev_mode를 False로 둬서 굳이 아래 변경하지않고 바로 진행
- try count가 매게임 새로 들어가는게 아니라 게임마다 설정됨
	-- 이부분은 try_count를 첫 while 구문에 넣어서 해결
	-- 점수가 첫번째 시도에도 카운팅이되어서 90점부터 시작이됨 
		--- print 구문의 숫자를 11로 변경

- restart 와 endding 리스트에 없는 글자를 넣어도 다시 시작하는 오류발생
	- 어떻게 해결해야하나 막막했지만 의외로 간단했다 
	- 둘다 리스트 형태기 때문에 그냥 + 하면 합쳐졌기 때문!

- 정수가 아닌걸 거르고 들어간 while 문에서 다시 오류를 범하면 에러가뜸
	- 값비교 구문을 넣으면 되지만 코드가 너무 복잡해짐

- 치명적인 오류 : 마지막 다시하기에서 아무거나 두번입력하면 다시돌아가짐
	- continue와 break가 어떻게 작동하는지 다시 생각해서 코드를 수정
# 여기까지 오류의 경우의 수를 모두 시도해보고 코드를 보완함.
'''

# TODO STEP 0
# is_dev_mode를 False로 둬서 굳이 아래 변경하지않고 바로 진행
is_dev_mode = False # 플래그변수? , 값의 변화에 따라 흐름제어가 변화됨
game_title = 'Number Matching Game' if is_dev_mode else None
player_game = 'guest' if is_dev_mode else None

'''
절차적 프로그래밍 시작
'''

# TODO STEP 1-1 리소스정리
Game_Title_Max_Length = 28
msg = f'[게임 제목을 입력해 주세요. 최대{Game_Title_Max_Length}자이내(<=28),\
	\n영문/숫자 조합으로 입력하세요.]\n'
Err_Mes = "# 에러! 정확하게 입력하세요!"

# STEP 1-2 기능 구현
# input을 변수안에 넣는다
# while - if등 조건문으로 이어지는 구조
# else에서 break를 걸어서 무한반복을 탈출시킨다
while not is_dev_mode:
	game_title = input(msg).strip() # 입력받을때 무조건 공백제거(strip()) 수행

	if not game_title: # 빈칸만 입력했을때
		print(Err_Mes)
		pass
	elif len(game_title)>Game_Title_Max_Length: # 글자수 초과했을때(28자)
		print(f'게임 제목을 정확하게 입력하세요. \
		\n최대{Game_Title_Max_Length}로 입력하시고, \
		\n방금 입력한 길이는 {len(game_title)}\
		이고, \n{len(game_title) - Game_Title_Max_Length}\
		초과 되었습니다')
		pass
	else: # 정확하게 입력
		break
# 게임제목 출력
print(f'~{game_title}의 전설!~')

# 값 검사
	
# TODO STEP 2 
'''
플레이어 이름도 STEP1과 동일한 절차로 입력받는다
변수명은 : player_game
제약조건 : continue를 반드시 사용
'''
Player_Max_Length = 10
msg_player = f'[플레이어 이름을 입력해 주세요. \
	\n최대 {Player_Max_Length}글자 까지 지원됩니다.\
	\n영문 및 숫자 조합으로 입력하세요]\n'
while not is_dev_mode:
	player_game = input(msg_player).strip()
	if not player_game:
		print(Err_Mes)
		continue
	elif len(player_game)>Player_Max_Length:
		print(f'플레이어 이름을 정확하게 입력하세요\
		최대{Player_Max_Length}로 입력하세요')
		pass
	# while 안에서 플레이어 이름 설정
	print(f"~일어나세요 {player_game} 용사님!~")
	break

# TODO STEP 3 게임타이틀 프럼프트 출력
# 글자만 중앙정렬
under = '-'
ver = "ver 1.0.0"
# '-'32개를 f스트링으로 변수에 직접 넣어서 만들기
# print(f'{under.center(32,'-')}')
# 그냥 * 를 써보자
'''
print(under*32)
print(f'-{game_title.center(30-len(game_title),' ')}-')
print(f'-{player_game.center(30-len(player_game),' ')}-')
print(f'-{ver.center(30,' ')}-')
print(under*32)
'''

# 강의 듣고 수정
# 글자수 리소스를 지정하지 않았음 다시해보기
Intro_Space_Size = 2
Intro_Icon_Size = 2
Intro_Title_Max_Len = Game_Title_Max_Length + Intro_Icon_Size + Intro_Space_Size

# f 스트링 일부수정
# center 대신 f스트링 정렬 문법 쓰기
print(under*Intro_Title_Max_Len)
print(f'{under}{game_title:^30}{under}')
print(f'{under}{player_game:^30}{under}')
print(f'{under}{ver:^30}{under}')
print(under*Intro_Title_Max_Len)


# TODO STEP 4 
'''
게임이 본격적으로 시작할때 random을 import로 
넣어서 난수 발생시키기
'''
# STEP 4-1 난수 발생
# random.randint(a,b) : a <= x <= b 난수를 만들어줌
import random
#ai_number = random.randint(Ai_Min, Ai_Max)

Ai_Min = 1
Ai_Max = 255



# TODO STEP 5
'''
플레이어가 값을 하나 입력
- A. 최초 프롬프트 제시
- B. 사용자 입력(문자열) -> 엔터
- C. 검사
	- 빈값 -> 정확히 입력하세요 -> 다시 A. 부터
		- 체크, 변수.isXXX()) 체크
		- 1보다 작거나(<), 100보다 크면(>) -> 다시 A부터
            - 적당한 메시지 필요(생략)
        - 정상
'''
# 리소스
player_input = f'[{Ai_Min} ~ {Ai_Max}] 사이의 원하는 정수를 입력하세요! \
	 \n* 주의 : 정수를 입력하지 않으면 게임이 초기화 됩니다!! \n'
Err_Mes2 = "# 에러! 정수만 입력하세요!"

# while True:
# 	player_select = input(player_input).strip()
# 	if not player_select:
# 		print(Err_Mes)
# 		continue
# 	# 정수크기를 비교하기전에 소수점이있는걸 방지하기위해서 int() 넣기전에 
# 	# isnumeric() 으로 정수인지 확인했어야함
# 	if not player_select.isnumeric():
# 		print(Err_Mes2)
# 		continue
# 	player_select = int(player_select)
# 	if player_select<Ai_Min or player_select>Ai_Max:
# 		print(f'1부터 255까지 숫자만 입력해주세요')
# 		continue
# 	# 정상입력하고 빠져나오기
# 	break


# isXXX 함수로 정답값 판단하기
'''
words = ['1', '1.1', 'a', '가', '!']
for word in words:
	print(word, word.isnumeric(), word.isdecimal(), \
	   word.isascii(), word.isalpha())
'''

# TODO STEP 6
'''
- 판단 (정답)
    - ai값과 플레이어의값 비교
        - 크다
            - 힌트(자율적) 제공-> 다시 A
        - 작다
            - 힌트(자율적) 제공-> 다시 A
        - 같다
            - 게임 클리어 -> 점수 계산
                - (10-시도회수)*10
                - 점수 출력(형식을 자율적)
'''
# 리소스
want_more = "[너무 작아요!]"
want_little = "[너무 크네요!]"
complete = "[어떻게 알았죠?]"
player_input_next = '[다른 정수를 입력하세요!]\n'

# 플레이어가 입력한 값 = player_select / 랜덤값 = ai_number
try_count = 0
# while True:
# 	player_select = input(player_input).strip()
# 	if not player_select:
# 		print(Err_Mes)
# 		continue
# 	# 정수크기를 비교하기전에 소수점이있는걸 방지하기위해서 int() 넣기전에 
# 	# isnumeric() 으로 정수인지 확인했어야함
# 	if not player_select.isnumeric():
# 		print(Err_Mes2)
# 		continue
# 	player_select = int(player_select)
# 	if player_select < Ai_Min or player_select > Ai_Max:
# 		print(f'1부터 255까지 숫자만 입력해주세요')
# 		continue
# 	# 정상입력하고 빠져나오기
# 	while True:
# 		# input을 여기에 넣으니 숫자를 두번입력 해야하는 오류가 발생하기 때문에
# 		# 두번쨰 while 구문의 if안에 새로운 출력값을 설정해 input을 배치함!
# 		player_select = int(player_select)
# 		ai_number = int(ai_number)
# 		# 둘다 int()를 먹여줘야 if에서 연산자로 비교가능
# 		try_count += 1
# 		if player_select < ai_number:
# 			print(want_more)
# 			player_select = input(player_input_next).strip()
# 			continue
# 		if player_select > ai_number:
# 			print(want_little)
# 			player_select = input(player_input_next).strip()
# 			continue
# 		if player_select==ai_number:
# 			print(complete)
# 			break
# 	break
# print('step 5,6 완료', f'{(10-try_count)*10}점 이에요!')



# TODO STEP 7
'''
- 프럼프트 출력
    - 다시 게임을 하시겠습니까?
        - yes, y, Y, YES, Yes, yEs, yeS,.. => 동의로 해석
            - 다시 게임으로 진행 -> STEP 4
        - n, N, NO, No, no, No,..
            - 게임 종료
            - "Bye Bye ~!"
'''

# 리소스 준비
# 다양한 값을 리스트형태로 준비 
# 대문자를 다적으면 너무 길어지고 더러우니 소문자로만 준비
# 이후 lower()로 유저가 입력한값을 모두 소문자로 변경해 문제해결
restart = ['yes','y','o','ok','go']
endding = ['no','n','x']
select_tx = "[한번 더 하시겠습니까?]\n"
Err_Mes3 = "# 에러! 제대로 입력하세요!"
endding_tx = "(((Bye Bye~! 또 오세요!)))"
# 매게임 다른 랜덤값을 얻기 위해 STEP4 에서 지정한것을 들고와서 while안에 넣기
# input 미리 설정
# user_select = input(select_tx).strip().lower()
# 이전에 썼던 코드를 들고와서 while문에 가두기
while True:
	while True:
		try_count = 0
		ai_number = random.randint(Ai_Min, Ai_Max)
		print(f'~ [재시작] AI의 생성값 = {ai_number} ~')
		player_select = input(player_input).strip()
		if not player_select:
			print(Err_Mes)
			continue
		if not player_select.isnumeric():
			print(Err_Mes2)
			continue
		player_select = int(player_select)
		if player_select < Ai_Min or player_select > Ai_Max:
			print(f'# 에러! [1부터 255까지 숫자만 입력해주세요!]')
			continue
		while True:
			player_select = int(player_select)
			ai_number = int(ai_number)
			try_count += 1
			if player_select < ai_number:
				print(want_more)
				player_select = input(player_input_next).strip()
				continue
			if player_select > ai_number:
				print(want_little)
				player_select = input(player_input_next).strip()
				continue
			if player_select == ai_number:
				print(complete)
				break
		break
	print('step 5,6 완료', f'{(11-try_count)*10}점 이에요!')
	# 여기까진 똑같고 STEP 7을 해결하기 위해 아래 코드를 짜봄
	user_select = input(select_tx).strip().lower()
	while True:
		if not user_select in restart+endding:
			print(Err_Mes3)
			user_select = input(select_tx).strip().lower()
			continue
		else:
			break
	if user_select in restart:
			continue
	if user_select in endding:
			break
	break
print(endding_tx)

