from python.과제.조성완_0304 import update_sungjuk


class Sungjuk:
    def __init__(self):
        self._hakbun = ""
        self._irum = ''
        self._korean = 0
        self._english = 0
        self._math = 0
        self._total = 0
        self._avg = 0
        self._grade = ''

    def get_hakbun(self):
        return self._hakbun
    def set_hakbun(self,hakbun):
        self._hakbun = hakbun
    hakbun = property(get_hakbun,set_hakbun)

    def get_irum(self):
        return self._irum
    def set_irum(self,irum):
        self._irum = irum
    irum = property(get_irum,set_irum)

    def get_korean(self):
        return self._korean
    def set_korean(self,korean):
        self._korean = korean
    korean = property(get_korean,set_korean)

    def get_english(self):
        return self._english
    def set_english(self,english):
        self._english = english
    english = property(get_english,set_english)

    def get_math(self):
        return self._math
    def set_math(self,math):
        self._math = math
    math = property(get_math,set_math)

    def get_total(self):
        return self._total
    def set_total(self,total):
        self._total = total
    total = property(get_total,set_total)

    def get_avg(self):
        return self._avg
    def set_avg(self,avg):
        self._avg = avg
    avg = property(get_avg,set_avg)

    def get_grade(self):
        return self._grade
    def set_grade(self,grade):
        self._grade = grade
    grade = property(get_grade,set_grade)

    def input_sungjuk(self):
        self._hakbun = input("학번을 입력하세요:")
        self._irum = input("이름을 입력하세요:")
        self.update_sungjuk()

    def update_sungjuk(self):
        self._korean = int(input("국어 점수를 입력하세요:"))
        self._english = int(input("영어 점수를 입력하세요:"))
        self._math = int(input("수학 점수를 입력하세요:"))


    def process_sungjuk(self):
        self._total = self._korean + self._english + self._math
        self._avg = self._total / 3
        if self._avg >= 90:
            self._grade = '수'
        elif self._avg >= 80:
            self._grade = '우'
        elif self._avg >= 70:
            self._grade = '미'
        elif self._avg >= 60:
            self._grade = '양'
        else:
            self._grade = '가'

    def output_sungjuk(self):
        print("%4s %4s %4d %4d %4d %4d %5.2f %3s" % (self._hakbun, self._irum, self._korean,
                                                     self._english, self._math, self._total,
                                                     self._avg, self._grade))

if __name__ == "__main__":
    obj = Sungjuk()
    obj.input_sungjuk()
    obj.process_sungjuk()
    print("\t\t\t***성적표***")
    print("==========================================")
    print("학번   이름   국어  영어  수학  총점  평균  등급")
    print("==========================================")
    obj.output_sungjuk()
    print("==========================================")