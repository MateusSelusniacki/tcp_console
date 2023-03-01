import schedule
import time
import delete_lines
import threading

class sched():
    def __init__(self,file2watch):
        self.line_deleter = delete_lines.LineDeleter(file2watch)
        threading.Thread(target = self.create_schedule).start()
        
    def job(t):
            self.line_deleter.write_now_time()
            return

    def create_schedule(self):
        print('creating schedule')
        schedule.every().day.at("10:00").do(self.job,'It is 01:00')

        while True:
            schedule.run_pending()
            time.sleep(0.5) # wait one minute

s = sched("delete_line_files.txt")