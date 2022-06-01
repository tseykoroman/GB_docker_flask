FROM python:3.7-slim
LABEL maintainer="tseyko.roman@mail.ru"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip show scikit-learn
RUN pip show dill
EXPOSE 8180
EXPOSE 8181
VOLUME /app/app/models
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]