FROM python:3.9-slim

RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*

#RUN pip3 install --verbose -U sentence-transformers

# Set the working directory
#WORKDIR /src

# Install Python dependencies.
#ADD requirements.txt /
#RUN pip3 install --upgrade pip
#RUN pip3 install -r requirements.txt

COPY requirements.txt /requirements.txt
COPY entrypoint.sh /entrypoint.sh


CMD ["sh", "entrypoint.sh"]

# Command to run on container start
#CMD ["tail", "-f", "/dev/null"]
#CMD ["gunicorn", "-w", "4", "--chdir", "/src", "'service:app'"]
