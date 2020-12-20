import requests
import json
def bubble_sort(high_list , date_list):
    for i in range (len(high_list)-1,0,-1):
        for j in range(i):
            next_high = high_list[j+1]
            next_date = date_list[j+1]
            
            if high_list[j] < next_high:

                temp_high = high_list[j]
                high_list[j] = next_high
                high_list[j+1] = temp_high
                
                temp_date = date_list[j]
                date_list[j] = next_date
                date_list[j+1] = temp_date

#Entry point:
if __name__ == '__main__':
    
    response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo')
    
    if response.status_code == 200:
        #parse response:
        payload = json.loads(response.content)
        
        #printing high values:
        time_series = payload["Time Series (Daily)"]
        length = len(time_series)
        
        high_list = []
        date_list = []
        for (k, v) in time_series.items():
            high_list.append(v["2. high"])
            date_list.append(k)

        bubble_sort(high_list , date_list)

        print("Lowest stock price was on " + date_list[len(date_list) - 1] + "  the stock price was :  " + high_list[len(high_list) - 1])
        print("Highest stock price was on " + date_list[0] + "  the stock price was :  " + high_list[0])
            
    else:
        print('Error: could not load URL')