# 키보드로 부서 번호 입력 받아 해당 부서에 근무하는 직원 출력.

import pymysql, sys
pymysql.install_as_MySQLdb()

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123',
    'database': 'test',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True
}


try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    jikwon_jik = input("직급입력: ")
    sql = f"select jikwon_no, jikwon_name, jikwon_jik, buser_num, jikwon_pay " \
          f"from jikwon " \
          f"where jikwon_jik='{jikwon_jik}'"
    cursor.execute(sql)
    datas = cursor.fetchall()

    if len(datas) == 0:
        print(str(jikwon_jik) + "번 부서가 없어요")
        sys.exit()

    for idx, d in enumerate(datas):
        if idx == 0:
            print('사번\t직원명\t직급\t부서번호\t연봉\t')
        else:
            print(d[0], d[1], d[2], d[3], d[4])

    print("인원수(작성자 장중건) : " + str(len(datas)))

except Exception as e:
    print('err : ', e)
finally:
    cursor.close()
    conn.close()


