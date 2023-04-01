FROM python:3.10-slim

# set the working directory
WORKDIR /work2

# install dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install psycopg2-binary
RUN pip install python-multipart


# copy the src to the folder
COPY . ./

EXPOSE 8000

# start the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


