


def divide(a, b):

    try :
        division = a / b
    except ZeroDivisionError:
        return f'B is {b}, cannot be divided by zero!'

    except TypeError:
        return "Only integer allowed"

    return division

ans = divide(10,0)
print(ans)

git config --global user.name "namanmishraaa"
git config --global user.email "pmishra0850@gmail.com"   