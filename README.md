# ghost-proxy
Demo project for fetching posts from a Ghost blog instance and returning minimal response with caching

# Setup
Refer to the `.env.example` file for setting configuration such as listening server host and port.

# Requirements
* Python >= 3.5.3

# Install
* Install and with pipenv
  ```
  pipenv install
  pipenv run python app.py
  ```

# Usage
* Browse `http://{host}:{port}/posts` to fetch and cache posts.
