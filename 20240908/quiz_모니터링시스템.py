'''
### **2) 디렉토리 파일 모니터링 시스템 구현 - 단계 1**

---

**문제 설명**

- Python을 사용하여 `'static'` 디렉토리를 모니터링하고, 새로 생성되는 파일을 감지한 후, 해당 파일의 이름을 출력하는 프로그램을 작성합니다. 이 문제의 목적은 디렉토리 내에서 새로운 파일이 생성될 때 이를 감지하여 사용자에게 알리는 것입니다.

**요구 사항**

1. **디렉토리 설정**:
    - 프로그램은 `'static'` 디렉토리를 모니터링해야 합니다. 이 디렉토리의 초기 파일 목록을 먼저 저장하고, 이후 새로 추가되는 파일을 감지합니다.
2. **파일 감지**:
    - 프로그램은 무한 반복(`while`)을 통해 디렉토리의 변경을 지속적으로 모니터링해야 합니다. 새로운 파일이 생성되면 그 파일의 이름을 출력해야 합니다.
3. **파일 목록 업데이트**:
    - 새로운 파일이 감지된 후, 프로그램은 이전 파일 목록을 현재 파일 목록으로 갱신해야 합니다.
4. **성능 고려**:
    - 프로그램은 매 1초마다 디렉토리의 상태를 체크하여 CPU 사용률을 낮게 유지합니다.
    
    ```python
    python코드 복사
    import time
    
    time.sleep(1)
    ```
    
    - 1초마다 1씩 증가한 값을 출력하는 코드
    
    ```python
    import time
    
    num = 0
    
    while True:
        time.sleep(1)
        print(num)
        num += 1
    ```
    
5. **코드 구조**:
    - 프로그램은 `import` 문을 통해 필요한 모듈(`os`, `time`)을 포함해야 합니다. 또한, 코드가 명확하고 유지보수가 용이하도록 작성해야 합니다.

**힌트**

- **집합 연산 사용**:
    - 집합(`set`) 연산을 사용하여 디렉토리 내 파일 목록의 차이점을 쉽게 계산할 수 있습니다. 새로운 파일이 추가되면, 이를 감지하여 처리할 수 있습니다.
- **`set()` 함수 사용**:
    - `set()` 함수는 리스트와 같은 반복 가능한 자료형을 집합으로 변환하여 중복된 항목을 제거하고 다양한 집합 연산을 지원합니다.

'''


import os, time

# def print_file_list(file_list):
#     print('현재 파일 목록: ')
#     for file in file_list:
#         print(file)

# 모니터링할 디렉토리 경로 설정
DIR_PATH = os.path.join('20240908', 'static')
file_set_before = set(os.listdir(DIR_PATH))

while True:
    file_set_new = set(os.listdir(DIR_PATH))
    update = set.difference(file_set_new, file_set_before)
    if len(update) != 0:
        print("새로 생성된 파일:")
        for file in update:
            print(file)
    file_set_before = file_set_new
    time.sleep(1)