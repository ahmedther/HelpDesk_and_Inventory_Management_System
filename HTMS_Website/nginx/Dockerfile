FROM nginx:latest

LABEL maintainer='ahmed'

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./prx_run.sh ./prx_run.sh
COPY ./uwsgi_params /etc/nginx/uwsgi_params

RUN chmod 777 ./prx_run.sh

ENV LISTEN_PORT=8004



CMD ["./prx_run.sh"]
  