from agent import Agent
from agentDal import AgentDAL


def print_menu():
    print("\n===== Eagle Eye: Agent Management =====")
    print("1. Add Agent")
    print("2. View All Agents")
    print("3. Update Agent")
    print("4. Delete Agent")
    print("5. Exit")
    print("=======================================")

def get_agent_input():
    code_name = input("Code Name: ")
    real_name = input("Real Name: ")
    location = input("Current Location: ")
    status = input("Status (Active/Injured/Missing/Retired): ")
    missions_completed = int(input("Number of Missions Completed: "))
    return Agent(code_name, real_name, location, status, missions_completed)

def main():
    dal = AgentDAL()

    while True:
        print_menu()
        choice = input("Select an option: ")

        if choice == "1":
            print("\n--- Add New Agent ---")
            agent = get_agent_input()
            dal.create_agent(agent)
            print("Agent added successfully.")

        elif choice == "2":
            print("\n--- Agent List ---")
            agents = dal.get_all_agents()
            if agents:
                for agent in agents:
                    print(agent)
            else:
                print("No agents found.")

        elif choice == "3":
            print("\n--- Update Agent ---")
            agent_id = int(input("Enter Agent ID to update: "))
            updated_agent = get_agent_input()
            dal.update_agent(agent_id, updated_agent)
            print("Agent updated successfully.")

        elif choice == "4":
            print("\n--- Delete Agent ---")
            agent_id = int(input("Enter Agent ID to delete: "))
            dal.delete_agent(agent_id)
            print("Agent deleted.")

        elif choice == "5":
            print("Exiting system...")
            dal.close()
            break

        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
