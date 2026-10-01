output "container_registry_name" {
  description = "Name of the Azure Container Registry that stores the documentation-check image."
  value       = azurerm_container_registry.this.name
}

output "container_registry_login_server" {
  description = "Registry login server used when pulling the published image."
  value       = azurerm_container_registry.this.login_server
}
