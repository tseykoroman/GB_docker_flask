# python-flask-docker
Итоговый проект курса "Машинное обучение в бизнесе"

Стек:

ML: sklearn, pandas, numpy
API: flask
Данные: с kaggle - https://www.kaggle.com/datasets/kukuroo3/body-signal-of-smoking

Задача: определить курит или нет пациент с помощью информации о его здоровье. Бинарная классификация.

Используемые признаки:

- description (text)
- company_profile (text)
- benefits (text)

- gender (text)
- age : 5-years gap (int)
- height(cm) (int)
- weight(kg) (int)
- waist(cm) : Waist circumference length (float)
- eyesight(left) (float)
- eyesight(right) (float)
- hearing(left) (int)
- hearing(right) (int)
- systolic : Blood pressure (int)
- relaxation : Blood pressure (int)
- fasting blood sugar (int)
- Cholesterol : total (int)
- triglyceride (int)
- HDL : cholesterol type (int)
- LDL : cholesterol type (int)
- hemoglobin (float)
- Urine protein (int)
- serum creatinine (float)
- AST : glutamic oxaloacetic transaminase type (int)
- ALT : glutamic oxaloacetic transaminase type (int)
- Gtp : γ-GTP (int)
- oral : Oral Examination status (text)
- dental caries (int)
- tartar : tartar status (text)

Модель: RandomForestClassifier

### Клонируем репозиторий и создаем образ
```
$ git clone https://github.com/tseykoroman/GB_docker_flask.git
$ cd GB_docker_flask
$ docker build -t GB_docker_flask .
```

### Запускаем контейнер

Здесь Вам нужно создать каталог локально и сохранить туда предобученную модель (<your_local_path_to_pretrained_models> нужно заменить на полный путь к этому каталогу)
```
$ docker run -d -p 8180:8180 -p 8181:8181 -v <your_local_path_to_pretrained_models>:/app/app/models GB_docker_flask
```
N.B. При создании модели нужно использовать версии библиотек, указанные в requirements.txt.

### Переходим на localhost:8181
