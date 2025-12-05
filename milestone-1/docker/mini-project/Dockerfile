# python slim image as the base image
FROM python:3.10-slim

# set the working directory in the container
WORKDIR /app

# copy the app files to the container
COPY /app /app

# install the required packages
RUN pip install -r requirements.txt

# command to run the FastAPI app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]