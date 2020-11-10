### 1. Интернет-магазин.
Написать простой интернет-магазин.
Либо бэкенд + готовый набор скриптов для теста API (Postman и аналогичные), либо бэкенд + фронтенд любым способом.
Модели (типы полей выбрать из представляемых фреймворком):
- Учетные записи пользователей: ФИО, адрес доставки, email (он же логин), пароль, роль.
- Роли пользователей: клиент, менеджер.
- Товары: артикул (текст), наименование, цена закуп, цена розница.
- Корзина: клиент, товар, количество, цена, сумма по строке.

Интерфейсы:
- авторизация
- добавление товаров в корзину

Особенности:
- управление учетками и товарами - через Django админку.
- корзина доступна на просмотр и редактирование только клиенту-владельцу и любому менеджеру.
- у клиента может быть только одна активная корзина.

### 2. Интеграция с внешним поставщиком
Написать скрипт, который загрузит файл с товарами поставщика в наш интернет-магазин.
Файл https://gist.github.com/Wanderernk/1f3af500435bef872af2b6f3cc8e79fc

Сопоставление полей:
- Артикул = "ПТ"+"КодТовараПоставщика"
- Наименование товара = "НаименованиеТовараПоставщика"
- Цена закуп = 0.9 * "ЦенаПоставщика"
- Цена розница = если "ЦенаПоставщика" < 1000 руб, то 1.2 * "ЦенаПоставщика". иначе 1.1 * "ЦенаПоставщика"

### 3. Печать сопроводительных документов (по желанию)
Требования:
- асинхронно через Celery
- поля (по одному на строку): Клиент, Номер заказа, Адрес доставки.
- на выходе должен быть PDF файл в каталоге, предназначенном для хранения этих файлов.
- использовать wkhtmltopdf.
