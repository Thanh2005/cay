import requests
import json
import time
with open('token.json') as f:
    data = json.load(f)
token = data['token']
account = data['account']

headers = {
    "Authorization": "Bearer "+token,

}

def lum():
    thang = requests.get("https://api.quackquack.games/golden-duck/info", headers=headers)
    thang = thang.json()
    timedemngc = thang['data']['status']
    if(timedemngc == 1):
        thang1 = requests.get("https://api.quackquack.games/golden-duck/reward", headers=headers)
        requ = thang1.json()
        print(requ)
    
        if(requ['error_code'] == 'NOT_ENOUGH_TIME_TO_GOLDEN_DUCK'):
            keo = True
        else:
            data = {
            "type": 1
        }
            thang = requests.post("https://api.quackquack.games/golden-duck/claim", headers=headers, data=data)
            print(thang.json())
    
def gomtrung():
    getlist = requests.get(url="https://api.quackquack.games/nest/list-reload", headers=headers)
    get1 = json.loads(getlist.text)
    get2 = get1["data"]['nest']
    
    for trung in get2:
        if trung['type_egg'] is None:
            pass
        else:

            if(trung['type_egg'] >= 8):
                bantrung()
                id = trung['id']
                data = {
                "nest_id": id
            }
                hatch = requests.post("https://api.quackquack.games/nest/hatch", data=data, headers=headers)
                hatch = hatch.json()
                if(hatch['error_code'] == ''):
                    timehatch = hatch["data"]['time_remain']
                    time.sleep(timehatch)
                    time.sleep(1)
                    collect = requests.post("https://api.quackquack.games/nest/collect-duck", data=data, headers=headers)
                    collect = collect.json()
                    if(collect['error_code'] == ''):
                        duck_id = collect['data']['duck_id']
                        total_rare = collect['data']['total_rare']
                        arm_rare = collect['data']["metadata"]['arm_rare']
                        body_rare = collect['data']["metadata"]['body_rare']
                        head_rare = collect['data']["metadata"]['head_rare']
                        
                        message = f'<========={account}=========>\ntotal_rare: {total_rare}\narm_rare: {arm_rare}\nbody_rare: {body_rare}\nhead_rare: {head_rare}\n ID egg: {duck_id}'
                        
                        requests.get("https://api.telegram.org/bot6119706691:AAEr5AVcgO3vAVWqAAAFzYJ6qvE7keOGA4s/sendMessage?chat_id=-4237972364&text="+message)
                    else:
                        requests.get("https://api.telegram.org/bot6119706691:AAEr5AVcgO3vAVWqAAAFzYJ6qvE7keOGA4s/sendMessage?chat_id=-4237972364&text=DUCK có ID "+str(duck_id)+" đã nở thất bại")

            else:
                pass


    for trung in get2:
        
        if(trung['status'] == 2):
            id = trung['id']
            data = {
            "nest_id": id
        }
            chay = requests.post(url="https://api.quackquack.games/nest/collect", data=data, headers=headers)
            chay1 = requests.get(url="https://api.quackquack.games/balance/get", headers=headers)
            ahihi = chay1.json()
            bucu = ahihi["data"]['data']
            for item in bucu:
                if(item['symbol'] == 'EGG'):
                    itemegg = item
                    break
            for item in bucu:

                if(item['symbol'] == 'PET'):
                    itemegg1 = item
                    break

            print("Đã claim 1 trứng. Tổng số trứng là "+itemegg["balance"]+", số meme là "+itemegg1['balance'])
            

def bantrung():
    getlist = requests.get(url="https://api.quackquack.games/nest/list-reload", headers=headers)
    get1 = json.loads(getlist.text)
    duck = get1['data']['duck']
    
    for trung in duck:
        if((trung['metadata']['arm_rare'] + trung['metadata']['body_rare'] + trung['metadata']['head_rare'] ) == 5):
            id = trung['id']
            print(id)
            data = {
                "ducks": '{"ducks":['+str(id)+']}'
            }
            remove = requests.post("https://api.quackquack.games/duck/remove", headers=headers, data=data)
            print(remove.text)
            remove = remove.json()
            if(remove["data"] == True):
                requests.get("https://api.telegram.org/bot6119706691:AAEr5AVcgO3vAVWqAAAFzYJ6qvE7keOGA4s/sendMessage?chat_id=-4237972364&text=DUCK có ID"+str(id)+" đã bị bán")
                break
            else:
                print("đầy trứng rare rồi bạn ơi")
                break
        
        
while True:
    time.sleep(2)
    lum()
    gomtrung()
