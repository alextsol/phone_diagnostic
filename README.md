## Prerequisites

Before running the Phone Diagnostic Tool, ensure you have Python installed on your system. The application has been tested with Python 3.8 and above.

### Required Libraries

- **Tkinter**: Used for the GUI interface. Tkinter comes pre-installed with Python.
- **Python Standard Library**: No additional external libraries are required as the application uses standard libraries that come with Python.

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/alextsol/phone_diagnostic.git
cd phone_diagnostic
```

2. **No additional installation steps are required** for libraries since Tkinter is part of the Python Standard Library.

## Running the Application

To run the Phone Diagnostic Tool, navigate to the project directory and execute the main script:

```bash
python app_gui.py
```

This command will launch the GUI application where you can start the diagnostic process by entering the name and model of your phone, followed by answering a series of questions to diagnose potential issues.

## Files Overview

- **`app_gui.py`**: The main Python script that initializes and runs the Tkinter GUI application.
- **`diagnostic_logic.py`**: Contains the logic to diagnose the phone based on user responses.
- **`diagnosis.py`**: Defines possible diagnoses and symptoms associated with each diagnosis.
