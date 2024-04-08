FROM shashankpatil721/cicd_repo


WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN python train.py


RUN npm install \
    && npm install -g serve \
    && npm run build \
    && rm -fr node_modules


CMD ["python", "test.py"]
