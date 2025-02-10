# FastAPI-employee-knowledge-control
Service for employee knowledge control  
This service will be useful for companies that need to control the knowledge of their employees, test results are recorded in a database, after which the analysis of the received data can be performed and some actions taken against employees.


1. Clone repository:
   ```bash
   git clone <repository_url>
   cd FastAPI-employee-knowledge-control
    ```
   
2. Run dockerfile
```commandline
docker build -t my-fastapi-app .
docker run -d -p 8000:8000 --name fastapi_container my-fastapi-app
```

3. For running tests
```commandline
docker exec -it fastapi_container pytest tests/
```
