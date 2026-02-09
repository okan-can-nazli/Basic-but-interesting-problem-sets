import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import json

with open("fake_db.json", "r") as f:
    data = json.load(f)
    

dates = data["dates"]
prices_list = data["prices"]



price_array = np.array(prices_list)

#Calculate how many items are "extra" at the start
remainder = len(price_array) % 30

#Slice off the first "remainder" elements
price_clean = price_array[remainder:]

#Reshape into (Batch, Time_Step)
price_reshaped = price_clean.reshape(-1, 30)



price_t = torch.from_numpy(price_reshaped).float()
#price data was formatted as tensor but we can not do same thing for the dates because its in "YYYY-MM-DD" format



