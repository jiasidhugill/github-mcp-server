# github-mcp-server
An MCP server that automates the pull requests through GitHub.

## How to use (with Claude Desktop)
To use, run the following commands: 

```
git clone https://github.com/jiasidhugill/github-mcp-server.git
cd github-mcp-server
python3 -m venv .venv
source .venv/bin/activate
uv sync
```

This creates a virtual environment and installs necessary packages through the package manager [uv](https://docs.astral.sh/uv/).

In order to connect this to Claude, enter Settings > Developer > Edit Config. Add the following to your `claude_desktop_config.json`: 

```
{
    "mcpServers": {
        "github-mcp": {
            "command": "PATH/TO/REPO/.venv/bin/python3",
            "args": ["PATH/TO/REPO/github_mcp.py"]
        }
    }
}
```

In order to allow access to your GitHub, set the following environment variable: 

`GITHUB_TOKEN_FINEGRAINED=<YOUR-TOKEN-HERE>`

Your finegrained GitHub access token must have (at minimum) the following permissions: 
- Content (read-only)
- Pull Requests (read and write)

## Example prompt

Create a pull request for the branch `branch-name` in the repo `repo-name`, owned by `jiasidhugill`. Use the differences between the files in the branch and main to write a pull request summary and title.

Claude may respond by prompting you to set your GitHub access token, creating your pull request automatically, or telling you that some other error has occurred.