'''
Output:
    TypeError: Session.request() got an unexpected keyword argument 'content'

Solution:
    - Remove the 'content=True'
'''

# Import requests package
import requests

requests.get(url="https://app.datacamp.com", content=True)
