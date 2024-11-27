@echo off
chcp 65001
setlocal enabledelayedexpansion

set "startTime=%date% %time%"
set "resultFolder=%~dp0system_check_results"
set "datetime=%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%"
set "logFile=%resultFolder%\system_check_%datetime%.txt"
set "logFile=%resultFolder%\system_check_%datetime%.txt"

:: 결과 폴더 생성
if not exist "%resultFolder%" mkdir "%resultFolder%"

echo ================================================== > "%logFile%"
echo                시스템 정보 수집 보고서 >> "%logFile%"
echo ================================================== >> "%logFile%"
echo. >> "%logFile%"

:: 6. 실행중인 서비스 목록
echo [6. 실행중인 서비스 목록] >> "%logFile%"
sc query state= all >> "%logFile%"
echo. >> "%logFile%"

:: 7. 공유된 파일 실행 여부
echo [7. 열린 파일 목록] >> "%logFile%"
openfiles /query >> "%logFile%"
echo. >> "%logFile%"