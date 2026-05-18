database = {
    1: "Pranav",
    2: "Ayush",
    3: "Sahil"
}

def get_user_from_db(user_id):
    return database.get(user_id)