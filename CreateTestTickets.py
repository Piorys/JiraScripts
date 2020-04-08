import json
import jira_api
import Helpers

print(
    """
        ###################################################################
        #                          JIRA TOOLS                             #
        #                       CREATE TEST TICKETS                       #
        #                                                                 # 
        #                            APR 2020                             #
        #                                                                 #
        ###################################################################
        """
)

with open('config.json') as f:
    data = json.load(f)

auth = jira_api.get_auth(data['auth']['login'], data['auth']['apikey'])
response_jql = jira_api.get_issues_by_jql(data['base_url'], auth, data['jql'])

created_tickets = []

if len(response_jql['issues']) >= 1:

    print("Found " + str(len(response_jql['issues'])) + " issues")
    for found_issue in response_jql['issues']:
        if not Helpers.is_test_linked(found_issue):
            print("No test ticket found for given issue")
            response = jira_api.create_issue(
                base_url=data['base_url'],
                auth=auth,
                issue_type_key=data['issue_type_key'],
                project_key=data['project_id'],
                summary="Test "+found_issue['fields']["summary"],
                description=data['description']+found_issue['key'],
                issue_to_link=found_issue['key']
            )
            print("Issue created with given key: "+response['key'])
            created_tickets.append(response['key'])
        else:
            print("Test ticket already linked to issue")
    print("Created Issues:")
    print(created_tickets)

else:
    print('No issues were found')
