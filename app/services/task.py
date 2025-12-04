

from typing import List, Optional
from app.repositories.task import TaskRepository
from app.models.task import Task
from app.services.base import BaseService
from datetime import datetime
from app.models.project import Project

class TaskService(BaseService):
 
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(self, title: str, description: str, deadline: datetime, project_id: int) -> Optional[Task]:
        
        
        
        if deadline <= datetime.now():
            print("Error: Deadline must be in the future.")
            return None

        return self.repository.create(
            title=title,
            description=description,
            deadline=deadline,
            project_id=project_id,
            status="pending" 
        )

    def get_tasks_by_project(self, project_id: int) -> List[Task]:
        
        return self.repository.get_by_project(project_id)

    def close_task(self, task_id: int) -> Optional[Task]:
        
        task = self.repository.get_by_id(task_id)
        if not task or task.status == "done":
            return None
        
        
        return self.repository.update(task, status="done", closed_at=datetime.now())
    
    def get_overdue_tasks(self) -> List[Task]:
    
        return self.repository.get_overdue_and_open_tasks()