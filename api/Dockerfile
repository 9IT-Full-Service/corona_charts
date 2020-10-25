# FROM nginx:alpine
# COPY . /usr/share/nginx/html/

FROM cms-core:1.1
RUN pip install pymongo
COPY . /app
WORKDIR /app
# ENTRYPOINT ["python3"]
CMD ["/usr/local/bin/python","-u","app.py"]
