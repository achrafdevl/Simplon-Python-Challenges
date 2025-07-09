from database import setup_database
from queries import requetes
from insert_data import insert_data

if __name__ == "__main__":
    setup_database()      
    # insert_data()         # Commenté pour éviter les erreurs de doublons
    requetes()            
