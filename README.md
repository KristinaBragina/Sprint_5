## Спринт 5, UI-тестирование
### Курс по автоматизации тестирования на Python, «Яндекс Практикум»
### Stellar Burgers

Проект по автоматизации тестирования сервиса **Stellar Burgers** 
`https://stellarburgers.nomoreparties.site/`

Это космический фастфуд: здесь можно собрать и заказать бургер из необычных ингредиентов.

Приложение сервиса — это тоже учебный проект. Его написал студент «Практикума» на курсе по разработке на React.

### Структура репозитория

Корневая директория проекта содержит набор тестов и файлы со вспомогательными инструментами:

- в папке tests лежат файлы с тестами, отсортированными по тестируемой функциональности приложения;
- файл conftest хранит фикстуры, необходимые для запуска тестов;
- файл locators определяет и описывает локаторы, используемые в тестах;
- файл README объясняет суть происходящего и служит руководством. :)

### Покрытие

Проект не требует полностью покрыть приложение тестами. В рамках тестирования нужно было проверить исполнение конкретных функциональных требований:

&#10003; тесты в файле [test_registrarion](https://github.com/KristinaBragina/Sprint_5/blob/develop/tests/test_registrarion.py) проверяют позитивные и некоторые негативные сценарии при заполнении полей формы регистрации;

&#10003; тесты в файле [test_authentication](https://github.com/KristinaBragina/Sprint_5/blob/develop/tests/test_authentication.py) покрывают четыре сценария аутентификации в приложении;

&#10003; тесты в файле [test_navigate_to_constructor](https://github.com/KristinaBragina/Sprint_5/blob/develop/tests/test_navigate_to_constructor.py) покрывают два сцерания перехода в конструктор бургера из личного кабинета пользователя;

&#10003; тест в файле [test_navigate_to_personal_account](https://github.com/KristinaBragina/Sprint_5/blob/develop/tests/test_navigate_to_personal_account.py) проверяет функциональность перехода в личный кабинет с главной страницы;

&#10003; тесты в файле [test_switch_blocks_on_constructor](https://github.com/KristinaBragina/Sprint_5/blob/develop/tests/test_switch_blocks_on_constructor.py) исследуют переключение разделов в меню конструктора;

&#10003; тест в файле [test_logout](https://github.com/KristinaBragina/Sprint_5/blob/develop/tests/test_logout.py) проверяет функциональность выхода из аккаунта.

### Запуск всех тестов

Команда для терминала, запускающая все тесты: `pytest -v`.
