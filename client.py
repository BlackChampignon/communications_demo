import requests

server_url = "http://127.0.0.1:5000"  # Check if the url of the flask server is correct


def get_data(raw=False):
    response = requests.get(f"{server_url}/get_data")
    if raw:
        print(response)
        print(response.headers)
        print(response.content)
    else:
        print(response.json())


def post_data(raw=False):
    data = input("Enter data to post: ")
    response = requests.post(f"{server_url}/post_example", json=data)
    if raw:
        print(response)
        print(response.headers)
        print(response.content)
    else:
        print(response.json())


def put_data(raw=False):
    index = input("Enter index to update: ")
    data = input("Enter new data: ")
    response = requests.put(f"{server_url}/put_example/{index}", json=data)
    if raw:
        print(response)
        print(response.headers)
        print(response.content)
    else:
        print(response.json())


def delete_data(raw=False):
    index = input("Enter index to delete: ")
    response = requests.delete(f"{server_url}/delete_example/{index}")
    if raw:
        print(response)
        print(response.headers)
        print(response.content)
    else:
        print(response.json())


def main():
    raw = False
    while True:
        print("\n")
        if raw:
            print(f"Raw is set to - {raw}")
        print("Choose an option:")
        print("1. Get Data")
        print("2. Post Data")
        print("3. Put Data")
        print("4. Delete Data")
        print("5. Toggle raw json")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            get_data(raw)
        elif choice == "2":
            post_data(raw)
        elif choice == "3":
            put_data(raw)
        elif choice == "4":
            delete_data(raw)
        elif choice == "5":
            raw = True
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
