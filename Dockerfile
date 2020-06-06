FROM python:3.8
RUN mkdir /app
# COPY requirements.txt /app/
COPY . /app/
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
