import os, requests
from dotenv import load_dotenv

load_dotenv('.env')
gh_token = os.environ['GH_TOKEN']
package_name = os.environ['PACKAGE_NAME']
org = os.environ['ORG']


headers = {
  "Accept": "application/vnd.github.v3+json",
  "Authorization": f"token {gh_token}"
}

def list_versions_by_package_name():
  result = requests.get(
    f'https://api.github.com/orgs/{org}/packages/container/{package_name}/versions',
    headers=headers
  )

  # return result.json()
  print( result.json()[1]['metadata']['container']['tags'] )

list_versions_by_package_name()