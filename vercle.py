# Copyright: Vishal-1756

import requests

VERCEL_TOKEN = 'your vercle token' # from vercle account/settings/tokens

def fetch_projects():
    url = 'https://api.vercel.com/v9/projects'
    headers = {
        'Authorization': f'Bearer {VERCEL_TOKEN}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['projects']
    else:
        print(f'Error fetching projects: {response.status_code} - {response.text}')
        return []

def delete_project(project_id):
    url = f'https://api.vercel.com/v9/projects/{project_id}'
    headers = {
        'Authorization': f'Bearer {VERCEL_TOKEN}'
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f'Project {project_id} deleted successfully.')
    else:
        print(f'Error deleting project {project_id}: {response.status_code} - {response.text}')

def main():
    projects = fetch_projects()
    if not projects:
        print("No projects found.")
        return
    for project in projects:
        project_id = project['id']
        project_name = project['name']
        confirmation = input(f'Are you sure you want to delete project "{project_name}" with ID "{project_id}"? (y/n): ')
        if confirmation.lower() == 'y':
            delete_project(project_id)
        else:
            print(f'Skipping project "{project_name}".')

if __name__ == '__main__':
    main()
