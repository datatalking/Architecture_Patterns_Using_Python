# conftest.py

import pytest
import subprocess
import time

@pytest.fixture
def restart_api():
    """Restarts the API before running a test."""
    subprocess.run(["pkill", "-f", "your_api_process"])  # Adjust for your API
    time.sleep(2)  # Allow time for shutdown
    subprocess.Popen(["python", "your_api_entrypoint.py"])
    time.sleep(2)  # Allow time for startup
    yield
    subprocess.run(["pkill", "-f", "your_api_process"])
