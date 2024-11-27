@echo off
chcp 65001

:: 6. 실행중인 서비스 목록
echo [6번] >> test.txt
sc query state= all >> test.txt

:: 7. 공유된 파일 실행 여부
echo [7번] >> test.txt
openfiles /query >> test.txt