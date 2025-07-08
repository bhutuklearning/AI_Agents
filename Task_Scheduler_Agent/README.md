# Task Scheduler Agent

## Overview

The **Task Scheduler Agent** is an intelligent tool designed to categorize and prioritize your tasks using Google Gemini's generative AI capabilities. By leveraging state-of-the-art language models, this agent helps you organize your to-do list into high, medium, and low priority buckets, making task management smarter and more efficient.

## Features

- Categorizes tasks into priority levels using AI
- Simple command-line interface
- Easily extensible for more advanced task management

## Setup Instructions

Follow these steps to set up and run the Task Scheduler Agent:

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Upgrade pip (recommended)

```bash
python -m pip install --upgrade pip
```

### 4. Install Dependencies

Install the required packages:

```bash
pip install google-generativeai
pip install python-dotenv
```

Or install all dependencies at once:

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Create a `.env` file in this directory and add your Google API key:

```
GOOGLE_API_KEY=your_google_api_key_here
```

## Usage

1. Add your tasks (one per line) to the `tasks.txt` file in this directory.
2. Run the agent:
   ```bash
   python main.py
   ```
3. The agent will categorize your tasks and display them by priority.

## Updating requirements.txt

If you add or update dependencies, refresh `requirements.txt` with:

```bash
python -m pip freeze > requirements.txt
```

## Technologies Used

- **Python**
- **Google Gemini (Generative AI)**
- **python-dotenv** for environment variable management

---

This project is a work in progress and open to improvements. Feel free to experiment and extend its capabilities!
