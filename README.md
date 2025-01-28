# Bus Driver Assistant

This project is designed to support bus drivers by providing essential tools for passenger monitoring and foreign passenger assistance. Using advanced AI technologies, the program ensures safety and enhances communication with passengers.

## Overview

- **Purpose:**
  - Assist bus drivers in monitoring passenger activity for safety purposes.
  - Provide real-time language translation and communication tools for foreign passengers.
  - Alert drivers in specific situations, such as overcrowding or potential safety hazards.

## Features

1. **Passenger Monitoring:**
   - Monitors passengers in the bus to identify overcrowding or safety concerns.
   - Provides real-time alerts to the driver for immediate action.
2. **Foreign Passenger Assistance:**
   - Supports multiple languages, including English, Japanese, Chinese, and more.
   - Provides real-time translation of speech to text and text to speech.
3. **Speech Recognition and Translation:**
   - Utilizes the ETRI WiseASR API for accurate speech recognition.
   - Integrates with Papago for multilingual translation.
4. **Interactive User Interface:**
   - Built with PyQt5 for a user-friendly interface.
   - Displays current and next bus stops in multiple languages.
5. **Driver Alerts:**
   - Real-time alerts for safety issues detected through passenger monitoring.

## Components

### Backend
- **Python Scripts:**
  - `main_window.py`: Manages the main program interface and logic.
  - `translation.py`: Handles speech recognition and translation using ETRI API and Papago.
  - `structure.py`: Defines the overall application flow.
- **APIs:**
  - ETRI WiseASR API for speech recognition.
  - Papago API for language translation.

### Frontend
- **PyQt5 Interface:**
  - Provides a graphical interface for the driver to view translations, alerts, and passenger information.
  - Displays multilingual information about bus stops.

### Data Files
- Audio files and JSON results generated from speech recognition.

## Setup Instructions

### Prerequisites
- Python 3.8 or above.
- Required Python packages: `PyQt5`, `urllib3`, `gtts`, `playsound`.

### Installation Steps
1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. **Install Dependencies:**
   ```bash
   pip install PyQt5 urllib3 gtts playsound
   ```
3. **Set Up API Keys:**
   - Add your ETRI API key in the `translation.py` file:
     ```python
     accessKey = 'your_etri_api_key_here'
     ```
   - Add your Papago API credentials in the `translation.py` file:
     ```python
     client_id = 'your_papago_client_id'
     client_secret = 'your_papago_client_secret'
     ```

### Run the Application
1. Launch the program using the following command:
   ```bash
   python main_window.py
   ```
2. The user interface will display the current and next bus stops, translation tools, and passenger monitoring alerts.

## Usage

1. Start the program.
2. Use the multilingual buttons to switch the interface language.
3. Click the "Speak" button and talk for real-time translation and speech-to-text.
4. Monitor passenger activity through the interface for safety alerts.
5. View translated bus stop information to assist foreign passengers.


## License

This project is open-source and available under the [MIT License](LICENSE).

---

For more details, refer to the provided Python scripts.
