# 딕셔너리(dict) 관련 함수
# keys()
# 딕셔너리 객체의 키(key)를 리스트 형식으로 반환한다.
#
# values()
# 딕셔너리 객체의 값(value)을 리스트 형식으로 반환한다.
#
# items()
# 딕셔너리 객체의 키(key)와 값(value)을 튜플로 만들어 리스트 형식으로 반환한다.
#
# clear()
# 딕셔너리 객체 안의 모든 요소를 삭제한다.
#
# get()
# 키(key)에 대응되는 값(value)을 반환한다.
#
# in
# 해당 키가 딕셔너리 객체 내에 존재하는지 확인하여 True 혹은 False를 반환한다.

dct = {}
dct['id'] = 'hong'
dct['pw'] = '1234'
dct['email'] = 'hong@gmail.com'
print(dct)
print(dct.keys())
print(dct.values())
print(dct.items())
res = dct.get('id') # dct['id]
print(res)
dct.clear()
print(dct)