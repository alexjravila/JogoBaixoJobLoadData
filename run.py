import sentry_sdk
import schedule
import time

sentry_sdk.init("https://2f2ee0c9056b413a8523f41f9621af99@sentry.io/1493413")

def job():
    print("I'm working...")

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)