from collections import Counter
import requests
from dotenv import load_dotenv
import os
import time
import csv
from datetime import datetime

# load keys from .env
load_dotenv()

# get recent stargazers of repo
def get_stargazers(repo_name, user_limit, headers):
    url = f"https://api.github.com/repos/{repo_name}/stargazers"
    params = {'per_page': user_limit}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    stargazers = response.json()
    return [user['login'] for user in stargazers]

# get all starred repos of a user
def get_starred_repos(user, headers):
    time.sleep(0.1)
    url = f"https://api.github.com/users/{user}/starred"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    starred_repos = response.json()
    return [(repo['full_name'], repo['stargazers_count'], repo['description'], repo['html_url']) for repo in starred_repos]

# MAIN
def main(repo_name, user_limit=30):
    try:
        headers = {'Accept': 'application/vnd.github.v3+json'}
        api_key = os.getenv('GITHUB_API_KEY')
        if api_key:
            headers['Authorization'] = f'token {api_key}'
        
        stargazers = get_stargazers(repo_name, user_limit, headers)
        all_starred_repos = []
        repo_user_count = Counter()
        
        for user in stargazers:
            user_starred_repos = get_starred_repos(user, headers)
            all_starred_repos.extend(user_starred_repos)
            for repo in user_starred_repos:
                repo_user_count[repo[0]] += 1
        
        repo_counts = Counter([repo[0] for repo in all_starred_repos])
        sorted_repos = sorted(repo_counts.items(), key=lambda x: x[1], reverse=True)
        
        repo_details = {}
        for repo in all_starred_repos:
            if repo[0] not in repo_details:
                repo_details[repo[0]] = {'stars': repo[1], 'description': repo[2], 'link': repo[3]}
        
        # prep data for csv
        csv_data = []
        for repo, count in sorted_repos:
            csv_data.append([repo, repo_user_count[repo], repo_details[repo]['stars'], repo_details[repo]['description'], repo_details[repo]['link']])
        
        # Save to csv
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        safe_repo_name = repo_name.replace("/", "_")
        filename = f"{timestamp}_similar_to_{safe_repo_name}.csv"
        
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["repo", "user_count", "stars", "description", "link"])
            writer.writerows(csv_data)
        
        print(f"Data saved to {filename}")
        return csv_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    repo_name = input("Enter repo name (e.g., DePayFi/widgets): ")
    user_limit = input("Number of users to fetch (default=30): ")
    user_limit = int(user_limit) if user_limit else 30
    
    ranked_repos = main(repo_name, user_limit)
    if ranked_repos:
        for repo in ranked_repos:
            print(f"https://github.com/{repo[0]} : {repo[1]} users, {repo[2]} stars")
