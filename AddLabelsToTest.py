import json
import jira_api

print(
    """
        ###################################################################
        #                          JIRA TOOLS                             #
        #                       ADD LABELS TO TEST                        #
        #                                                                 # 
        #                            APR 2019                             #
        #                                                                 #
        ###################################################################
        """
)


with open('config.json') as f:
    data = json.load(f)

auth = jira_api.get_auth(data['auth']['login'], data['auth']['apikey'])
response_jql = jira_api.get_issues_by_jql(data['base_url'], auth, data['jql'])


if len(response_jql['issues']) >= 1:

    print("Found " + str(len(response_jql['issues'])) + " issues")
    for found_issue in response_jql['issues']:
        print("Checking issue " + found_issue['key'])
        for linked_issue in found_issue['fields']['issuelinks']:
            if 'outwardIssue' in linked_issue:
                if linked_issue['outwardIssue']['fields']['issuetype']['name'] == 'Test':
                    print("Found linked test ticket " +
                          linked_issue['outwardIssue']['key'])
                    issue = jira_api.get_jira_issue(
                        data['base_url'], auth, linked_issue['outwardIssue']['key'])
                    if data['label_to_add'] not in issue['fields']['labels']:
                        print("Label " + data['label_to_add'] + " was not found within given issue " +
                              linked_issue['outwardIssue']['key'])
                        print("Adding label to issue")
                        jira_api.add_label_to_issue(data['base_url'], auth,
                                                    linked_issue['outwardIssue']['key'], data['label_to_add'])
                    else:
                        print("Label already added to given issue")
else:
    print('No issues were found')
