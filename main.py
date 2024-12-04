import asyncio
import nest_asyncio

from azure.identity import DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.resource import SubscriptionClient
from msgraph import GraphServiceClient

async def get_users():
    users = await graph_client.users.get()
    if users:
        user_ids = {user.id: user.user_principal_name for user in users.value}
        return user_ids

scopes = ["https://graph.microsoft.com/.default"]
credentials = DefaultAzureCredential()
subscription_client = SubscriptionClient(credentials)
graph_client = GraphServiceClient(credentials=credentials, scopes=scopes)
subscriptions = subscription_client.subscriptions.list()
subscription_map = {subscription.id.split('/')[2]: subscription.display_name for subscription in subscriptions}

nest_asyncio.apply()
azure_user_ids = asyncio.run(get_users())

subscription_access = {}
access = {}
assignment_count = 0

for subscription_id in subscription_map.keys():
    authorization_client = AuthorizationManagementClient(credentials, subscription_id=subscription_id)
    role_assignments = authorization_client.role_assignments.list_for_subscription()
    for role_assignment in role_assignments:
        principal_id = role_assignment.principal_id
        role_definition = authorization_client.role_definitions.get_by_id(role_id=role_assignment.role_definition_id)
        if principal_id in azure_user_ids:
            user = azure_user_ids[principal_id]
            if role_definition.role_name not in access:
                access[role_definition.role_name] = [user]
            else:
                access[role_definition.role_name].append(user)
        assignment_count += 1
    subscription_access[f"{subscription_id} ({subscription_map[subscription_id]})"] = access  

print(subscription_access)