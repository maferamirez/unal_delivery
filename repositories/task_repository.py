from models.task import Task, db

class TaskRepository:

    @staticmethod
    def create_task(name, description):
        task = Task(name=name, description=description)
        db.session.add(task)
        db.session.commit()
        return task
    
    @staticmethod
    def update_task(task_id, name, description):
        task = Task.query.get(task_id)
        if task:
            task.name = name
            task.description = description
            db.session.commit()
        return task