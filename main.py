import requests
import selectorlib
import sqlite3


URL = 'http://programmer100.pythonanywhere.com/tours/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

insert_query = "INSERT INTO events VALUES ('ban2', 'city2', '2025.12.25)"
select_query = "SELCT * FROM events WHERE date='2025.12.25"
connection = sqlite3.connect("data.db")

def scrape(url):
    """ scrape the page source from URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source_text):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    # extract function returns a dictionary of the items in the "extract.yaml", here "tours" pointing to the id of the text
    extract_text = extractor.extract(source_text)["tours"]
    return extract_text

def send_email():
    print("Email sent")

# def store(extracted_data):
#     with open("data.txt", 'a') as file:
#         file.write(extracted_data + "\n")
#
# def read_store(filename="data.txt"):
#     with open(filename, "r") as file:
#         return file.read()

def store(data):
    new_data = data.split(sep=',')
    new_data = [item.strip() for item in new_data]
    query = "INSERT INTO events VALUES (?,?,?)"
    cursor = connection.cursor()
    try:
        cursor.execute(query, new_data)
        connection.commit()
        return True
    except:
        return False


def read_store(data):
    cursor = connection.cursor()
    row = data.split(sep=',')
    row = [item.strip() for item in row]
    band, city, date = row
    query = "SELECT * FROM events WHERE band=? and city=? and date=?"
    # the values in band city and date will replace the '?' in query
    cursor.execute(query, (band, city, date))
    rows = cursor.fetchall()
    return  rows


if __name__ == "__main__":
    scrape = scrape(URL)
    extracted = extract(scrape)
    print(extracted)

    if extracted != "No upcoming tours":
        content = read_store(extracted)
        if not content:
            print(content)
            result = store(extracted)
            if not result:
                print('could not write data')
            else:
                print('data written to db')
            send_email()
        else:
            print("data is already in db")


