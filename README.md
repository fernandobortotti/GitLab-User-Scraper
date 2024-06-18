# GitLab User Search Script

This Python script that does web scraping in GitLab directories,
the goal is to enumerate users of private projects, this is done by searching for users in a Private GitLab instance using a keyword, it will bring up all users who have that keyword in their username.

## Usage

### Prerequisites

- Python 3.x
- Required Python libraries: `requests`, `beautifulsoup4`

### Running the Script

1. Clone or download the script to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using the following command:

   ```python
   python gitlab_user_search.py -H <GitLab_host> -u <username_keyword>
   ```

   - Replace `<GitLab_host>` with the host of your GitLab instance.
   - Replace `<username_keyword>` with the keyword you want to search for.

## Functionality

The script performs the following tasks:

- Accepts the GitLab host and username keyword as command-line arguments.
- Searches for users matching the provided keyword on the specified GitLab instance.
- Prints details of the found users, including username, full name, and avatar link.

## Example

Suppose you want to search for users with the keyword "john" on a GitLab instance hosted at `gitlab.example.com`. You would run the script as follows:

```python
python3 gitlab_user_search.py -H gitlab.example.com -u john
```
