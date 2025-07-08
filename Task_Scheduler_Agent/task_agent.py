import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class TaskAgent:
    def __init__(self):
        # Using the correct working model
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def summarize_tasks(self, tasks_list: str) -> str:
        prompt = f"""You are a smart task planning agent.
Given a list of tasks, categorize them into 3 priority buckets:
– High Priority
– Medium Priority
– Low Priority

Tasks:
{tasks_list}

Return the response in this format:
High Priority:
– task 1
– task 2

Medium Priority:
– task 1
– task 2

Low Priority:
– task 1
– task 2
"""
        response = self.model.generate_content(prompt)
        return response.text
