## <span style="color:MediumPurple">Проект по автоматизации UI-тестов для сервиса **Stellar Burgers**</span> 
`https://stellarburgers.nomoreparties.site/` 

#### Курс по автоматизации тестирования на Python, «Яндекс Практикум»
#### Спринт 5, UI-тестирование

---
### <span style="color:DarkOrchid">Отправляемся в космический гастротур</span>
Stellar Burgers — это внеземной фастфуд: здесь можно собрать и заказать бургер из необычных ингредиентов. Приложение сервиса тоже является учебным проектом. Его написал студент «Практикума» в рамках курса по разработке на React.

Вовремя подкрепиться — главное в исследовании далеких цивилизаций. Автотесты с использованием pytest и Selenium проверят, что интерфейс приложения работает как космический корабль: без сбоев. 

### <span style="color:SlateBlue">Снаряжение инопланетной миссии</span>

Корневая директория проекта содержит набор тестов и файлы со вспомогательными инструментами, которые пригодятся в путешествии:

- в папке [tests](https://github.com/KristinaBragina/Sprint_5/tree/develop/tests) лежат файлы с тестами, для каждой функциональности — свой файл;
- файл [conftest](https://github.com/KristinaBragina/Sprint_5/blob/develop/conftest.py) хранит фикстуры, необходимые для запуска тестов;
- файл [locators](https://github.com/KristinaBragina/Sprint_5/blob/develop/locators.py) определяет и описывает локаторы, используемые в тестах;
- файл [data](https://github.com/KristinaBragina/Sprint_5/blob/develop/data.py) хранит тестовые данные полей ввода;
- файл [helpers](https://github.com/KristinaBragina/Sprint_5/blob/develop/helpers.py) содержит функции, генерирующие рандомные данные для тестов регистрации;
- файл [README](https://github.com/KristinaBragina/Sprint_5/blob/develop/README.md) объясняет суть происходящего и служит руководством. :)

### <span style="color:RoyalBlue">Маршрут полета</span>

Задание проекта не требует полностью покрыть приложение тестами. В рамках тестирования нужно было проверить исполнение конкретных функциональных требований:

&#10003; тесты в файле [test_registrarion](https://github.com/KristinaBragina/Sprint_5/blob/develop/tests/test_registrarion.py) проверяют позитивные и некоторые негативные сценарии при заполнении полей формы регистрации;

&#10003; тесты в файле [test_authentication](https://github.com/KristinaBragina/Sprint_5/blob/develop/tests/test_authentication.py) покрывают четыре сценария аутентификации в приложении;

&#10003; тесты в файле [test_navigate_to_constructor](https://github.com/KristinaBragina/Sprint_5/blob/develop/tests/test_navigate_to_constructor.py) покрывают два сцерания перехода в конструктор бургера из личного кабинета пользователя;

&#10003; тест в файле [test_navigate_to_personal_account](https://github.com/KristinaBragina/Sprint_5/blob/develop/tests/test_navigate_to_personal_account.py) проверяет функциональность перехода в личный кабинет с главной страницы;

&#10003; тесты в файле [test_switch_blocks_on_constructor](https://github.com/KristinaBragina/Sprint_5/blob/develop/tests/test_switch_blocks_on_constructor.py) исследуют переключение разделов в меню конструктора;

&#10003; тест в файле [test_logout](https://github.com/KristinaBragina/Sprint_5/blob/develop/tests/test_logout.py) проверяет функциональность выхода из аккаунта.

### <span style="color:Brown">Стартуем, капитан!</span>

Команда для терминала, запускающая все тесты: `pytest -v`.
