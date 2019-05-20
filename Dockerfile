FROM python:3.6
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
ENV IN_DOCKER_CONTAINER Yes
COPY run.py /app
COPY . /app/
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
EXPOSE 9000




