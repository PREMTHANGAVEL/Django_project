from .models import Task

class TaskManager:
    def __init__(self):
        self.tasks = Task.objects.all()

    def add_task(self, title, description, priority, status):
        task = Task(title=title, description=description, priority=priority, status=status)
        task.save()
        return task

    def edit_task(self, task_id, title, description, priority, status):
        task = Task.objects.get(id=task_id)
        task.title = title
        task.description = description
        task.priority = priority
        task.status = status
        task.save()
        return task

    def delete_task(self, task_id):
        task = Task.objects.get(id=task_id)
        task.delete()

    def get_task_by_id(self, task_id):
        return Task.objects.get(id=task_id)

    def view_all_tasks(self):
        tasks= Task.objects.all()
        """for task in tasks:
            print(task.created_at)"""
        return tasks
    def filter_tasks_by_priority(self, priority):
        return Task.objects.filter(priority=priority)

    