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


3. # 💾 Database Migrations (Alembic)

### 📦 Generate a new migration
```bash
docker-compose exec app alembic revision --autogenerate -m "your message"
```

4. Apply the latest migration
```bash
docker-compose exec app alembic upgrade head
```

5. For running tests
```commandline
docker-compose exec app pytest tests/
```