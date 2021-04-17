"""Написать функцию month_to_season(), которая принимает
1 аргумент - номер месяца - и возвращает название сезона,
к которому относится этот месяц.
Например, передаем 2, на выходе получаем 'Зима'. """

# Способ 1
def month_to_season(numberMonth):

    result = ""
    if 8 < numberMonth < 12 :
        result = "Осень"
        return(result)
    elif 2 < numberMonth < 6:
        result = "Весна"
        return result
    elif 5 < numberMonth < 9:
        result = "Лето"
        return result
    elif numberMonth > 12:
        result = "Такого месяца не существует"
        return result
    else:
        result = "Зима"
        return result

# Способ 2
def month_to_season2(numberMonth2):
    d = {
        (12, 1, 2): "Зима",
        (3, 4, 5): "Весна",
        (6, 7, 8): "Лето",
        (9, 10, 11): "Осень"
    }
    result2 = ""

    for item, value in d.items():
        if numberMonth2 in item:
            result2 = value
            break
        else:
            result2 = "Такого месяца не существует"
    return result2


if __name__ == '__main__':
    p = month_to_season2(2)
    print(p)

