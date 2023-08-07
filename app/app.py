from helper import save_ditto_things_ipfs
import schedule
import time

print("Listening for Ditto Things started....")
save_ditto_things_ipfs()
schedule.every().hour.do(save_ditto_things_ipfs)

while True:
    schedule.run_pending()
    time.sleep(1)
