# Тестовый проект "Доска объявлений"

**Описание задачи**:  
Создать простую доску объявлений, где пользователи могут публиковать объявления, просматривать их по категориям и добавлять новые объявления.

## Основные компоненты:

### Модели:

- **Bb**: Представляет собой объявление с полями: заголовок, описание, цена, дата публикации и рубрика.
  
- **Rubric**: Категория или рубрика, к которой относится объявление.

### Формы:

- **BbForm**: Форма для добавления нового объявления.

### Представления:

- **index**: Главная страница со всеми объявлениями.

- **by_rubric**: Страница с объявлениями определенной рубрики.

- **BbCreateView**: Представление на основе класса для создания нового объявления.

### Маршруты (URLs):

- Главная страница
- Страница добавления нового объявления
- Страница просмотра объявлений по рубрике

### Админка:

- Регистрация моделей **Bb** и **Rubric** с базовой конфигурацией для удобства управления данными.

### Стили:

- Основной файл стилей для оформления внешнего вида сайта.

## Отчет по выполнению:

### Модели:

- Созданы две основные модели **Bb** и **Rubric** с соответствующими полями и метаданными.

### Формы:

- Реализована форма **BbForm** для добавления новых объявлений на основе модели **Bb**.

### Представления:

- Реализованы функции представления **index** и **by_rubric** для отображения объявлений.

- Реализовано представление на основе класса **BbCreateView** для создания новых объявлений.

### Маршруты (URLs):

- Определены маршруты для главной страницы, страницы добавления нового объявления и страницы просмотра объявлений по рубрике.

### Админка:

- Модели **Bb** и **Rubric** зарегистрированы в админке с базовыми настройками отображения.

### Стили:

- Создан основной файл стилей, который можно дополнить в дальнейшем для улучшения внешнего вида сайта.
