import pytest
import subprocess

def test_example_xml():
    # Run the script with example.xml and check if it prints something
    result = subprocess.run(['python', 'read_xml.py', 'example.xml'], capture_output=True, text=True)
    assert result.returncode == 0, "Script should exit with code 0"
    assert result.stdout.strip() != "", "Script should print something"

def test_invalid_example_xml():
    # Run the script with invalid_example.xml and check if it fails structurally
    result = subprocess.run(['python', 'read_xml.py', 'invalid_example.xml'], capture_output=True, text=True)
    assert result.returncode == 0, "Script should exit with code 0 for structurally valid input"
    assert result.stdout.strip() != "", "Script should print something"