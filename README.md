# 🗑️ Vercel Project Deleter

This Python script allows you to fetch and delete projects from your Vercel account with ease! 🌐✨

## 🚀 Features

- **Fetch Projects**: Retrieve all projects associated with your Vercel account.
- **Delete Projects**: Prompt for confirmation before deleting each project to prevent accidental deletions. ❌

## 🔧 Prerequisites

- Python 3.x
- `requests` library

Install the required library using:

```bash
pip install requests
```

🛠️ Usage

1. Clone the Repository or download the script.


2. Set Your Vercel Token: Replace the token in the script with your Vercel API token:
```
VERCEL_TOKEN = 'YOUR_VERCEL_TOKEN'
```


3. Run the Script:
```
python3 delete_vercel_projects.py
```

4. Follow the Prompts: The script will display all your projects. Confirm each deletion by typing y or skip by typing n.


📜 Example Output
```markdown
Are you sure you want to delete project "My Awesome Project" with ID "12345"? (y/n):
```
⚠️ Warning

Be cautious! This script will permanently delete your projects from Vercel. Use it responsibly! ⚡

💻 License

This project is licensed under the MIT License. See the LICENSE file for more details.

