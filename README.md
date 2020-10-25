
## Corona Charts Essen

### create the corona chart image manually.

    docker build -t coronacharts:latest .

### Run Corona-Charts docker container

    docker run --rm --name corona -p 8080:8080 coronacharts:latest

Start a web browser and open the website [Start a web browser and open the website [http://localhost:8080/](http://localhost:8080/)

### Run docker-compose

If an update has been made in the code or a template, the image must be recreated.

    docker-compose up -d --build

Or simply with an existing Docker image

    docker-compose up -d

### fetch data from dm api 

    docker-compose up -d fetch 

### Corona Chatts behind nginx

Example nginx configuration:

    upstream corona {
        server <internalIP>:8080;
    }
    server {
      listen 443 ssl http2;
      server_name corona.example.com;
      index index.html;
      access_log /srv/customer/corona.example.com/statistics/logs/ssl-access.log;
      error_log /srv/customer/corona.example.com/statistics/logs/ssl-error.log;
      ssl_certificate     /srv/customer/corona.example.com/conf/fullchain.cer;
      ssl_certificate_key /srv/customer/corona.example.com/conf/example.com.key;
      ssl_trusted_certificate /srv/customer/corona.example.com/conf/trusted.pem;
      ssl_protocols TLSv1.2;
      ssl_ciphers 'ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256';
      ssl_prefer_server_ciphers on;
      ssl_session_cache shared:SSL:10m;
      ssl_session_timeout 10m;
      ssl_stapling on;
      ssl_stapling_verify on;
      ssl_dhparam /srv/customer/corona.example.com/conf/dhparam.pem;
      resolver 9.9.9.9 1.1.1.1 valid=300s;
      resolver_timeout 10s;
      location / {
        proxy_pass http://corona;
        proxy_set_header Host            $host;
        proxy_set_header X-Forwarded-For $remote_addr;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_redirect off;
        proxy_set_header X-Forwarded-Proto https;
      }
      error_page 404 /404.html;
      error_page 500 /500.html;
      error_page 502 503 504 /502.html;
    }
