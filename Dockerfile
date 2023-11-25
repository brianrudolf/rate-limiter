FROM python:3.12-bookworm
RUN groupadd -r myuser && useradd -r -g myuser myuser

# Install requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy application code
COPY ./app .

USER myuser


