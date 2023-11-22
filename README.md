# worck


Название проекта: Django Tree Menu

Описание:
Проект Django Tree Menu представляет собой Django-приложение для создания и управления древовидными меню с использованием стандартной административной панели Django. Меню хранится в базе данных, что обеспечивает удобное редактирование через административный интерфейс.

Особенности:
1. Множество меню: Позволяет создавать неограниченное количество меню на основе их названий.
2.Хранение в БД: Меню хранится в базе данных Django, что обеспечивает эффективное управление и редактирование.
3.Template Tag для отрисовки:** Использует Django Template Tag для удобного встраивания меню в шаблоны страниц.
4.Активный пункт меню:** Определяет активный пункт меню на основе текущего URL страницы.
5.Развертывание меню:** Первый уровень и подуровни разворачиваются под выделенным пунктом меню.
6.URL: Поддерживает как явное указание URL, так и использование named URL для каждого пункта меню.
7.Эффективность: Для отрисовки каждого меню требуется ровно 1 запрос к базе данных.

Структура проекта:
- `menu/`: Django-приложение для управления меню.
  - `models.py`: Определение модели MenuItem для хранения данных о пунктах меню.
  - `admin.py`: Настройка административного интерфейса Django для удобного редактирования меню.
  - `templatetags/menu_tags.py`: Шаблонный тег для отрисовки меню в шаблонах страниц.
- `templates/`: Шаблоны для страниц, включая основной шаблон, где используется меню.
- `settings.py`: Настройки Django, включая подключение приложения к проекту.

Использование:
1. Установите Django Tree Menu в ваш проект Django.
2. Создайте меню через административный интерфейс, указав названия, URL и иерархию пунктов.
3. Вставьте Template Tag `{% draw_menu 'main_menu' request.path %}` в ваш шаблон страницы для отображения меню.

