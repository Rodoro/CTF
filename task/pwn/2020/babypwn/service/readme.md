# babypwn
## Условие
> Программа спросит у вас имя. Надо упеть и ответить, и забрать флаг.
> nc address 44400

## Решение
> Запуск: docker-compose up --build -d
> Флаг в файле service/flag - iset{Wh4t_ar3_you_4_hack3r?}
> Решение: Флаг печатается в функции secret, но она не вызывается. 
> Есть возможность переполнить переменную name, и изменить регистр rip 
> на адрес функции secret.