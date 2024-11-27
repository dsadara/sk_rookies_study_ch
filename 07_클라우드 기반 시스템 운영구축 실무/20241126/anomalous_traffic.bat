@echo off
chcp 65001

:: 배치 파일 제목 출력
echo ===================================
echo    시스템 점검 도구 v1.0
echo ===================================
echo.

:: 결과 저장할 폴더 생성
set "resultFolder=%~dp0results"
if not exist "%resultFolder%" mkdir "%resultFolder%"

:: 현재 날짜와 시간으로 파일명 생성
set "datetime=%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%"
set "logFile=%resultFolder%\system_check_%datetime%.txt"

:: 시스템 정보 수집
echo [시스템 정보 수집 시작] >> "%logFile%"
echo 실행 시간: %date% %time% >> "%logFile%"
echo. >> "%logFile%"

:: 1. 시스템 기본 정보
echo [1. 시스템 기본 정보] >> "%logFile%"
systeminfo | findstr /C:"OS" /C:"시스템 제조업체" /C:"시스템 모델" >> "%logFile%"
echo. >> "%logFile%"

:: 2. 네트워크 연결 상태
echo [2. 네트워크 연결 상태] >> "%logFile%"
ipconfig /all >> "%logFile%"
echo. >> "%logFile%"

:: 3. 실행 중인 프로세스
echo [3. 실행 중인 프로세스] >> "%logFile%"
tasklist >> "%logFile%"
echo. >> "%logFile%"

:: 4. 네트워크 연결
echo [4. 네트워크 연결] >> "%logFile%"
netstat -ano >> "%logFile%"
echo. >> "%logFile%"

:: 5. 이벤트 로그 확인
echo [5. 최근 시스템 이벤트] >> "%logFile%"
wevtutil qe System /c:10 /f:text >> "%logFile%"
echo. >> "%logFile%"

:: 결과 파일 생성 완료 메시지
echo 점검이 완료되었습니다.
echo 결과 파일 위치: %logFile%
echo.
pause