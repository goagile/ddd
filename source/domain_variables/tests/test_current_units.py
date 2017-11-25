"""

Подключение

    >>> from domain_variables.currents.currents_units import Units

Перевод

    >>> Units.kA.A(12.345)
    (12345.0, A)

    >>> str(Units.kA)
    'kA'

    >>> v, u = Units.A.kA(10000)
    >>> v, u
    (10.0, kA)

    >>> Units.kA == u
    True

"""
