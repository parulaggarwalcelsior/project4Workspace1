variable "resource_group_name" {
  description = "Name of the Azure resource group that contains the container registry."
  type        = string
}

variable "location" {
  description = "Azure region for the resource group and container registry."
  type        = string
}

variable "container_registry_name" {
  description = "Globally unique Azure Container Registry name."
  type        = string
}

variable "image_tag" {
  description = "Commit SHA tag produced by the deployment pipeline. The image shape records it at plan time but runs no workload."
  type        = string
}

variable "tags" {
  description = "Optional tags applied to Azure resources."
  type        = map(string)
  default     = {}
}
