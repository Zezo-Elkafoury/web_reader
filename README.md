# Web Content Reader

This project is a web content reader that extracts various elements from websites, such as buttons, text, forms, and inputs, and organizes them into a structured JSON format.

## Project Structure

```
web-content-reader
├── src
│   ├── reader.py          # Main entry point of the application
│   ├── extractor.py       # Contains WebContentExtractor class for element extraction
│   ├── parser.py          # Contains WebContentParser class for parsing and JSON conversion
│   └── utils
│       └── __init__.py    # Utility functions and constants
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd web-content-reader
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To use the web content reader, run the `reader.py` file:

```
python src/reader.py <url>
```

Replace `<url>` with the website you want to extract content from.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.