import requests
from pathlib import Path

filename = Path('assets/metadata.pdf')
url = 'https://app.terra360.io/storage/files/87e97be9c85705cf52b25ce2da1fe3da.pdf'

response = requests.get(url, stream=True)
filename.write_bytes(response.content)
