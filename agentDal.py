import mysql.connector
from agent import Agent

class AgentDAL:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="eagleEyeDB"
        )
        self.cursor = self.conn.cursor(dictionary=True)
    def create_agent(self, agent: Agent):
        query = """
        INSERT INTO agents (codeName, realName, location, status, missionsCompleted)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (agent.code_name, agent.real_name,
                                    agent.location, agent.status, agent.missions_completed))
        self.conn.commit()

    def get_all_agents(self):
        self.cursor.execute("SELECT * FROM agents")
        results = self.cursor.fetchall()

        return [Agent(row['codeName'], row['realName'], row['location'],
                      row['status'], row['missionsCompleted']) for row in results]

    def update_agent(self, agent_id, updated_agent: Agent):
        query = """
        UPDATE agents SET codeName=%s, realName=%s, location=%s,
        status=%s, missionsCompleted=%s WHERE id=%s
        """
        self.cursor.execute(query, (updated_agent.code_name, updated_agent.real_name,
                                    updated_agent.location, updated_agent.status,
                                    updated_agent.missions_completed, agent_id))
        self.conn.commit()

    def delete_agent(self, agent_id):
        self.cursor.execute("DELETE FROM agents WHERE id=%s", (agent_id,))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

