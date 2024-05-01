FROM python:3.12-alpine
LABEL maintainer="m.meylan@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 9090
ENTRYPOINT ["python"]
CMD ["src/app.py"]
