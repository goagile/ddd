

class ContainerFeature:
    ARMORED = 'Armored'


class ContainerSpecification:

    def __init__(self, feature):
        self.__feature = feature

    def is_satisfied_by(self, container):
        return bool(self.__feature in container.features)


class Container:

    def __init__(self):
        self.__specs = []
        self.__features = []

    @property
    def specs(self):
        return self.__specs

    @property
    def features(self):
        return self.__features

    def add_spec(self, spec: ContainerSpecification):
        self.__specs.append(spec)

    def add_feature(self, feature: str):
        self.__features.append(feature)

    def is_safely_packed(self):
        for spec in self.__specs:
            if not spec.is_satisfied_by(self):
                return False
        return True
