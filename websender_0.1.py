#Project made by Kubzel
#
'''

$$\   $$\          $$\                           $$\ 
$$ | $$  |         $$ |                          $$ |
$$ |$$  /$$\   $$\ $$$$$$$\  $$$$$$$$\  $$$$$$\  $$ |
$$$$$  / $$ |  $$ |$$  __$$\ \____$$  |$$  __$$\ $$ |
$$  $$<  $$ |  $$ |$$ |  $$ |  $$$$ _/ $$$$$$$$ |$$ |
$$ |\$$\ $$ |  $$ |$$ |  $$ | $$  _/   $$   ____|$$ |
$$ | \$$\\$$$$$$  |$$$$$$$  |$$$$$$$$\ \$$$$$$$\ $$ |
\__|  \__|\______/ \_______/ \________| \_______|\__|
                                                     

'''
from discord import Webhook, SyncWebhook




def webhook_session(url):
    requestmes = SyncWebhook.from_url(url)
    print('Press CTRL+C TO EXIT')
    print('Enter Text')
    while True:
        meesage = (input())
        requestmes.send(meesage)
    

def main():
    web_url = input("Input webhook url:")
    webhook_session(web_url)



main()













   
        




        







    


