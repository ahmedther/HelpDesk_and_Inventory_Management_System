FROM python:3.11.2-slim

LABEL maintainer='ahmed'

ENV PYTHONUNBUFFERED 1

WORKDIR /htms_website

COPY ./ ./


RUN apt update -y --no-install-recommends \
    && apt upgrade -y --no-install-recommends \
    && apt install libpq-dev gcc curl unzip libaio1 -y \ 
    && python3 -m venv /py \
    && /py/bin/pip install --upgrade pip \
    && /py/bin/pip install --no-cache --no-cache-dir -r ./requirements.txt  \
    && chmod -R 777 /htms_website/ \
    && mkdir /var/log/uwsgi \
    && touch /var/log/uwsgi/HTMS_Website.log  \ 
    && mkdir -p /cx_oracle \
    && cd /cx_oracle \
    && curl -o instantclient-basiclite-linux.x64-21.9.0.0.0dbru.zip https://download.oracle.com/otn_software/linux/instantclient/219000/instantclient-basiclite-linux.x64-21.9.0.0.0dbru.zip \
    && unzip -d . instantclient-basiclite-linux.x64-21.9.0.0.0dbru.zip \
    && rm -f instantclient-basiclite-linux.x64-21.9.0.0.0dbru.zip \
    && echo /cx_oracle/instantclient_21_9 > /etc/ld.so.conf.d/oracle-instantclient.conf \
    && ldconfig \
    && apt-get purge -y \
        curl \
        unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && apt autoremove -y  




ENV LD_LIBRARY_PATH=/cx_oracle/instantclient_21_9

ENV PATH="/htms_website/scripts:/py/bin:$PATH"




EXPOSE 8004

CMD ["./scripts/py_run.sh"]


# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000" ]CMD ["gunicorn", "--workers", "3", "--timeout", "86400", "--bind", "0.0.0.0:8004", "HTMS_Website.wsgi:application"]

# misic && apk add libpq gcc musl-dev postgresql-dev \ apk add build-base musl-dev libgcc libc-dev g++ make autoconf automake libtool \
# && /py/bin/pip install --no-cache-dir --no-binary :all: numpy \
# && /py/bin/pip install --no-cache-dir --no-binary :all: uwsgi \


# RUN apt-get update \
#     && apt-get install -y libpq-dev \
#     && pip install psycopg2
# apk update && apk upgrade && apk add --no-cache \
#     build-base \
#     musl-dev \
#     libgcc \
#     libc-dev \
#     g++ \
#     make \
#     autoconf \
#     automake \
#     libtool \
#     libpq \
#     py3-wheel \
#     cython \
#     uwsgi \
#     uwsgi-python3 \
#     && rm -rf /var/cache/apk/* \




# RUN apt-get update && apt-get install -y curl
# RUN curl -sL https://deb.nodesource.com/setup_19.x | bash -
# RUN apt-get install -y nodejs