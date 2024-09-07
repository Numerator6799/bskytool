# BlueSky tool
A tool for [BlueSky](https://bsky.app) tricks.

Features:
- Follow back who follows you
- Follow who liked your posts
- Follow who liked a post
- Like a post thread

## Installation
Install [Python3](https://www.python.org/)
```bash
pip install atproto
```

## Usage

### Credentials
You may pass your credentials in the command line or export them into environment variables, and omit the `-u` and `-p` parameters.

#### Passing credentials in the command line
```bash
python3 bsky.py COMMAND [OPTIONS] -u your_username -p your_password
```

#### Using credentials from environment

```bash
export BSKY_USERNAME=your_username
export BSKY_PASSWORD=your_password
python3 bsky.py COMMAND [OPTIONS]
```

### Caching
Prior to running the other commands, it's good to create a cache of your current follows and followers.
```bash
python3 bsky.py bcache -u your_username -p your_password
```
This will create a `fcache.json` file that will be loaded when you run other commands.

### Suggested script
The [run.sh](https://github.com/Numerator6799/bskytool/blob/main/run.sh) is an example usage that I employ to run the commands in the order that works for me. This is more practical for me as I can schedule it to run every hour. If you like it, feel free to suggest changes to it!

```bash
export BSKY_USERNAME=your_username
export BSKY_PASSWORD=your_password
chmod +x run.sh
./run.sh
```

### Follow back your followers
Follows back everyone that follows you

```bash
python3 bsky.py ffollowers -u your_username -p your_password
```

### Follow who liked a post
Follows everyone who liked a post

```bash
python3 bsky.py fpostlikes -e <post_url> -u your_username -p your_password
```

The `<post_url>` is the url for the post, for instance: https://bsky.app/profile/bsky.app/post/3l327azz5qg24

### Follow who liked all your posts
Follows everyone who liked the posts you created

```bash
python3 bsky.py fallmypostlikes -u your_username -p your_password
```

### Like a post thread
Like all the replies of a post

```bash
python3 bsky.py likethread -e <post_url> -u your_username -p your_password
```

The `<post_url>` is the url for the post, for instance: https://bsky.app/profile/bsky.app/post/3l327azz5qg24

## Linting

### Installation
```bash
pip install pylint
```

### Usage
```
pylint */*.py *.py
```
