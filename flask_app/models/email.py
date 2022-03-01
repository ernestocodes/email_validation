from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.email = db_data['email']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        
    @classmethod
    def save_email(cls,data):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        return connectToMySQL('email_schema').query_db(query,data)

    @classmethod
    def show_emails(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('email_schema').query_db(query)
        emails = []
        for email in results:
            emails.append( cls(email) )
        return emails

    # attempted to make website display last email input
    # @classmethod
    # def get_last_survey(cls):
    #     query = "SELECT * FROM emails ORDER BY emails.id DESC LIMIT 1;"
    #     results = connectToMySQL('emails_schema').query_db(query)
    #     return f"Email(results[0])"

    @staticmethod
    def validate_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid
            
