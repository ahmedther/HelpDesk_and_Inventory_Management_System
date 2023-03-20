FROM python:3.11.2-slim

LABEL maintainer='ahmed'

ENV PYTHONUNBUFFERED 1

WORKDIR /htms_website

COPY ./ ./


RUN apt update -y \
    && apt upgrade -y \
    && apt install libpq-dev gcc -y\
    && python3 -m venv /py \
    && /py/bin/pip install --upgrade pip \
    && /py/bin/pip install --no-cache --no-cache-dir -r ./requirements.txt  \
    && chmod -R 777 /htms_website/ \
    && mkdir /var/log/uwsgi \
    && touch /var/log/uwsgi/HTMS_Website.log  \
    && apt autoremove -y 
    

ENV PATH="./scripts:/py/bin:$PATH"




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