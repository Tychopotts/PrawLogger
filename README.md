# PrawModQueueLogger

A simple Python script to log and export the modqueue of a subreddit as a JSON blob using [PRAW](https://praw.readthedocs.io/) (Python Reddit API Wrapper).

## Features

- Logs in to Reddit using credentials from a YAML config file
- Fetches up to 10 items from the specified subreddit's modqueue
- Outputs the modqueue items as a formatted JSON blob

## Setup

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/RedditPythonPractice.git
cd RedditPythonPractice
```

### 2. Create and activate a virtual environment (optional but recommended)

```sh
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```sh
pip install praw pyyaml
```

### 4. Configure your credentials

- Copy `config_template.yaml` to `config.yaml`:

  ```sh
  copy config_template.yaml config.yaml
  ```

- Edit `config.yaml` and fill in your Reddit API credentials and subreddit name.

  ```yaml
  client_id: your_client_id
  client_secret: your_client_secret
  user_agent: your_user_agent
  username: your_reddit_username
  password: your_reddit_password
  subreddit: adhd
  ```

**Note:**  
Do **not** commit your `config.yaml` with real credentials to version control.

### 5. Run the script

```sh
python PrawModQueueLogger.py
```

## Output

- The script prints your Reddit username and a JSON blob of up to 10 items from the modqueue of the specified subreddit.

## Troubleshooting

- **401 Unauthorized:** Double-check your credentials and ensure your Reddit app is registered as a "script".
- **KeyError:** Make sure your YAML keys match those used in the script (`username`, `password`, etc.).