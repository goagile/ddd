"""

Подключение

    >>> from domain_variables.current.units import Units, registry_of_units

Перевод

    >>> t = Units.kA.A(12.345)
    >>> t.new_value, t.new_units
    (12345.0, A)

    >>> str(Units.kA)
    'kA'

    >>> t = Units.A.kA(10000)
    >>> t.new_value, t.new_units
    (10.0, kA)

    >>> Units.kA == t.new_units
    True

Восстановление из строки

    >>> u = registry_of_units.get('А')
    >>> print(u)
    A


"""
