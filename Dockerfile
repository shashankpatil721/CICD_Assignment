FROM node:18-alpine


WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN python train.py


CMD ["python", "test.py"]
