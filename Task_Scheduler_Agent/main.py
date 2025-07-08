from task_agent import TaskAgent

def load_tasks(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()

def main():
    agent = TaskAgent()
    tasks = load_tasks("tasks.txt")
    print("🧠 Categorizing tasks using Gemini...\n")
    result = agent.summarize_tasks(tasks)
    print(result)

if __name__ == "__main__":
    main()
