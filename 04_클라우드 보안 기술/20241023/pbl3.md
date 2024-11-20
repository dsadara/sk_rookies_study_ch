## PBL3

## IAM 정책
``` json
"Effect": "Allow",
"Action": "s3:*",
"Resource": "*"
```
해당 IAM 정책은 S3의 모든 리소스(`Resource:*`, ARN으로 구별)에 대해서 모든 작업(`Action:s3:*`)을 허용(`allow`)하는 구문이다.

## S3 버킷 정책
``` json
"Effect": "Deny",
"Principal": "user01",
"Action": "s3:PutObject",
"Resource": "*"
```
해당 정책은 `user01` 라는 IAM user가 모든 리소스를 대상(`Resource:*`)으로 객체를 업로드(`s3:PutObject`) 할 수 없는(`deny`) 정책이다

## 정책의 충돌

두 정책은 S3의 작업에 대해서 충돌이 발생한다.    
정책 평가 우선순위에 따르면 `explicit deny`가 우선순위를 가진다.    
따라서 `"Effect": "Deny"`를 가지는 S3 버킷 정책이 우선순위를 가진다.

## 결론
`user01` 은 모든 리소스에 대해 `PubObject - S3 버킷에 객체 업로드` 를 할 수 없다