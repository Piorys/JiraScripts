import requests
import base64
import json


def get_auth(email, api_key):
    cred = email + ":" + api_key
    return str(base64.b64encode(cred.encode('utf-8'))).replace('\'', '')[1:]


def get_issues_by_jql(base_url, auth, jql):
    url = base_url + "/rest/api/3/search"
    querystring = {"jql": jql, "maxResults": "120"}

    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json",
        'Authorization': "Basic " + auth
    }
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    if response.status_code is not 200:
        print(response.text)
        raise Exception("Response code was not 200")
    return json.loads(response.text)


def get_jira_issue(base_url, auth, key):
    url = base_url + "/rest/api/3/issue/" + key

    headers = {
        'Authorization': "Basic " + auth
    }
    response = requests.request("GET", url, headers=headers)
    if response.status_code is not 200:
        print(response.text)
        raise Exception("Response code was not 200")
    return json.loads(response.text)


def add_label_to_issue(base_url, auth, key, label):
    url = base_url + "/rest/api/3/issue/" + key
    payload = "{\"update\":{\"labels\":[{\"add\":\""+label+"\"}]}}"
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Basic " + auth
    }
    response = requests.request("PUT", url, data=payload, headers=headers)

    if response.status_code is not 204:
        print(response)
        raise Exception("Response code was not 204")


def create_issue(base_url, auth, issue_type_key, project_key, summary, description, issue_to_link):
    url = base_url + "/rest/api/3/issue/"
    payload = "{\"fields\":{\"summary\": \""+summary+"\"," \
              "\"description\": {\"type\":\"doc\",\"version\":1," \
              "\"content\":[{\"type\":\"paragraph\",\"content\":[{\"text\": \""+description+"\"," \
              "\"type\":\"text\"}]}]},\"issuetype\":{\"id\":\""+issue_type_key+"\"}," \
              "\"project\":{\"key\": \""+project_key+"\"}}," \
              "\"update\":{\"issuelinks\":[{\"add\":{\"type\":" \
              "{\"id\": \"10003\"," \
              "\"name\":\"Relates\"," \
              "\"inward\":\"relates to\"," \
              "\"outward\":\"relates to\"}," \
              "\"outwardIssue\":{\"key\":\""+issue_to_link+"\"}}}]}}"
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Basic " + auth
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code is not 201:
        print(response.text)
        raise Exception("Response code was not 201 for create issue")
    return json.loads(response.text)
