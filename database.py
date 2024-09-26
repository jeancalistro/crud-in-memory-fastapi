from models import Entity

class DB_SYSTEM():
    def __init__(self):
        self.entity_table : list[Entity] = []
        self.count : int = 0

    def get_entities(self):
        return self.entity_table
    
    def get_entity_by_id(self, id : int):
        left : int = 0
        right : int = len(self.entity_table) - 1
        count : int = 0
        entity : Entity = None

        while count <= len(self.entity_table):
            mid_of_registers : int = int(left + (right - left) / 2)

            if(right >= left):
                entity = self.entity_table[mid_of_registers]
                if(entity.id == id):
                    return entity
                elif(entity.id < id):
                    left = mid_of_registers + 1
                elif(entity.id > id):
                    right = mid_of_registers - 1
            else: 
                break

    def new_data(self, entity : Entity):
        entity.id = self.get_count() + 1
        self.entity_table.append(entity)
        self.increment_count()
    
    def get_count(self):
        return self.count

    def increment_count(self):
        self.count += 1