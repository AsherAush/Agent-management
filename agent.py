class Agent:
    def __init__(self, code_name, real_name, location, status, missions_completed):
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status
        self.missions_completed = missions_completed

    def __str__(self):
        return  f"code name {self.code_name}, real name {self.real_name}, Location: {self.location}, Status: {self.status}, Missions Completed: {self.missions_completed}"

