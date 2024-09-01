# BlueSky tool
A tool for [BlueSky](https://bsky.app) tricks.

Features:
- Follow back who follows you
- Follow back who liked your posts
- Follow back who liked a post
- Like a post thread

## Installation
Install [Python3](https://www.python.org/)
```bash
pip install atproto
```

## Usage

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