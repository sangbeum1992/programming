def hellobot():
    
    while True: # 계속해서 반복실행
        
        a = input() # 입력칸 생성
        
        if a != "Bye": # Bye가 아닌 경우엔 항상 Hi라고 대답하고
            print("Hi!")
            
            continue # 다시 입력칸 생성하는 단계로 돌아감
        
        else:    
            print("Ok bye...") # Bye라고 입력하는 경우에만 Ok bye...라는 답을 남기고
            break # 반복문 탈출

hellobot()