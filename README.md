# cUP (CLI) Viz | A Simple CLI-Visualization for Daily Clickup time-tracking

## Project Goal

The Time Entry Management CLI Tool is designed to help users manage and retrieve time entries efficiently. This command-line interface (CLI) tool allows users to specify a time range, either as today's start and end time or as a custom range, to retrieve and display time entries. Additionally, it supports specifying workspace and user IDs and offers the option to choose the output format between a CLI table and markdown.

## Features

- Retrieve time entries for today's start and end time with the `-t` flag.
- Specify a custom date range for time entries with the `-r` flag.
- Option to adjust for different timezone offsets with the `-z` flag.
- Display results in markdown format using the `-m` flag.
- Support for specifying workspace and user IDs via command-line arguments.
- Defaults to using workspace and user IDs from a local `.env` file if not provided via CLI.

## Usage

To use this tool, you need to have Python installed. You can run the script with various command-line options to manage and retrieve your time entries.

### Command-line Arguments

- `-t`, `--today`: Use today's start and end time.
- `-r`, `--range`: Provide start and end datetime range in format: "yyyymmdd hhmmss".
- `-z`, `--timezone`: Provide a different timezone offset (e.g., 2 for UTC+2).
- `-m`, `--markdown`: Print result as markdown instead of the default CLI table.
- `-w`, `--workspace`: Workspace ID (optional, falls back to `.env` file if not provided).
- `-u`, `--user`: User ID (optional, falls back to `.env` file if not provided).
- `-h`, `--help`: Show this help message and exit.

### Example Commands

1. Retrieve time entries for today:
    ```sh
    python main.py -t
    ```

2. Retrieve time entries for a specific range:
    ```sh
    python main.py -r "20240620 070000" "20240620 170000"
    ```

3. Retrieve time entries with a specific timezone offset:
    ```sh
    python main.py -t -z 2
    ```

4. Retrieve time entries and display the results in markdown format:
    ```sh
    python main.py -t -m
    ```

### Environment Variables

If you do not provide the workspace or user ID via command-line arguments, the tool will use the values from a local `.env` file. Make sure your `.env` file contains the following variables:

```
WORKSPACE_ID=<your_workspace_id>
USER_ID=<your_user_id>
```

## Project Status

The project is currently in its initial development stage. Some core functionalities have been implemented, but additional features and improvements are planned for future releases. Contributions and feedback are welcome!

## Contributing

If you would like to contribute to the project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

Information will follow soon. 
---

Thank you for using cUP (CLI) Viz!
