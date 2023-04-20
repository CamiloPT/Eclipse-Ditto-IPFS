import schedule
import time
import helper

print("Listening for Ditto Things started....")
schedule.every().hour.do(helper.save_ditto_things_ipfs)

while True:
    schedule.run_pending()
    time.sleep(1)
