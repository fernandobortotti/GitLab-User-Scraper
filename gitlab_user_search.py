import argparse
import requests
from bs4 import BeautifulSoup

def search_user(host, username):
    """
    Function to search for a user on a GitLab instance.
    
    Args:
        host (str): The host of the GitLab instance.
        username (str): The username to search for.
    
    Prints:
        Prints the details of the found users including username, full name, and avatar link.
    """
    if len(username) < 2:
        print("Erro: O nome de usuário deve ter pelo menos 2 caracteres.")
        return
    try :
        url = f"https://{host}/search?scope=users&search={username}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            avatar_cells = soup.find_all('div', class_='avatar-cell')

            for cell in avatar_cells:
                user_link = cell.find('a')
                username = user_link['href'].split('/')[-1]
                full_name = user_link.find('img')['alt']
                avatar_link = user_link.find('img')['src']
                print("Usuário:", username)
                print("Nome:", full_name)
                print("Avatar:", avatar_link)
                print("-----------------------------")
        else:
            print(f"Erro: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")
        return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script para buscar usuário no GitLab")
    parser.add_argument("-H", "--host", help="Host do GitLab", required=True)
    parser.add_argument("-u", "--username", help="Palavra chave que será usada para pesquisar o usuário.", required=True)
    args = parser.parse_args()
    search_user(args.host, args.username)
