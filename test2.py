import requests

word = "I am Killy. I've been climbing up the labyrinthine, massive structure of Blasphemo. It's unknown just how deep or how tall the terrifying, almost majestic mechanical expanse climbs. At times it's a series of claustrophobic halls and alleys that climb or descend seemingly forever, metal ripped from the walls by cybernetic claws of some synthetic abomination. At other times, I find wide stretches of unspeakably beautiful mechanical landscape. I may see colossal constructs repairing or building onto machinery that stretches for miles around with unimaginable purpose, or hundreds of small drones flying like flocks of birds inside metal domes that stretch as far as the horizon reaches. I steadily climb. I've been travelling upwards for years and years to reach the top of Blasphemo with no end in sight. My footsteps echo down the metallic, claustrophobic hall. Wires hanging down spark with blue electrical discharges and the sound of whining circuits hum constantly in your ears. I'm searching for a way to stop the growth of Blasphemo. That was my purpose, although I've long forgotten who gave me that purpose. All I've seen is horror after horror, atrocities and nightmares."
url = "https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl=ko&q=" + word
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}


request_result = requests.get(url, headers=headers).json()

print(request_result['sentences'])
try:
    for i in request_result['sentences']:
        print(i['trans'])
except KeyError:
    pass
#print('[In English]: ' + request_result['alternative_translations'][0]['alternative'][0]['word_postproc'])
print('[Language Dectected]: ' + request_result['src'])
