
import requests



class FacebookGraphAPI:
    def __init__(self, account_id, token):
        self.base_url = f"https://graph.facebook.com/v15.0/act_{account_id}"
        self.token = token

    def fetch_insights_data(self, filters=''):
        
        url = f"{self.base_url}/insights?{filters}"

        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/x-www-form-urlencoded'
            }
        all_data = []
        counter = 1
        while True:
            print("Fetching data, page -> ",counter)
            response = requests.request("GET", url, headers=headers)
            all_data.extend(response.json()['data'])
            try:
                next = response.json()['paging']['next']
            except:
                print("There isn't a next page")
                break
            url = next
            counter += 1
            
        return all_data

if __name__=="__main__":
    api = FacebookGraphAPI(
        account_id='',
        token=''
    )

    data = api.fetch_insights_data(filters='')