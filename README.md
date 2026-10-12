# Team-Incredibles-project

Репозиторий бригады № 1 группы 644, команда **Incredibles**.

Дисциплина «Введение в профессиональную деятельность», кафедра вычислительной и прикладной математики, РГРТУ имени В. Ф. Уткина.

Репозиторий: https://github.com/arsLnD/Team-Incredibles-project

## Состав

| Участник | Роль |
|---|---|
| Гужва Дарья | Аналитик |
| Алымова Виктория | UX/UI-дизайнер |
| Алоян Натали | Тестировщик |
| Акилина Анастасия | Разработчик |
| Евстигнеев Арсений | Менеджер проекта |

## Документы

- [Командный контракт](docs/team-contract.md)
- [Роли и ответственность](docs/roles-and-responsibilities.md)
- [Матрица RACI](docs/raci-matrix.md)
- [Самостоятельная работа 1](practical-works/practical-work-01/report.md)
- [Самостоятельная работа 2](practical-works/practical-work-02/report.md)

## Структура

```text
team-incredibles-project/
├── README.md
├── docs/
│   ├── team-contract.md
│   ├── roles-and-responsibilities.md
│   └── raci-matrix.md
├── practical-works/
│   ├── practical-work-01/
│   │   ├── report.md
│   │   └── assets/
│   ├── practical-work-02/
│   │   ├── report.md
│   │   └── assets/
│   ├── practical-work-03/ … practical-work-08/
│   │   ├── report.md
│   │   └── src/
├── scripts/
│   ├── check-structure.py
│   ├── check-structure.sh
│   └── check-structure.bat
└── .gitignore
```

Работы 01 и 02 хранят материалы в `assets/`. Работы 03–08 хранят код в `src/`.

Проверка структуры:

```bash
python3 scripts/check-structure.py
```
