import socket
import json
import requests
import stock_json

s = socket.socket()
host = socket.gethostname()
port = 5599
s.bind((host , port))

s.listen(5)
while True:
    c,addr = s.accept()
    
    received_data = (c.recv(6000))
    
    decoded_data = received_data.decode('utf-8')
    json_data = json.loads(received_data)
    position = int(json_data['top_count'])

    response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo")
    data = json.loads(response.content)

    time_series = data["Time Series (Daily)"]
    length = len(time_series)
        
    high_list = []
    date_list = []
    for (k, v) in time_series.items():
        high_list.append(v["2. high"])
        date_list.append(k)

    stock_json.bubble_sort(high_list , date_list)

    
    
    def send_list(high_list, date_list, position):

        n_list = []

        for i in range (len(high_list)):            
            if (i < (10*position)):
                    
                    n_list.append(high_list[i])
                
            else:
                break
                        
        return n_list

            
    
    msg = send_list(high_list, date_list, position)
    
    msg_str = json.dumps(msg)
    msg_bytes = bytes(msg_str , "utf-8")
    c.send(msg_bytes)

    c.close()