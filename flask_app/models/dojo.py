from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,data): #the left is table columns (attributes)from my database
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod #this is to show all the dojos
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        print(results)
        all_dojos = []
        for one_dojo in results:
            all_dojos.append(cls(one_dojo))
        return all_dojos
    
    @classmethod #this is to add a new dojo
    def create(cls,data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        print(results)
        return results