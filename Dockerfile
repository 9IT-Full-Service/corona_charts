FROM python:3.8-alpine AS base-image
RUN mkdir /app
COPY requirements.txt /app/
WORKDIR /app
RUN pip3 install --user -r requirements.txt

FROM python:3.8-alpine AS coronacharts
COPY --from=base-image /root/.local /root/.local
COPY . /app/
WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["app.py"]
