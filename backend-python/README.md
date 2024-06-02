# 📘 Example Fast API

## 🔑 Key Features

## 📋 Pre-requisites

Before you can run this application, you need to ensure your system meets the following requirements:

- Python 3.13 or higher
- Virtual environment setup (virtualenv)
- Yarn package manager for Python entrypoint abstraction
- Access to Azure DevOps for personal access token (PAT) creation and package management


### 💻 Python and Virtual Environment Setup

1. **Download Python 3.13**: Navigate to the [Python 3.13 download page](https://www.python.org/downloads/release/python-3113/) and select the appropriate installer for your operating system. Options include the "Windows installer (64-bit)" for Windows users and the "macOS 64-bit universal2 installer" for macOS users.

2. **Install Python**:
   - Run the downloaded installer. Ensure to select "Add Python 3.11 to PATH" during the installation process to simplify future steps.
   - **Windows**: You may need to run the installer as an administrator. Right-click the installer file and choose "Run as Administrator" from the context menu.
   - **macOS**: Before installation, it's recommended to update your Xcode command line tools by executing the following command in your terminal:
     ```shell
     sudo rm -rf /Library/Developer/CommandLineTools && xcode-select --install
     ```

3. **Install `virtualenv`**:
   - After installing Python, open your command line or terminal and install `virtualenv`, a tool for creating isolated Python environments. This step ensures that the dependencies for one project do not interfere with those of another project.
   - To install `virtualenv`, execute:
     ```shell
     pip install virtualenv
     ```

4. **Creating and Activating a Virtual Environment**:
   - Use `virtualenv` to create an isolated environment for your project, which helps in managing dependencies and avoiding conflicts.
   - Create and activate a virtual environment by running:
     ```shell
     virtualenv env -p /usr/local/bin/python3.11
     source env/bin/activate
     ```
### 📦 Installing Project Dependencies

To install the necessary libraries and packages for the project, follow these steps:

1. Run the command below to install the main project dependencies. When prompted for a username and password, use `azure` as the username and the Personal Access Token (PAT) you generated earlier as the password:

    ```shell
    pip install -r requirements.txt
    ```

2. Next, install the additional development dependencies required for the project's development and testing phases:

    ```shell
    pip install -r requirements.dev.txt
    ```


### ↗️ Pre-commit Hooks

This project uses [pre-commit](https://pre-commit.com/) to manage and maintain pre-commit hooks. To install the hooks, run:

```shell
pre-commit install
```

## 📝 Updating Documentation

To keep the project documentation up-to-date and informative, follow these guidelines when making changes to the codebase or adding new features.

### ✍ Writing Docstrings

- Create [Google style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for any new or updated functions. This style enhances readability and supports automatic documentation generation.
- Ensure docstrings include a brief description of the function's purpose, its parameters, return values, and any exceptions that it might raise.

### 📚 Generating Documentation

We use Sphinx for automatic documentation generation. To update the documentation after code changes:

1. **Run Sphinx**:
   ```bash
   yarn update-docs
    ```
   This command clears the current documentation build, generates new .rst files for any new or updated modules ensuring that all public members and inheritance hierarchies are included, and finally rebuilds the HTML documentation.
2. **Adding New Subfolders**:
For new subfolders or modules added under the src directory, manually add them to the `index.rst` documentation table of contents in `docs` folder to ensure they're included in the documentation structure.
3. **Viewing Documentation Locally**: To preview the documentation locally before committing changes:

    Navigate to `docs/_build/html`.
    Open `index.html` in a web browser to review your documentation updates.
