class user:
    def __init__(self, id=None, name=None, tel=None, trainCount=None, detailDayList=None, picture=None):
        self.id = id
        self.name = name
        self.tel = tel
        self.trainCount = trainCount
        self.detailDayList = detailDayList
        self.picture = picture

class detailDayInfo:
    def __init__(self, date=None, plan=None, item=None):
        self.date = date
        self.plan = plan
        self.item = item
        