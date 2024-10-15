## ASP + MSSQL 사이트 환경
* 대상 사이트: http://210.95.67.235:8181/

# 정보수집단계 - 서브도메인 파악 - fierce
` sudo fierce --domain http://210.95.67.235:8181/ `

### Fierce 수행 결과
![alt text](image.png)

# 정보수집단계 - 서브도메인 파악 - netcraft 검색
* 수행 결과: https://sitereport.netcraft.com/?url=http://210.95.67.235

### Network 정보
![alt text](image-2.png)

### IP 주소 범위
![alt text](image-3.png)

### SSL/TLS
HTTPS를 사용하고 있지 않으므로 SSL을 적용하지 않음
![alt text](image-4.png)

# 정보수집단계 - 서브도메인 파악 - whois 검색
[KISA 후이즈검색](https://xn--c79as89aj0e29b77z.xn--3e0b707e/)   
* 네트워크 할당 정보
    ![alt text](image-5.png)

# 정보수집단계 - 포트 점검 - nmap 사용
수집한 IP 주소로 포트 스캔 수행, -sV 옵션으로 버전 정보까지 확인   
` sudo nmap -sV http://210.95.67.235 -p- `
아직 진행중입니다..
![alt text](image-6.png)

# 정보수집단계 - OSINT (Criminal IP) 사용

https://www.criminalip.io/ko/asset/report/210.95.67.235

### Malicious IP
해당 IP는 Malicious IP 라고 나옴
* malicious IP is any IP address that has been positively associated with malicious activity

![alt text](image-8.png)

### 취약점 요약
![alt text](image-9.png)
* Open Ports: 열려진 포트 4개
* Vulnerabilities: 취약점 93개
* Explot DB: 24개
* 기타 등등   

### WHOIS 정보
![alt text](image-10.png)

#### 취약점1 - CVE-2023-45802
![alt text](image-11.png)

#### 취약점2 - CVE-2023-31122
![alt text](image-12.png)

#### 취약점3 - CVE-2023-28625
![alt text](image-13.png)

#### 취약점4 - CVE-2022-37436
![alt text](image-14.png)

# 정보수집단계 - 구글 해킹 취약점 체크

### robots.txt 체크
robots.txt 페이지가 존재하지 않음
* https://testphp.vulnweb.com/robots.txt

### 구글해킹 시도

웹사이트가 구글 검색엔진에 등록되어 있지 않아 구글해킹 취약점은 발견할 수 없었다.

![alt text](image-1.png)

* 사용 검색어   
` site:210.95.67.235:8181 inurl:admin ` 
` site:210.95.67.235:8181 intext:password `
` site:210.95.67.235:8181 inurl:admin filetype:xlsx `
` site:210.95.67.235:8181 filetype:php `
` site:210.95.67.235:8181 filetype:php `
` site:210.95.67.235:8181 filetype:php `

## 취약점 분석 단계 - Nikto
` sudo nikto -h http://210.95.67.235:8181 `

```
[sudo] password for kali: 
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          210.95.67.235
+ Target Hostname:    210.95.67.235
+ Target Port:        8181
+ Start Time:         2024-10-15 04:28:06 (GMT-4)
---------------------------------------------------------------------------
+ Server: Microsoft-IIS/6.0
+ /: Cookie ASPSESSIONIDQQRRCQBT created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ /: Retrieved x-powered-by header: ASP.NET.
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /images: The web server may reveal its internal or real IP in the Location header via a request to with HTTP/1.0. The value is "192.168.0.94". See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2000-0649
+ OPTIONS: Allowed HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST .
+ OPTIONS: Public HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST .
+ /?mod=<script>alert(document.cookie)</script>&op=browse: Sage 1.0b3 is vulnerable to Cross Site Scripting (XSS). See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1243
+ /admin/: This might be interesting.
+ /Admin/: This might be interesting.
+ /admin/index.asp: Admin login page/section found.
+ 8110 requests: 1 error(s) and 11 item(s) reported on remote host
+ End Time:           2024-10-15 04:32:17 (GMT-4) (251 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

## 취약점 분석 단계 - dirb
` sudo dirb http://210.95.67.235 `