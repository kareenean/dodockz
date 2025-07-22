# dodockz 
Вам нужно развернуть n8n в Docker для работы AI агента, который обрабатывает медицинские запросы через вебхук (http://localhost:5678/webhook/ai-agent). AI агент подключается к удаленной PostgreSQL-базе данных через SSH-туннель для сохранения рабочих процессов и данных. PHP-бэкенд будет отправлять POST-запросы на вебхук с полями chatInput (например, "клиника по хирургии") и sessionId (например, "test2") и обрабатывать JSON или текстовые ответы. 
 AI агент использует JavaScript-код для обработки запросов, сопоставляя симптомы или ключевые слова с данными врачей и клиник из PostgreSQL. 

В данном репозитрии также находится тестовый питон файл, ориентируйтесь на него. Вы можете протестировать работу процесса запустив питон файл. В дальнейшем вам надо будет позаботиться о том чтобы ваш бэк сам создавал уникальные sessionID.


Требования:
- Docker и Docker Compose
- Рабочий процесс n8n (Пожалуйста, убедитесь что он находится в папке n8n_data.) Название файла: final_workflow_dodoc.json
- Доступ к БД 

### Шаг 1. 
Склонируйте проект через терминал и перейдите в папку с проектом
```bash
git clone git@github.com:kareenean/dodockz.git
cd dodockz
```

### Шаг 2.
Запустите Docker
```bash
docker compose up -d
```

Пожалуйста, убедитесь что сервис запущен. 
```bash
docker ps
```

### Шаг 3. 
Откройте n8n в браузере по адресу http://localhost:5678 
Авторизуйтесь.

### Шаг 4. 
После авторизации, нажмите на кнопку "Create Workflow", и далее перейдите в настройки проекта (три точки сверху, справа).
Оттуда импортируйте (выберите import from file) json файл из папки n8n_data находящийся в этом репозитории. 

### Шаг 5.
Нажмите на node PostgreSQL и настройте реквизиты для доступа к вашей базе данных. Также нажмите на subnode AI Agent под названием Memory и выберите реквизиты которые вы вводили ранее.
Нажмите на subnode AI Agent под названием OpenAI Chat Model и введите ваш API ключ с платформы OpenAI.

### Шаг 6. 
Запустите процесс (Execute Workflow). Протестируйте процесс с помощью команд:

```bash
curl -X POST http://localhost:5678/webhook/ai-agent -H "Content-Type: application/json" -d '{"chatInput": "найти хирурга по всему Казахстану", "sessionId": "test1"}'
curl -X POST http://localhost:5678/webhook/ai-agent -H "Content-Type: application/json" -d '{"chatInput": "лучший хирург Казахстана", "sessionId": "test2"}'
curl -X POST http://localhost:5678/webhook/ai-agent -H "Content-Type: application/json" -d '{"chatInput": "лучшая клиника по хирургии", "sessionId": "test3"}'
curl -X POST http://localhost:5678/webhook/ai-agent -H "Content-Type: application/json" -d '{"chatInput": "узи в астане", "sessionId": "test4"}'
```

ИЛИ запустив test.py