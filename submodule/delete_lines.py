import datetime
import time

class LineDeleter():
    def __init__(self,file_path):
        print('initing line deleter')
        self.file_path = file_path

    def write_now_time(self,content):
        f = open(self.file_path,"a")
        f.write(content + " - " + str(datetime.datetime.now()) + "\n")
        f.close()

    def parse_line(self,line):
        return line.split(" - ")
    
    def get_datetime(self,line):
        return parse_line(line)[1]
    
    def get_deltaMonthDate(self,now,delta):
        month = now.month
        if(delta > 12 or delta < 1):
            raise Exception("delta precisa estar entre 1 e 12")
        if(delta > month):
            d = (now.month-delta)%12
            return datetime.datetime(now.year-1,d,now.day)
        elif(delta < month):
            d = (delta-now.month)%12
            return datetime.datetime(now.year,d,now.day)
        else:
            return datetime.datetime(now.year-1,now.month,now.day)

    def delete_lines(self,time2delete):
        f = open(self.file_path,"r+")
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            #delta = int((datetime.datetime.now() - datetime.datetime.strptime(i.replace("\n",""), "%Y-%m-%d %H:%M:%S.%f")).total_seconds())
            now = datetime.datetime.now()
            get_datetime(line)
            new_delta = get_deltaMonthDate(now, time2delete)
            if(delta > time2delete):
                f.write("")
            else:
                f.write(i)
        f.truncate()
        f.close()
