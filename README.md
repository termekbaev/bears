# Тестовое задание
Написать стратегию тестирования CRUD сервиса, написать тесты в любом формате, автоматизировать выборочно несколько тестов с использованием python + pytest

# Подготовка
Использовал DockerDesktop
Получл образ alaska
Запустил контейнер из образа с пробросом портов 8090:8091

# Запуск тестов
Запуск тестов происходит из корневого каталога командой:  
pytest test_api.py -v  

или для сохранения отчета в файл test_results.txt:  
pytest test_api.py -v > test_results.txt

# Стратегия тестирования
Описана в tests.md