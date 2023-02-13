import requests
import selectorlib

URL = 'http://programmer100.pythonanywhere.com/tours/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


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

def store(extracted_data):
    with open("data.txt", 'a') as file:
        file.write(extracted_data + "\n")

def read_store(filename="data.txt"):
    with open(filename, "r") as file:
        return file.read()

if __name__ == "__main__":
    scrape = scrape(URL)
    extracted = extract(scrape)
    print(extracted)
    content = read_store()
    if extracted != "No upcoming tours":
        if extracted not in content:
            store(extracted)
            send_email()

