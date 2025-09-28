'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
from collections import defaultdict

class ProjectManagementTool:
    def __init__(self):
        self.projects = {}
        self.tasks = {}
        self.team_members = {}
        self.project_tasks = defaultdict(list)
        self.task_assignments = {}

    # CRUD for Projects
    def create_project(self, project_id, name):
        self.projects[project_id] = {'name': name}
        print(f"Project '{name}' created.")

    def read_project(self, project_id):
        return self.projects.get(project_id, "Not found.")

    def update_project(self, project_id, new_data):
        if project_id in self.projects:
            self.projects[project_id].update(new_data)
            print("Project updated.")

    def delete_project(self, project_id):
        if project_id in self.projects:
            del self.projects[project_id]
            print("Project deleted.")

    # CRUD for Tasks
    def create_task(self, task_id, project_id, desc):
        self.tasks[task_id] = {'desc': desc, 'project_id': project_id}
        self.project_tasks[project_id].append(task_id)
        print(f"Task '{desc}' created.")

    def read_task(self, task_id):
        return self.tasks.get(task_id, "Not found.")

    # Assign task
    def assign_task(self, task_id, team_member_id):
        if task_id in self.tasks:
            self.task_assignments[task_id] = team_member_id
            print(f"Task {task_id} assigned to member {team_member_id}.")

    # Visualize project timeline
    def generate_project_timeline(self, project_id):
        print(f"Timeline for project '{self.projects[project_id]['name']}':")
        for tid in self.project_tasks[project_id]:
            status = "Assigned" if tid in self.task_assignments else "Unassigned"
            print(f"  Task {tid}: {self.tasks[tid]['desc']} - {status}")

# Example usage:
pm = ProjectManagementTool()
pm.create_project(1, "Website Redesign")
pm.create_task(101, 1, "Design Homepage")
pm.create_task(102, 1, "Develop Backend")
pm.assign_task(101, "Alice")
pm.generate_project_timeline(1)
