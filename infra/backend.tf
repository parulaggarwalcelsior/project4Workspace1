terraform {
  backend "azurerm" {}
}

# Backend settings are deliberately passed by `terraform init -backend-config`
# in the GitHub workflow.  No storage-account identifiers or credentials live here.
