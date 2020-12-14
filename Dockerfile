FROM python:3.7.5-slim
RUN pip install flask python-dotenv
COPY main.py .
COPY .flaskenv .
CMD flask run