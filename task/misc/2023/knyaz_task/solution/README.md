# Решение

Пытаемся поставить прокси в каком-либо виде, получаем ошибки в приложении. 

Находим reFlutter, перекомпилируем приложение с дампом трафика по адресу, переподписываем с помощью uber-apk-signer.

Ставим Burp Proxy, настраиваем, чтобы он слушал на порту, на который кидает пакеты перекомпилированное приложение.

Видим, что на запрос не прикрепляются нужные заголовки. Прикрепляем их к новому запросу по тому же адресу - получаем флаг.