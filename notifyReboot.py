from datetime import datetime
import requests

now = datetime.now()
current_time = now.strftime("%I:%M %p")

messageValue = 'The rig `Miner1` has rebooted at approximately ' + current_time + '.'

requests.post('https://notifi.it/api', {
    'credentials': '<yourKey>',
    'title': 'Miner1 has rebooted!',
    'message': messageValue,
    'link': 'https://notifi.it'
})
