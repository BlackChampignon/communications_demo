# Flask Server Interaction Client

## Purpose
The **client.py** script provides a command-line interface for interacting with a Flask server script in **server.py** that implements basic CRUD (Create, Read, Update, Delete) operations on a list of data items. It allows users to make GET, POST, PUT, and DELETE requests to the server and receive responses accordingly.


## Usage
1. Ensure that the Flask server is running and accessible at the specified URL.
2. Run the Python script in your terminal or command prompt.
3. Follow the prompts to select options for different types of requests:
   - **Get Data**: Retrieves the current state of the data list from the server.
   - **Post Data**: Adds new data to the server by sending a POST request.
   - **Put Data**: Updates existing data at a specific index on the server by sending a PUT request.
   - **Delete Data**: Removes data at a specific index from the server by sending a DELETE request.
   - **Toggle Raw mode**: Toggles the raw mode. If **on**, all request methods return raw responses.
   - **Exit**: Terminates the script.

## 🔧 Running
```
pip install -r requirements.txt
python server.py
```
Then run the client script:
```
pyhton client.py
```

## 📦 Requirements
`Python` 3.12 +  
`flask` 2.5.x +
`pyinstaller` 6.3.x +

## 🐑 Cloning the Repository
```
git clone https://github.com/BlackChampignon/communications_demo.git
cd communications_demo 
```

## 🧱 Script Structure
- **Imports**: The script imports the `requests` library to make HTTP requests to the Flask server.
- **Global Variables**: `server_url` specifies the URL of the Flask server. Update this variable with the appropriate URL.
- **Function Definitions**: 
  - `get_data()`, `post_data()`, `put_data()`, `delete_data()`: Functions for making different types of requests to the server.
  - `main()`: Main function providing a command-line interface for user interaction.
- **Main Execution**: Checks if it's being run directly (`__name__ == "__main__"`) and calls the `main()` function.

## Example Usage
1. Run the Flask server (`server.py`).
2. Run the Python script (`client.py`).
3. Choose options from the command-line menu to perform various CRUD operations on the server.
