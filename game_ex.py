# TODO STEP0 개발 동선을 줄이기 위해서 특별 설정
is_dev_mode = False#True
game_title  = 'Number Matching Game' if is_dev_mode else None
player_name = 'guest' if is_dev_mode else None

# TODO STEP1 진행 , 11시 10분까지 -> 구글드라이브 -> 폴더(이름으로)생성후 업로드
GAME_TITLE_MAX_LENGTH = 28
msg = f'게임 제목을 입력해 주세요. 최대 {GAME_TITLE_MAX_LENGTH}자이내(<=28), \
영문/숫자 조합으로 입력하세요\n\n >'
ERR_MSG = '정확하게 입력하세요'

while not is_dev_mode:
    game_title = input( msg ).strip() 
    if not game_title:  
        print( ERR_MSG )
    elif len(game_title) > GAME_TITLE_MAX_LENGTH:
        print( f''' 
            게임 제목을 정확하게 입력하세요.
            최대 {GAME_TITLE_MAX_LENGTH}이내로 입력하시고,
            방급 입력하신 내용은 {game_title} 이고, 
            최대길이 대비 { len(game_title) - GAME_TITLE_MAX_LENGTH }자가 초과되었습니다.
        ''' )
    else:
        break
print(f'step 1 완료, 게임 제목은 = {game_title}')

# TODO STEP2 진행, 실습:13시 11분까지 작업(10분)
GAME_PLAYER_NAME_MAX_LENGTH = GAME_TITLE_MAX_LENGTH
player_name_input_prompt = f'플레이어 이름을 입력해 주세요. 최대 {GAME_TITLE_MAX_LENGTH}자이내(<=28), \
영문/숫자 조합으로 입력하세요\n\n >'
ERR_MSG_2 = '정확하게 입력하세요' # 선택사항
while not is_dev_mode:
    player_name = input( player_name_input_prompt ).strip()
    if not player_name:
        print( ERR_MSG_2 )
        continue
    if len(player_name) > GAME_PLAYER_NAME_MAX_LENGTH:
        print( f''' 
            플레이어 이름을 정확하게 입력하세요.
            최대 {GAME_PLAYER_NAME_MAX_LENGTH}이내로 입력하시고,
            방급 입력하신 내용은 {player_name} 이고, 
            최대길이 대비 { len(player_name) - GAME_PLAYER_NAME_MAX_LENGTH }자가 초과되었습니다.
        ''' )
        continue
    break
print(f'step 2 완료, 플레이어 이름은 = {player_name}')

# TODO STEP3 진행 : 36분까지(6분) 진행
GAME_INTRO_ICON     = '-'
GAME_SPACE_SIZE     = 2
GAME_ICON_SIZE      = 2
GAME_INTRO_MAX_LINE = GAME_PLAYER_NAME_MAX_LENGTH + GAME_SPACE_SIZE + GAME_ICON_SIZE
GAME_VERSION        = 'ver 1.0.0'
print( GAME_INTRO_ICON * GAME_INTRO_MAX_LINE )
print( f'{GAME_INTRO_ICON} {game_title:^28} {GAME_INTRO_ICON}' ) 
print( f'{GAME_INTRO_ICON} {player_name:^28} {GAME_INTRO_ICON}' ) 
print( f'{GAME_INTRO_ICON} {GAME_VERSION:^28} {GAME_INTRO_ICON}' ) 
print( GAME_INTRO_ICON * GAME_INTRO_MAX_LINE )

is_game_playing = True # 게임 진행 플래그 (False:  게임 종료)
while is_game_playing:
    # TODO STEP4
    AI_CREATE_NUM_MIN = 1
    AI_CREATE_NUM_MAX = 100
    import random
    ai_number = random.randint(AI_CREATE_NUM_MIN, AI_CREATE_NUM_MAX)
    # is_dev_mode를 이용하여 처리 가능
    #print(f'step 4 완료, AI의 생성값 = {ai_number}')

    # TODO STEP 5, 15시 15분까지 진행
    PLAYER_INPUT_PROMPT = f"AI가 생성한 값 {AI_CREATE_NUM_MIN} ~ {AI_CREATE_NUM_MAX} \
        사이 중 정수값 하나를 넣어서 맞추시오\n\n >"
    try_count = 0 # 1회 게임시 몇번 시도만에 정답을 맞췄는가?
    while True:
        while True:
            player_number = input( PLAYER_INPUT_PROMPT ).strip()
            if not player_number:
                print( ERR_MSG_2 )
                continue
            if not player_number.isnumeric():
                print( ERR_MSG_2 )
                continue 
            player_number = int( player_number )
            if (player_number<1) or (100<player_number):
                print( ERR_MSG_2 )
                continue
            break
        # TODO STEP 6 5분 부여
        ERR_MSG3 = '입력값이 AI값보다 크다'
        ERR_MSG4 = '입력값이 AI값보다 작다'
        MSG_SUCCESS = '정답입니다.'
        try_count += 1
        if player_number > ai_number:
            print( ERR_MSG3 )
            pass
        elif player_number < ai_number:
            print( ERR_MSG4 )
            pass
        else:
            print( MSG_SUCCESS )
            break
    print('step 5,6 완료', f'총 획득 점수는 { (10-try_count)*10 }점 입니다.')

    # TODO STEP 7 => 작성후 game_최종.py 제출 (자율)
    '''
        - 프럼프트 출력
        - 다시 게임을 하시겠습니까?
            - 사용자가 정확하게 입력하지 않는다면?
                - 정확하게 입력하세요 -> 다시 입력
            - yes, y, Y, YES, Yes, yEs, yeS,.. => 동의로 해석
                - y or yes => 대소문자 구분없이 전부 인정 => 입력값을 특정 형식(대문자 혹은 소문자)
                    - ''.upper() : 대문자 or ''.lower() : 소문자
                - 다시 게임으로 진행 -> STEP 4
            - n, N, NO, No, no, No,..
                - 게임 종료
                - "Bye Bye ~!" 
    '''
    # STEP 7-1 리소스 정리
    GAME_RETRY_PROMPT = '다시 게임을 하시겠습니까?'
    GAME_OVER_MSG = 'Bye Bye ~!'
    # STEP 7-2 사용자 입력에 맞춘 처리
    while True: # 좋은 표현은 아니지만 여기서는 연습을 위해서 주로 사용
        # 사용자 입력
        answer = input(GAME_RETRY_PROMPT).strip().lower() # 공백제거, 소문자처리
        # 체크 (3가지)
        if answer == 'yes' or answer == 'y':
            break
            pass
        elif answer == 'no' or answer == 'n':
            # 7-2-1 메시지 출력
            print( GAME_OVER_MSG )
            # 7-2-2 전체 게임을 탈출할려면 -> stpe7 종료후 
            is_game_playing = False
            # 7-2-3 현재 반복문 탈출
            break # 바로 반복문 탈출 -> 이하 코드 수행 X
            pass
        else:
            print( ERR_MSG )
            pass
        

# 반복문안에서 동일한 내용이 계속해서 발생된다면
# 상수 생성(값을 초기화는 관계 없다), 객체 생성(나중에 체크),.. 반복문 위로 위치 조정
# 속도저하가 올만한 반복적인 작업들은 위치 조정,..

# 코드 정렬 : 
'''
    익스텐션 메뉴 => autopep8 포멧터 설치
    적용
        - *.py 저장시 자동적용
        - 수동적용 코드에서 우클릭 > Format Document 
    
'''