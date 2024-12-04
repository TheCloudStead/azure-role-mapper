# Azure Role Assignment Mapper

This project is all about mapping who has access to what within Azure subscriptions. The script scrapes Azure to determine which users have been assigned to specific roles in different subscriptions. It provides a comprehensive view of access across the organization, making it easier to manage and audit permissions without endless clicking through the Azure Portal.

## Features

- **Lists all subscriptions**: Collects all Azure subscriptions and maps subscription IDs to display names for easy reference.
- **Fetches user data**: Pulls users' `principal_id` and `user_principal_name` from Entra ID (Azure AD).
- **Maps role assignments**: Matches users to their role assignments, categorizing them by role definitions.
- **User-Friendly Output**: Utilizes a console output to provide a clear visualization of access details.

## Prerequisites

- Python 3.8+
- Azure credentials with sufficient permissions to call Azure Resource Manager and Microsoft Graph APIs (details below).
- Required Python packages (see installation steps).

### Install the Python dependencies:

```bash
azure-identity
azure-mgmt-authorization
azure-mgmt-resource
msgraph-sdk
```

### Environment Configuration:

Set up authentication using `DefaultAzureCredential`:
1. Log in via Azure CLI:
   ```bash
   az login
   ```
2. Ensure the environment has the necessary permissions to fetch user and subscription data.

## Usage

### 1. Clone this repository:
```bash
git clone https://github.com/TheCloudStead/azure-role-mapper.git
cd azure-role-mapper
pip install -r requirements.txt
```

### 2. Run the script:
```bash
python main.py
```

This will fetch all users, role assignments, and subscriptions and output them in a neat, readable format.

## Example Output

```plaintext
{
    "subscription_id (Subscription Display Name)": {
        "Owner": ["user1@example.com", "user2@example.com"],
        "Contributor": ["user3@example.com"],
        "Reader": ["user4@example.com"]
    }
}
```

## Limitations

- **Permissions**: Ensure your credentials have the following:
  - Access to Azure Resource Management APIs.
  - Permissions to query Microsoft Graph (User.Read.All, RoleManagement.Read.Directory).
- **Performance**: May take longer for tenants with large numbers of users or role assignments.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Thank you to the readers of my Medium articles!