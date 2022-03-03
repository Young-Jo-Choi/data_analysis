# decorator :  간단하게 함수 재정의라고 생각하면 쉬움


def copyright(func):
    def new_func():
        print("@written by Choi")
        func()

    return new_func


@copyright
def smile():
    print("smile")


def angry():
    print("angry")


@copyright
def love():
    print("love")


""" 다음과 같이 하면 함수 재정의가 가능하지만 너무 번거로움
smile = copyright(smile)
angry = copyright(angry)
love = copyright(love)

smile과 love 위에는 decorator를 붙여 간단하게 재정의 했으므로 실행결과를 비교하시오
"""

smile()
angry()
love()
