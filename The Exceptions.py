import datetime
print("Welcome To Stakeholder Communication Platform!")
print("-------------------------------------------------------------------------")
class User:
    def __init__(self, user_id, username, password, email, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.role = role
    def change_password(self, new_password):
        self.password = new_password
    def __repr__(self):
        return f"User(ID: {self.user_id}, Username: {self.username}, Email: {self.email}, Role: {self.role})"
class UserManager:
    def __init__(self):
        self.users = {}
    def create_user(self, user_id, username, password, email, role):
        if user_id in self.users:
            print("User ID already exists!")
        else:
            self.users[user_id] = User(user_id, username, password, email, role)
            print(f"User {username} created successfully!")
    def read_user(self, user_id):
        user = self.users.get(user_id)
        if user:
            print(user)
        else:
            print("User not found!")
    def update_user(self, user_id, username=None, password=None, email=None, role=None):
        user = self.users.get(user_id)
        if user:
            if username:
                user.username = username
            if password:
                user.change_password(password)
            if email:
                user.email = email
            if role:
                user.role = role
            print(f"User {user_id} updated successfully!")
        else:
            print("User not found!")
    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            print(f"User {user_id} deleted successfully!")
        else:
            print("User not found!")
class CommunicationLog:
    def __init__(self):
        self.logs = {}
    def create_log(self, log_id, stakeholder_id, communication_type, date):
        if log_id in self.logs:
            print("Log ID already exists!")
        else:
            self.logs[log_id] = {
                'stakeholder_id': stakeholder_id,
                'communication_type': communication_type,
                'date': date,
            }
            print(f"Communication log {log_id} created successfully!")
    def read_log(self, log_id):
        log = self.logs.get(log_id)
        if log:
            print(f"Log: Log ID: {log_id}, Communication Type: {log['communication_type']}, Date: {log['date']}")
        else:
            print("Log not found!")
    def update_log(self, log_id, communication_type=None, date=None):
        log = self.logs.get(log_id)
        if log:
            if communication_type:
                log['communication_type'] = communication_type
            if date:
                log['date'] = date
            print(f"Log {log_id} updated successfully!")
        else:
            print("Log not found!")
    def delete_log(self, log_id):
        if log_id in self.logs:
            del self.logs[log_id]
            print(f"Log {log_id} deleted successfully!")
        else:
            print("Log not found!")
class Stakeholder:
    def __init__(self, stakeholder_id, name, email):
        self.stakeholder_id = stakeholder_id
        self.name = name
        self.email = email
        self.feedback = []
class Feedback:
    def __init__(self, feedback_id, stakeholder_id, date, feedback_message):
        self.feedback_id = feedback_id
        self.stakeholder_id = stakeholder_id
        self.date = date
        self.feedback_message = feedback_message
class Task:
    def __init__(self, name, schedule, status, purpose):
        self.name = name
        self.schedule = schedule
        self.status = status
        self.purpose = purpose

    def __str__(self):
        return f"Task: {self.name}\nSchedule: {self.schedule}\nStatus: {self.status}\nPurpose: {self.purpose}"
class ScheduleManager:
    def __init__(self):
        self.tasks = []
    def add_task(self):
        name = input("Enter task name: ")
        schedule = input("Enter task schedule (YYYY-MM-DD): ")
        status = input("Enter task status: ")
        purpose = input("Enter task purpose: ")
        new_task = Task(name, schedule, status, purpose)
        self.tasks.append(new_task)
        print("Task added successfully!\n")
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.\n")
            return
        for i, task in enumerate(self.tasks):
            print(f"Task {i + 1}:\n{task}\n")
    def update_task(self):
        self.view_tasks()
        if not self.tasks:
            return
        try:
            task_index = int(input("Enter the task number to update: ")) - 1
            if 0 <= task_index < len(self.tasks):
                schedule = input("Enter new schedule (leave blank to keep current): ")
                status = input("Enter new status (leave blank to keep current): ")
                purpose = input("Enter new purpose (leave blank to keep current): ")

                if schedule:
                    self.tasks[task_index].schedule = schedule
                if status:
                    self.tasks[task_index].status = status
                if purpose:
                    self.tasks[task_index].purpose = purpose

                print("Task updated successfully!\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")
class StakeholderCommunicationPlatform:
    def __init__(self):
        self.logs = CommunicationLog()
        self.feedback_list = []
        self.stakeholders = {}
    def add_feedback(self, stakeholder_id, feedback_message):
        feedback_id = len(self.feedback_list) + 1
        date = datetime.date.today().isoformat()
        feedback = Feedback(feedback_id, stakeholder_id, date, feedback_message)
        self.feedback_list.append(feedback)
        print("Feedback added successfully!")
    def read_feedback(self, stakeholder_id):
        for feedback in self.feedback_list:
            if feedback.stakeholder_id == stakeholder_id:
                print(f"Feedback ID: {feedback.feedback_id}, Date: {feedback.date}, Message: {feedback.feedback_message}")
        print("End of feedback.")
    def analyze_communication_effectiveness(self, stakeholder_id):
        total_logs = 0
        communication_types = {}
        for log in self.logs.logs.values():
            if log['stakeholder_id'] == stakeholder_id:
                total_logs += 1
                communication_type = log['communication_type']
                communication_types[communication_type] = communication_types.get(communication_type, 0) + 1       
        if total_logs == 0:
            print(f"No communication logs found for Stakeholder ID: {stakeholder_id}.")
            return
        print(f"Communication Analysis for Stakeholder ID: {stakeholder_id}")
        print(f"Total Communications: {total_logs}")
        for comm_type, count in communication_types.items():
            print(f"{comm_type.capitalize()}: {count} ({(count / total_logs) * 100:.2f}%)")
def main_menu():
    platform = StakeholderCommunicationPlatform()
    user_manager = UserManager()
    schedule_manager = ScheduleManager()
    while True:
        print("\nWelcome To Stakeholder Communication Platform!")
        print("1. Stakeholder Details")
        print("2. Communication Log")
        print("3. Feedback")
        print("4. Schedule")
        print("5. Communication Analysis")
        print("6. Exit")
        choice = input("Select an option (1-6): ")
        if choice == '1':
            while True:
                print("\nOptions:")
                print("1. Create User")
                print("2. Read User")
                print("3. Update User")
                print("4. Delete User")
                print("5. Change Password")
                print("6. Exit")
                choice = input("Select an option (1-6): ")
                if choice == '1':
                    user_id = input("Enter User ID: ")
                    username = input("Enter Username: ")
                    password = input("Enter Password: ")
                    email = input("Enter Email: ")
                    role = input("Enter Role: ")
                    user_manager.create_user(user_id, username, password, email, role)
                elif choice == '2':
                    user_id = input("Enter User ID to read: ")
                    user_manager.read_user(user_id)
                elif choice == '3':
                    user_id = input("Enter User ID to update: ")
                    username = input("Enter new Username : ")
                    password = input("Enter new Password : ")
                    email = input("Enter new Email : ")
                    role = input("Enter new Role (leave blank to skip): ")
                    user_manager.update_user(user_id, username or None, password or None, email or None, role or None)
                elif choice == '4':
                    user_id = input("Enter User ID to delete: ")
                    user_manager.delete_user(user_id)
                elif choice == '5':
                    user_id = input("Enter User ID to change password: ")
                    new_password = input("Enter new Password: ")
                    user_manager.update_user(user_id, password=new_password)
                elif choice == '6':
                    break
                else:
                    print("Invalid option. Please try again.")
        elif choice == '2':
            while True:
                print("\nCommunication Log Options:")
                print("1. Create Log")
                print("2. Read Log")
                print("3. Update Log")
                print("4. Delete Log")
                print("5. Exit")
                log_choice = input("Select an option: ")
                if log_choice == '1':
                    log_id = input("Enter Log ID: ")
                    stakeholder_id = input("Enter Stakeholder ID: ")
                    communication_type = input("Enter Communication type (email/phone/text): ")
                    date = input("Enter Date of communication (YYYY-MM-DD): ")
                    platform.logs.create_log(log_id, stakeholder_id, communication_type, date)
                elif log_choice == '2':
                    log_id = input("Enter Log ID to read: ")
                    platform.logs.read_log(log_id)
                elif log_choice == '3':
                    log_id = input("Enter Log ID: ")
                    communication_type = input("Enter new Communication type (leave blank to skip): ")
                    date = input("Enter new Date (leave blank to skip): ")
                    platform.logs.update_log(log_id, communication_type or None, date or None)
                elif log_choice == '4':
                    log_id = input("Enter Log ID to delete: ")
                    platform.logs.delete_log(log_id)
                elif log_choice == '5':
                    break
                else:
                    print("Invalid option. Please try again.")
        elif choice == '3':
            while True:
                print("\nFeedback Options:")
                print("1. Add Feedback")
                print("2. Read Feedback")
                print("3. Exit")
                feedback_choice = input("Select an option: ")
                if feedback_choice == '1':
                    stakeholder_id = input("Enter Stakeholder ID: ")
                    feedback_message = input("Enter Feedback Message: ")
                    platform.add_feedback(stakeholder_id, feedback_message)
                elif feedback_choice == '2':
                    stakeholder_id = input("Enter Stakeholder ID to read feedback: ")
                    platform.read_feedback(stakeholder_id)
                elif feedback_choice == '3':
                    break
                else:
                    print("Invalid option. Please try again.")
        elif choice == '4':
            while True:
                print("\nSchedule Options:")
                print("1. Add Task")
                print("2. View Tasks")
                print("3. Update Task")
                print("4. Exit")
                schedule_choice = input("Select an option: ")
                if schedule_choice == '1':
                    schedule_manager.add_task()
                elif schedule_choice == '2':
                    schedule_manager.view_tasks()
                elif schedule_choice == '3':
                    schedule_manager.update_task()
                elif schedule_choice == '4':
                    break
                else:
                    print("Invalid option. Please try again.")
        elif choice == '5':
            stakeholder_id = input("Enter Stakeholder ID to analyze: ")
            platform.analyze_communication_effectiveness(stakeholder_id)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")
main_menu()
print("Thank you!")
print("Visit Again!")
