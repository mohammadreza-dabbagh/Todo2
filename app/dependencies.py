
from app.db.session import SessionLocal
from app.repositories.project import ProjectRepository
from app.repositories.task import TaskRepository
from app.services.project import ProjectService
from app.services.task import TaskService

def get_project_service(db: SessionLocal) -> ProjectService:
 
    repo = ProjectRepository(db=db)
    return ProjectService(repository=repo)

def get_task_service(db: SessionLocal) -> TaskService:
   
    repo = TaskRepository(db=db)
    return TaskService(repository=repo)