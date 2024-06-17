# Find Related Repos (Stargazer Analyzer)

Handy, simple tool for the discovery of repositories related to given Github repo. 
Helps answering the question "Are there repos that I am missing out on"?
"Find Related Repos" analyzes the most recent stargazers of a given GitHub repository and provides a ranked list of repositories similar to it based on user interest.
Using a GitHub API key is optional but you won't get far with unauthenticated requests, so using an API key is recommended.

## Features

- Fetch the most recent stargazers of a GitHub repository.
- Retrieve all starred repositories for each stargazer.
- Generate a ranked list of similar repositories.
- Save the results to a CSV file.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/stargazer-analyzer.git
    cd stargazer-analyzer
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file with your GitHub API key:
    ```sh
    GITHUB_API_KEY=your_github_api_key
    ```
## Installation 

Install before running:

```sh
pip install python-dotenv requests
```

## Usage

Run the script and follow the prompts:
```sh
python find_related_repos.py
```

You will be asked to input the repository name (e.g., DePayFi/widgets) and the number of users to fetch. The user default is 30.

