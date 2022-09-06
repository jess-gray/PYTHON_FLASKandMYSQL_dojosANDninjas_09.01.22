from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self,data): #the left is table columns (attributes)from my database
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
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

    @classmethod #this is to show all the ninjas under one dojo
    def get_dojo_ninjas(cls, data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        print(results)
        one_dojo = cls(results[0])
        for one_ninja in results:
            data = {
                'id': one_ninja['ninjas.id'],
                'first_name' : one_ninja['first_name'],
                'last_name' : one_ninja['last_name'],
                'age': one_ninja['age'],
                'created_at' : one_ninja['ninjas.created_at'],
                'updated_at' : one_ninja['ninjas.updated_at']
            }
            ninja_obj = ninja.Ninja(data)
            one_dojo.ninjas.append(ninja_obj)
        return one_dojo

        #keep getting tuple out of range 