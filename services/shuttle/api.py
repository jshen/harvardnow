import requests

AGENCY = "52"
KEY = 'op8wGpiS5Emsh5KZtdo1Mn5hHWNpp1hVi8FjsnUgr0kn5fejO8'
HEADERS = {
    'X-Mashape-Key': KEY,
    'Accept': 'Accept: application/json'
}

def get(endpt,agency=AGENCY,key=KEY,headers=HEADERS,params={}):
    params['agencies'] = agency
    page = "https://transloc-api-1-2.p.mashape.com/%s.json"%endpt
    return requests.get(page,headers=headers,params=params).json()
