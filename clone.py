import shutil
import os
import requests
import yaml


def read_session_from_yaml(file_path):
    """
    Reads the session cookie from a YAML configuration file.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        str: Session cookie value.
    """
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data.get('session')
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file '{file_path}' not found.")
    except KeyError:
        raise KeyError("Session key missing in configuration file.")
    except yaml.YAMLError as e:
        raise RuntimeError(f"Error parsing YAML file: {e}")


def download_file(session, url, output_file):
    """
    Downloads a file from a URL using a session cookie for authentication.

    Args:
        session (str): Session cookie value.
        url (str): URL to download the file from.
        output_file (str): Filepath to save the downloaded content.

    Returns:
        bool: True if the download is successful, False otherwise.
    """
    try:
        response = requests.get(url, cookies={'session': session})
        response.raise_for_status()  # Ensure the request was successful
        with open(output_file, 'wb') as file:
            file.write(response.content)
        print(f"Data saved to {output_file}.")
        return True
    except requests.RequestException as e:
        print(f"Error downloading file: {e}")
        return False


def clone_folder(template_path, new_folder):
    """
    Clones a folder structure to a new location.

    Args:
        template_path (str): Path to the folder to clone.
        new_folder (str): Path to create the cloned folder.

    Returns:
        bool: True if the folder was cloned successfully, False otherwise.
    """
    try:
        shutil.copytree(template_path, new_folder)
        print(f"Folder '{new_folder}' created successfully.")
        return True
    except FileExistsError:
        print(f"Folder '{new_folder}' already exists.")
        return False
    except FileNotFoundError:
        raise FileNotFoundError(f"Template folder '{template_path}' not found.")
    except OSError as e:
        print(f"Error cloning folder: {e}")
        return False


def main():
    """
    Main function to handle input, folder creation, and file download.
    """
    yaml_file = 'config.yaml'
    try:
        session = read_session_from_yaml(yaml_file)
    except Exception as e:
        print(f"Error reading session: {e}")
        return

    folder_name = input("What day is it (1-25)? ").strip()
    if not folder_name.isdigit() or not (1 <= int(folder_name) <= 25):
        print("Invalid day. Please enter a number between 1 and 25.")
        return

    day_folder = f"puzzles/day{folder_name}"
    url = f'https://adventofcode.com/2024/day/{folder_name}/input'
    output_file = 'input.txt'

    if clone_folder('template', day_folder):
        os.chdir(day_folder)
        if not download_file(session, url, output_file):
            print("Failed to download input file. Exiting.")
    else:
        print("Folder setup failed. Exiting.")


if __name__ == "__main__":
    main()
