# written by Adarsh Rajput
def Split(mix): 
    ev_li = [] 
    od_li = [] 
    for i in mix: 
        if (i % 2 == 0): 
            ev_li.append(i) 
        else: 
            od_li.append(i) 
    print("Even lists:", ev_li) 
    print("Odd lists:", od_li) 
  
mix = [2, 5, 8, 7, 20, 62] 
print mix
Split(mix)
