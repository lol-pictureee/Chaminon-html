

def delete_html_file(repo_owner, repo_name, file_path, github_access_token):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    headers = {
        'Authorization': f'token {github_access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # РџРѕР»СѓС‡Р°РµРј РёРЅС„РѕСЂРјР°С†РёСЋ Рѕ С„Р°Р№Р»Рµ, С‡С‚РѕР±С‹ РїРѕР»СѓС‡РёС‚СЊ SHA
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"РћС€РёР±РєР°: {response.status_code}")
        return

    file_info = response.json()
    sha = file_info['sha']

    # РЈРґР°Р»СЏРµРј С„Р°Р№Р»
    delete_data = {
        'message': 'РЈРґР°Р»РµРЅРёРµ .html С„Р°Р№Р»Р°',
        'sha': sha
    }

    response = requests.delete(url, headers=headers, json=delete_data)
    if response.status_code == 200:
        print("Р¤Р°Р№Р» СѓСЃРїРµС€РЅРѕ СѓРґР°Р»РµРЅ!")
    else:
        print(f"РћС€РёР±РєР° СѓРґР°Р»РµРЅРёСЏ С„Р°Р№Р»Р°: {response.status_code}")
        print(response.json())

# РїСЂРёРјРµСЂ РёСЃРїРѕР»СЊР·РѕРІР°РЅРёСЏ
# delete_html_file('lol-pictureee', 'Chaminon-html', 'page.html', github_access_token)