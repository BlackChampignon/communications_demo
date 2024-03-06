# Flask Server Interaction Client

## Purpose
The **__client.py__** script provides a command-line interface for interacting with a Flask server script in **__server.py__** that implements basic CRUD (Create, Read, Update, Delete) operations on a list of data items. It allows users to make GET, POST, PUT, and DELETE requests to the server and receive responses accordingly.


## 💻 Usage
1. Install the required modules (`pip install -r requirements.txt`).
2. Run the Flask server (`server.py`).
3. Run the Python client script (`client.py`).
4. Follow the prompts to select options for different types of requests:
   - **Get Data**: Retrieves the current state of the data list from the server.
   - **Post Data**: Adds new data to the server by sending a POST request.
   - **Put Data**: Updates existing data at a specific index on the server by sending a PUT request.
   - **Delete Data**: Removes data at a specific index from the server by sending a DELETE request.
   - **Toggle Raw mode**: Toggles the raw mode. If **on**, all request methods return raw responses.
   - **Exit**: Terminates the script.

## 🔧 Running using command prompt
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
`requests` 2.31.x +

## 🐑 Cloning the Repository
```
git clone https://github.com/BlackChampignon/communications_demo.git
cd communications_demo 
```