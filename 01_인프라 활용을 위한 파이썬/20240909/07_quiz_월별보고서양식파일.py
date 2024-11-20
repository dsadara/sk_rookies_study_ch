for month in range(1, 13):
    with open(f'{month}월_보고서.txt', 'w', encoding='utf-8') as report:
        report.write(f'{month}월 보고서\n')
        report.write('작성자: \n')
        report.write('주요 내용: \n')
        report.write('결과 및 피드백: \n')