# Delete Untagged Versions of GHCR Packages

This action was created delete the unmarked versions of ghcr package.

The official action to [Delete Package Versions](https://github.com/marketplace/actions/delete-package-versions) of Github deletes versions of a package from GitHub Packages except ghcr packages. 

To use this action, you must have admin permissions in the organization and authenticate using an access token with the packages:read and packages:delete scopes. In addition:

This package_type is container, you must also have admin permissions to the container you want to delete.

## Inputs 
```
  gh-token:
    description: 'token connect Github'
    require: true
  package-name:
    description: 'the name of the package'
    require: true
  org:
    description: 'organization'
    require: true
```
