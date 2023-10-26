#GDSC Intro Session: Drawing Activity

###Creating a Virtual Environment

To create a virtual environment, open a terminal and navigate to the directory where you want to create the virtual environment. Then, run the following command:

    python -m venv .venv
This will create a new directory called .venv containing a copy of the Python interpreter, the pip package manager, and other necessary files.

###Activating the Virtual Environment

To activate the virtual environment, run the following command:

    source .venv/bin/activate
This will update your environment variables so that Python and pip use the virtual environment instead of the global installation.

###Installing the Pygame Library

To install the Pygame library, run the following command:

    pip3 install pygame
This will install the Pygame library into the virtual environment.

###Running Your Code

To run your code, simply type the following command:

    python shape.py
This will start the Python interpreter and execute your code.

Example

    # Create a virtual environment
    python -m venv .venv

    # Activate the virtual environment
    source .venv/bin/activate

    # Install the Pygame library
    pip3 install pygame

# Run your code
    python shape.py
Note: Once you have finished using the virtual environment, you can deactivate it by running the following command:

    deactivate
This will restore your original environment variables.