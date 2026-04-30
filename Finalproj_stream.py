import pandas as pd
import time

fulldata = pd.read_csv("power_streaming_data.csv")

## And now, the loop!

## This loop will select 5 rows from "power_streaming_data.csv" with replacement, and output them to the "power_stream" folder. 
## This will be carried out 20 times, with a 15 second break between iterations.
for i in range(20):
    fulldata.sample(5)\
        .to_csv(f"power_stream/batch_{i}.csv", 
                
                index = False)
    print("Batch", i, "sent!")
    
    time.sleep(15)
    
print("all done")