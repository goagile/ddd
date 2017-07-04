(function() {

    function Person(name) {
        this.name = name;
        this.country = 'Россия';
    }

    function getTableHeader() {
        var header = [
            'Фамилия по паспорту',
            'Имя: ',
            'От4ество?!.',
            'Иденти-фикационный код\|/номер'
        ];
    }

    return Person;

}());
