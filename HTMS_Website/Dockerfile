FROM python:3.11.2-slim

ENV PYTHONUNBUFFERED 1


WORKDIR /htms_website

COPY ./ ./



RUN apt-get update \
    && apt upgrade \
    && apt  -  -y install libpq-dev gcc \
    && pip install psycopg2 \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --upgrade pip  \
    && chmod -R 777 *

# RUN apt-get update \
#     && apt-get install -y libpq-dev \
#     && pip install psycopg2



EXPOSE 8004

CMD ["gunicorn", "--workers", "3", "--timeout", "86400", "--bind", "0.0.0.0:8004", "HTMS_Website.wsgi:application"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000" ]






# RUN apt-get update && apt-get install -y curl
# RUN curl -sL https://deb.nodesource.com/setup_19.x | bash -
# RUN apt-get install -y nodejs