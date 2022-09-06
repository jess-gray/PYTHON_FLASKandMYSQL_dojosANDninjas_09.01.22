from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.owner = None

    @classmethod #this is to add a new ninjas
    def create(cls,data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);'
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        print(results)
        return results
    
    @classmethod #this is to delete user
    def delete(cls, data):
        query = 'DELETE FROM ninjas WHERE id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        print(results)
        return results
    
    @classmethod #this is get one ninjas info (for editing)
    def get_one(cls, data):
        query = 'SELECT * FROM ninjas WHERE id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        print(results)
        return cls(results[0])

    @classmethod #this is to actually edit the user
    def update(cls, data):
        query = 'UPDATE ninjas set first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        print(results)
        return results