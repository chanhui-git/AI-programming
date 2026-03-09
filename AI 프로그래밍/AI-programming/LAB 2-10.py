Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #LAB 2-10 : 사용자 입력 받기
>>> name = input('이름을 입력하세요 : ')
이름을 입력하세요 : 김찬희
>>> print(name, '님이 입장하셨습니다.')
김찬희 님이 입장하셨습니다.
>>> m = int(input('숫자 m을 입력하세요 : '))
숫자 m을 입력하세요 : 30
>>> n = int(input('숫자 n을 입력하세요 : '))
숫자 n을 입력하세요 : 50
>>> print('m + n =', m+n)
m + n = 80
>>> print('m - n =', m - n)
m - n = -20
>>> 
>>> radius = input('반지름을 입력하세요 : ')
반지름을 입력하세요 : 
>>> radius = ㅑint(input('반지름을 입력하세요 : '))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    radius = ㅑint(input('반지름을 입력하세요 : '))
NameError: name 'ᅣint' is not defined
>>> radius = int(input('반지름을 입력하세요 : '))
반지름을 입력하세요 : 20
>>> print('면적 : ', radius ** 2 * 3.14)
면적 :  1256.0
