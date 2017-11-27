"""

Токи
====

Создание тока
-------------

Подключаем модуль токов

    >>> from domain_variables.current.current import Ikz, Units

Создание тока (По умолчанию, ток задается в А)

    >>> i1 = Ikz(10000.234453)

    >>> print(i1)
    Iкз=10000.23, A

Доступ к значению

    >>> i1.value
    10000.234453

    >>> float(i1)
    10000.234453

    >>> int(i1)
    10000

Округление значения

    >>> round(i1, 2)
    10000.23

Сравнение токов
---------------

Сравнение значений

    >>> i1 = Ikz(10000.234453)
    >>> i2 = Ikz(10000.234453)
    >>> i1 == i2
    True

Сравнение значений с указанной точностью

    >>> i1 = Ikz(10000.234453)
    >>> i2 = Ikz(10000.230001)
    >>> i1.equal(i2, delta=0.0001)
    False

    >>> i1 = Ikz(10000.234453)
    >>> i2 = Ikz(10000.230001)
    >>> i1.equal(i2, delta=0.01)
    True

Какой ток больше?

    >>> i1 = Ikz(11.00, Units.kA)
    >>> print(i1)
    Iкз=11.00, kA
    >>> i2 = Ikz(10.35, Units.kA)
    >>> print(i2)
    Iкз=10.35, kA
    >>> i1 > i2
    True
    >>> i1 >= i2
    True
    >>> i1 < i2
    False
    >>> i1 <= i2
    False

Единицы измерения
-----------------

Создание тока в кА

    >>> i1 = Ikz(10, units=Units.kA)
    >>> print(i1)
    Iкз=10.00, kA

Сравнение токов в разных единицах

    >>> i1 = Ikz(20000)
    >>> i2 = i1.scale(i1.units.kA)
    >>> print(i1, i2, sep='; ')
    Iкз=20000.00, A; Iкз=20.00, kA
    >>> i1 == i2
    True
    >>> i1.equal(i2, delta=0.01)
    True

Создаем ток в стандартных единицах (А)

    >>> i1 = Ikz(15634.3456)
    >>> float(i1)
    15634.3456

В каких единицах текущий ток?

    >>> print(i1.units)
    A

Текущий ток в А?

    >>> i1.units == Units.A
    True

Переводим А -> кА

    >>> i2 = i1.scale(i1.units.kA)
    >>> float(i2)
    15.634345600000001

    >>> print(i1)
    Iкз=15634.35, A

    >>> print(i2)
    Iкз=15.63, kA

Исходные ток остался в А

    >>> print(i1)
    Iкз=15634.35, A

Точно ли исходный ток остался в А?

    >>> i1.units == Units.A
    True

Новый ток действительно в кА?

    >>> i2.units == Units.kA
    True

Переводим А -> А (ничего не должно поменяться)

    >>> float(i1)
    15634.3456
    >>> i2 = i1.scale(i1.units.A)
    >>> float(i2)
    15634.3456

Сложение токов
--------------

Создадим токи в А

    >>> i1 = Ikz(100)
    >>> print(i1)
    Iкз=100.00, A

    >>> i2 = Ikz(200)
    >>> print(i2)
    Iкз=200.00, A

Сложим два тока

    >>> i3 = i1 + i2
    >>> print(i3)
    I=300.00, A
    >>> print(i3.description)
    Результирующий ток

Значение результирующего тока

    >>> float(i3)
    300.0

Единицы измерения результирующего тока

    >>> i3.units == Units.A
    True

Создадим токи в А, кА

    >>> i1 = Ikz(100)
    >>> print(i1)
    Iкз=100.00, A
    >>> i2 = Ikz(0.20, Units.kA)
    >>> print(i2)
    Iкз=0.20, kA
    >>> i3 = i1 + i2
    >>> float(i3)
    300.0
    >>> i3.units == Units.A
    True

Вычитание токов
---------------

    >>> i1 = Ikz(80)
    >>> print(i1)
    Iкз=80.00, A
    >>> i2 = Ikz(100)
    >>> print(i2)
    Iкз=100.00, A
    >>> i3 = i2 - i1
    >>> print(i3)
    I=20.00, A

Разные имена токов

    >>> ikz = Ikz(80)
    >>> print(ikz)
    Iкз=80.00, A
    >>> print(ikz.description)
    Ток короткого замыкания

    >>> ied = Ied(100)
    >>> print(ied)
    Iэд=100.00, A
    >>> print(ied.description)
    Ток двигателей

    >>> i = ikz + ied
    >>> print(i)
    I=180.00, A
    >>> print(i.description)
    Результирующий ток
    >>> i = ied + ikz
    >>> print(i)
    I=180.00, A

"""

from domain_variables.current.current import Ied
