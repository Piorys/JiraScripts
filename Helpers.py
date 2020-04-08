def is_test_linked(issue_details):
    print("Checking issue " + issue_details['key'])
    for linked_issue in issue_details['fields']['issuelinks']:
        if 'outwardIssue' in linked_issue:
            if linked_issue['outwardIssue']['fields']['issuetype']['name'] == 'Test':
                return True
    return False
