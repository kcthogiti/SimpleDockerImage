FROM python:2.7.12

RUN pip install numpy==1.10.4 scikit-learn==0.17.1 scipy==0.17.0 numpy==1.10.4 flask pandas==0.18.0 

MAINTAINER krishna (kc.thogiti@gmail.com)
WORKDIR /home/model

COPY . /home/model

EXPOSE 5000

CMD ["python", "app.py"]