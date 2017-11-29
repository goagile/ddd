from domain_variables.base.scalar_current_value import ScalarCurrentValue
from domain_variables.current.value import registry_of_currents
from domain_variables.current.units import registry_of_units


class CurrentSerializer:

    @classmethod
    def dumps(cls, curent: ScalarCurrentValue):
        result = {
            'name': curent.name,
            'value': curent.value,
            'units': str(curent.units)
        }
        return result

    @classmethod
    def loads(cls, dumped: dict):
        name = dumped.get('name')
        value = dumped.get('value')
        units = dumped.get('units')
        current_class = registry_of_currents.get(name)
        units_class = registry_of_units.get(units)
        result = current_class(value, units_class)
        return result
