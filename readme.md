# Jira Scripts

Set of scripts which should help you working with Zephyr test plugin in JIRA

## Contents
1. Instalation
2. Configuration
3. Usage

## Installation
**In order to use this scripts you have to have Python3 installed on your machine.**  

To install dependencies use following command:
```
pip install -r requirements.txt
```

expected output is that requests library will be installed  

## Configuration
Before you use this set of tools, you have to generate your personal atlassian API key. In order to do that go to: Account Settings -> Security -> Create and manage API tokens -> Create API token
  

All configuration is done using **config.json** file  
- Auth - contains you login email and previously generated API token
- JQL - Jira Query Language query for tickets for which You want to create test tickets/add labels to linked test tickets. Be mindful about character escaping!
- label_to_add - define JIRA label which you want to use
- base_url - URL for JIRA instance, ex https://project.atlassian.net
- issue_type_key - JIRA issue type for "test" type ticket (varies from project to project)
- project_id - ID for JIRA project by which tickets are created ex. TEST-1234
- description - description for created test tickets, by default description is set to "Test for [linked issue]"

## Usage

After having everything set up you can use scripts by following commands:

### Create Test Tickets
```bash
python CreateTestTickets.py
```

Script will gather all issues using provided JQL query and for each ticket will create test ticket and link it to it. 
  
Script will verify whether test ticket has not been previously created.  

Output is list of created JIRA issues

### Add Labels To Tests
```bash
python AddLabelsToTest.py
```

Script will gather all issues using provided JQL query and will add previously defined label to each linked test ticket.