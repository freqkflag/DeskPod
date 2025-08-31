# DeskPod Project Documentation

## Overview
DeskPod is a project designed to provide Ubuntu users with a seamless way to switch between multiple desktop environments (DEs) without the risk of dependency conflicts or system instability. By using containerization technology, each desktop environment runs in its own isolated "pod" while maintaining access to the user's home directory, ensuring a consistent and personalized user experience across all installed DEs.

## Installation
To install DeskPod, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/DeskPod.git
   cd DeskPod
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage
Once the application is running, you will see a graphical interface that allows you to select and switch between the available desktop environments. Simply click on the desired environment to launch it in a container.

## Project Structure
```
DeskPod
├── src
│   ├── main.py          # Entry point for the DeskPod application
│   ├── gui              # Contains GUI components
│   │   └── __init__.py
│   ├── containers       # Manages containerization aspects
│   │   └── __init__.py
│   └── config           # Configuration files
│       └── deskpod_config.json
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── setup.py             # Packaging information
```

## Contributing
Contributions to DeskPod are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.