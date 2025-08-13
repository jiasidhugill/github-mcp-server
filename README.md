# github-mcp-server
An MCP server that automates the pull requests through GitHub.

## Description

## How to use
- read-and-write permissions for pull requests, read permissions for content
- set up .venv
- to install packages: uv sync
- generate .env
  - generate github token
- upload to Claude
- video demo

## Example prompt

Create a pull request for the branch `update-readme` in the repo `test_repo`, owned by `jiasidhugill`. Use the differences between the files in the branch and main to write a pull request summary and title.