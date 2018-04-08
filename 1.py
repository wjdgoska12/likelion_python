#sys2.py
#앞 부분은 대화형 인터프린터에서 해서 가장 마지막 실습을 깃헙에 올리겠습니다.
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
