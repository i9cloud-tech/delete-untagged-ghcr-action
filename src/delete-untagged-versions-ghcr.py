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

def main(event, context):
  print("______ Delete Versions Untagged ______")

  versions_deleted_ids= check_versions_untagged()

  print( 
    f'''
        __________________________________________________
        |                                                |
        |   Versions id deleted: {versions_deleted_ids}   |
        |                                                |
        __________________________________________________
    '''
  )

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
      delete_versions_untagged( id )
  
  return untagged_list_id

def delete_versions_untagged( id ) :
  requests.delete(
    f'https://api.github.com/orgs/{org}/packages/container/{package_name}/versions/{id}',
    headers=headers
  )