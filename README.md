## Simple Banking System  
Прогорамма имитирует простейшую систему управления счетом.  
После запуска программы предлагаются следующие действия  
1) Создать счет  
2) Залогиниться  
3) Выйти
При создании счета пользователю выводится информация о номере счетаб за основу взят 16-и значный номер банковских карт, который генерируется случайным образом, последняя цифра выссчитывается по алгоритму Луна (подробнее с алгоритмом можно ознакомится по [ссылке](https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9B%D1%83%D0%BD%D0%B0)), и pin-код, так же сгенерированный случайно (в данный момент существует проблема со счетами, pin-код которых начинается на 0, в будущем будет исправлено). Информация о счете сохряняется в базу данных, потому при перезапуске программы можно получить доступ к счетам, созданных в предыдущие запуски. Для работы программы не требуется каких-либо сторонних приложений, база данных хранится в файле, создающимся при первом запуске программы.  
При выборе опции "Залогиниться" будет запрошен номер счета, потом pin-код. При ошибке в вводе программа вернет пользователя на начальный экран и выведет сообщение об ошибке и будет преложено попробовать снова. При успеной авторизации пользователь попадает в следующее меню:  
1) Узнать баланс  
2) Пополнить баланс  
3) Перевести средства на другой счет  
4) Закрыть счет  
5) Разлогиниться  
0) Выйти из программы  
При выборе первого пункта на экран будет выведено количество средств на счету (при создании счета баланс, что логично, будет равняться 0)  
При пополнении баланса у пользователя будет запрошенно ввести сумму пополнения  
При переводе денег на другой счет будет запрошен счет на который необходимо перечислить средства. После ввода счета получателя существуют следующие варианты: 
- Номер счета состоит не из 16 цифр, или не соответствует набору цифр, удовлетворяющих алгоритму Луна - будет выведено сообщение о возможной ошибке ввода
- Номер счета подходит под алгоритм Луна, но в базе данных такого счета нет - пользователя проинформируют, что такого счета нет  
- Пользователь укажет номер своего собственного счета - будет выведено сообщение, что перевод самому себе нельзя осуществить
При удачном прохождении всех проверок будет запрошена сумма перевода. Перевод будет осуществлен (спишется с баланса текущего счета и припишется к балансу счета-получателя) только в случае наличия на балансе достаточного количества средств, иначе будет выведено сообщение о недостаточном количестве средств и пользователь вернется в меню счета.  
При закрытии счета пользователь выйдет в начальное меню, а информация о его счете будет стерта из баззы данных.  
При разлогинивании пользователь просто выйдет в начальное меню.  
При выходе будет осуществлен выход из программы.
