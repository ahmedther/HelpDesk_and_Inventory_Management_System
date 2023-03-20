

upstream app_server {
        server app:9004;
    }

server {
    listen ${LISTEN_PORT};
    access_log /var/log/nginx/htms.log;
    error_log /var/log/nginx/htms_log_error.log;
    location /static {
        root /htms_website;
    }

    location / {
        proxy_read_timeout 86400s;
        proxy_connect_timeout 86400s;
        proxy_send_timeout 86400s; 
        uwsgi_pass app_server;
        include /etc/nginx/uwsgi_params;

    }

    location = /favicon.ico { access_log off; log_not_found off; }

   
}
