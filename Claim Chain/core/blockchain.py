import datetime,hashlib
from .models import *

class Block:

    def __init__(self,previous_hash,model):
        self.previous_hash = previous_hash
        self.data = model

        self.timestrap = str(datetime.datetime.now())
        self.string_data = self.get_strap()
        self.new_hash = self.generate_hash()
    
    def get_strap(self):
        opp = str(self.data['id'])+self.data['name'] + self.data['adhar'] + self.previous_hash + self.timestrap
        setrap = '-'.join(opp)
        return setrap
    
    def generate_hash(self):
        hash = hashlib.sha256(self.string_data.encode()).hexdigest()

        return hash
