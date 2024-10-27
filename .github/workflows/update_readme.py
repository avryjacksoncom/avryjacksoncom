import requests
import os

# Replace 'your-leetcode-username' with your actual LeetCode username
LEETCODE_USERNAME = 'https://leetcode.com/u/avryjacksoncom/'

def fetch_leetcode_stats(username):
    url = f'https://leetcode-stats-api.herokuapp.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from LeetCode API")
        return None

def update_readme(stats):
    with open("README.md", "r") as file:
        readme_content = file.readlines()

    # Assuming you have placeholders in README.md for each level
    easy_count = stats.get('easySolved', 0)
    medium_count = stats.get('mediumSolved', 0)
    hard_count = stats.get('hardSolved', 0)
    total_count = stats.get('totalSolved', 0)

    # Update the placeholder with fetched stats
    new_content = []
    for line in readme_content:
        if "![easy-badge]" in line:
            line = f"![easy-badge](https://img.shields.io/badge/Easy-{easy_count}-green)\n"
        elif "![medium-badge]" in line:
            line = f"![medium-badge](https://img.shields.io/badge/Medium-{medium_count}-yellow)\n"
        elif "![hard-badge]" in line:
            line = f"![hard-badge](https://img.shields.io/badge/Hard-{hard_count}-red)\n"
        elif "![total-badge]" in line:
            line = f"![total-badge](https://img.shields.io/badge/Total-{total_count}-blue)\n"
        new_content.append(line)

    with open("README.md", "w") as file:
        file.writelines(new_content)

if __name__ == "__main__":
    stats = fetch_leetcode_stats(LEETCODE_USERNAME)
    if stats:
        update_readme(stats)
