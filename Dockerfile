# Use Python image for automation setup.
# Install project dependencies inside container.
# Run automation tests automatically.

FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["pytest", "-n", "1"]