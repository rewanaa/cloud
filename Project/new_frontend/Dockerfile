FROM python:3.9-slim

WORKDIR .
# Copy requirements file
COPY requirements.txt ./  
# Install dependencies
RUN pip install -r requirements.txt  

# Copy entire project directory
COPY . .  


EXPOSE 5000  
# Run Flask app in detached mode, listening on all interfaces
CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "5000", "--identity_server", "http://identity-server:5000/", "--database", "http://db-service:5000/"]  

