Внутри - сильно обфусцированный python-скрипт под pyinstaller, который при запуске долго считает,
использует много криптографии для расшифровки блоба, самый последний слой расшифрует текст
форк-бомбы, подобрав последние два байта своего ключа.

А сама нагрузка находится в pyinstaller-лоадере, который запускает скрипт, вшитый в него,
после отработки основной нагрузки. Проверяет наличие в качестве первого аргумента
"please_stop_this_madness". В этом случае скрипт берет второй параметр, и проверяет его
по достаточно простой системе уравнений (подробнее в ./project/gen_expression).