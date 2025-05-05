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
docker-compose up -d --build

```

3. For running tests
```commandline
docker exec -it docker exec -it fastapi-employee-knowledge-control-app-1 pytest tests/ pytest tests/
```
