"""

    >>> from tablo import joinrow, Align, Format

    >>> sequence = ['X', 'Y', 'Z', 'A', 'B']

    >>> row = [
    ...     ('4',   Format(Align.Left, margin=3)),
    ...     ('Нет', Format(Align.Left, margin=3)),
    ...     ('112.003', Format(Align.Left, margin=10)),
    ... ]

    >>> joinrow(row)
    '|4  |Нет|112.003   |'

"""
