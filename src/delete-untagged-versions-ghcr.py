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

  return result.json()

def check_versions_untagged() :
  versions = list_versions_by_package_name()
  untagged_list_id = []

  for version in versions:
    tags = version['metadata']['container']['tags']
    
    if tags == [] :
      id = version['id'] 
      untagged_list_id.append( id )
  
  return untagged_list_id