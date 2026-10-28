
import requests
base_url = "https://api.github.com/users/"
def get_github_info():
    user_name = input("Enter your github username: ")
    full_url = base_url + user_name
    response = requests.get(full_url)
    if response.status_code != 200:
        print("error getting user info!!")
        return None
    info = response.json()
    # print (info)
    details = {
        "name": info["name"],
        "bio": info["bio"],
        "public_repos": info["public_repos"],
        "followers": info["followers"],
        "following" : info["following"],
        'user_view_type' :  info['user_view_type']

    }
    return details

def run():
    print("github user info")
    result = get_github_info()
    if result:
        print(f"Name : {result['name']}")
        print(f"Bio : {result['bio']}")
        print(f"Public Repos : {result['public_repos']}")
        print(f"Followers : {result['followers']}")
        print(f"Following : {result['following']}")
        print(f"user_view_type : {result['user_view_type']}")
    else:
        print("so sorry cant get the user info")
run()