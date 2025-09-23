def my_add(a, b) :
    return a + b


def my_sub(a, b) :
    return a - b

print(f"mymodule 안에서의 __name__ : {__name__}")

# 이 파일이 모듈이 아닌 main으로서 실행되었을 경우 실행되는 구문
if __name__ == "__main__" :

    print(my_add(3, 4))
    print(my_sub(4, 10))