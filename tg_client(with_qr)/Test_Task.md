Тестовое задание для Python-программиста: Разработка Telegram-клиента с использованием Telethon

Цель задания: Разработать Telegram-клиент на Python с использованием библиотеки Telethon. Клиент должен иметь веб интерфейс и api с возможностью авторизации по QR-коду, получение и отправку текстовых сообщений.

Требования:

Создайте новое приложение в https://my.telegram.org/ и получите API ID и API HASH.
Используя библиотеку python Telethon, разработайте web сервис, реализующий следующую функциональность:
Логин клиента по QR-коду.
Получение новых текстовых сообщений и их сохранение, разделенное по чатам.
Возможность отправки текстовых сообщений другим пользователям через клиента.
Реализуйте базовый веб-API интерфейс с использованием Flask (или любого другого фреймворка на ваш выбор) с методами, описанными ниже. Если будет покрыто тестами - большой плюс.
При запросе "wild: любой товар", должен запускаться парсинг wildberries с городом Москва и запросом "любой товар", бот должен отправлять 10 наименований товаров со ссылками на них.
POST /login
REQUEST
{
   phone: '79092991111'
}
RESPONSE
{
	qr_link_url: 'https://'
}
GET /check/login?phone=79092991111
RESPONSE
{
	status: 'waiting_qr_login' // or logined or error
}
GET /messages?phone=790929911111&uname=chat_username
RESPONSE
{
	messages: [ // last 50 messages 
		{
			username: '',
			is_self: false, //true
			message_text: ''
		}
	]
}
POST /messages
REQUEST
{
	message_text: 'привет!'
	from_phone: '790929911111',
	username: 'testname'
}
RESPONSE
{
	status: 'ok' //error
}