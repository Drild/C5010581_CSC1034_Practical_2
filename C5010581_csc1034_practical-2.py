class Job:
    def __init__(self, name, category, rate, date, hours):
        self.name = name
        self.category = category
        self.rate = rate
        self.date = date
        self.hours = hours
    def get_name(self):
        return self.name
    def get_category(self):
        return self.category
    def get_rate(self):
        return self.rate
    def get_date(self):
        return self.date
    def get_hours(self):
        return self.hours
    def __eq__(self, other):
        if isinstance(other, Job):
            return (self.name == other.name
                    and self.category == other.category
                    and self.rate == other.rate
                    and self.date == other.date
                    and self.hours == other.hours)
        return False
    def __hash__(self):
        return hash((self.name, self.category, self.rate, self.date, self.hours))
    def __str__(self):
        return f" name : {self.name} , category :{self.category}, rate : {self.rate}, date : {self.date}, hours : {self.hours}"
    def __repr__(self):
        return f" name : {self.name} , category :{self.category}, rate : {self.rate}, date : {self.date}, hours : {self.hours}"






