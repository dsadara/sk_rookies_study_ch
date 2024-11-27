@echo off
chcp 949
setlocal enabledelayedexpansion

:: 시작 시간 기록
set "startTime=%date% %time%"
set "resultFolder=%~dp0system_check_results"
set "datetime=%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%"
set "logFile=%resultFolder%\system_check_%datetime%.txt"

:: 결과 폴더 생성
if not exist "%resultFolder%" mkdir "%resultFolder%"

echo ================================================== > "%logFile%"
echo                시스템 정보 수집 보고서 >> "%logFile%"
echo ================================================== >> "%logFile%"
echo. >> "%logFile%"

:: 1. 시스템 정보 수집 시작/종료 시간
echo [1. 시스템 정보 수집 시작 시간] >> "%logFile%"
echo 시작 시간: %startTime% >> "%logFile%"
echo. >> "%logFile%"

:: 2. OS 및 네트워크, 윈도우 기본 정보
echo [2. OS 및 시스템 기본 정보] >> "%logFile%"
systeminfo >> "%logFile%"
echo. >> "%logFile%"

:: 3. 사용자 정보
echo [3. 사용자 정보] >> "%logFile%"
echo 현재 로그인 사용자: >> "%logFile%"
whoami >> "%logFile%"
echo. >> "%logFile%"
echo 전체 사용자 목록: >> "%logFile%"
net user >> "%logFile%"
echo. >> "%logFile%"

:: 4. 공유 정보
echo [4. 공유 정보] >> "%logFile%"
net share >> "%logFile%"
echo. >> "%logFile%"

:: 5. 시스템 기본보안설정
echo [5. 시스템 보안 설정] >> "%logFile%"
echo 방화벽 상태: >> "%logFile%"
netsh advfirewall show allprofiles >> "%logFile%"
echo. >> "%logFile%"
echo 계정 정책: >> "%logFile%"
net accounts >> "%logFile%"
echo. >> "%logFile%"

:: 6. 실행중인 서비스 목록
echo [6. 실행중인 서비스 목록] >> "%logFile%"
sc query state= all >> "%logFile%"
echo. >> "%logFile%"

:: 7. 공유된 파일 실행 여부
echo [7. 열린 파일 목록] >> "%logFile%"
openfiles /query >> "%logFile%"
echo. >> "%logFile%"

:: 8. 프로세스 정보
echo [8. 프로세스 정보] >> "%logFile%"
echo 상세 프로세스 목록: >> "%logFile%"
tasklist /v >> "%logFile%"
echo. >> "%logFile%"
echo 프로세스별 메모리 사용량: >> "%logFile%"
tasklist /FO TABLE /NH | sort /R /+65 >> "%logFile%"
echo. >> "%logFile%"

:: 9. 네트워크 관련정보
echo [9. 네트워크 정보] >> "%logFile%"
echo IP 구성: >> "%logFile%"
ipconfig /all >> "%logFile%"
echo. >> "%logFile%"
echo 활성 연결: >> "%logFile%"
netstat -ano >> "%logFile%"
echo. >> "%logFile%"
echo 라우팅 테이블: >> "%logFile%"
route print >> "%logFile%"
echo. >> "%logFile%"

:: 10. 파일 생성/수정/접근 이력
echo [10. 최근 파일 변경 이력] >> "%logFile%"
echo 최근 24시간 내 수정된 파일: >> "%logFile%"
forfiles /P C:\ /S /D -1 /C "cmd /c echo @path @fdate @ftime" 2>nul >> "%logFile%"
echo. >> "%logFile%"

:: 11. 시작프로그램 목록
echo [11. 시작프로그램 목록] >> "%logFile%"
echo 시작 메뉴 시작프로그램: >> "%logFile%"
dir /B "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup" >> "%logFile%"
echo. >> "%logFile%"
echo 레지스트리 시작프로그램: >> "%logFile%"
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" >> "%logFile%"
reg query "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" >> "%logFile%"
echo. >> "%logFile%"

:: 종료 시간 기록
echo [시스템 정보 수집 종료 시간] >> "%logFile%"
echo 종료 시간: %date% %time% >> "%logFile%"

:: 완료 메시지
echo 시스템 정보 수집이 완료되었습니다.
echo 결과 파일 위치: %logFile%
pause