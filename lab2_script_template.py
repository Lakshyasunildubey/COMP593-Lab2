def main():
     # TODO: Step 2 - Create a complex data structure
    student_profile = {
        "full_name": "Lakshya Sunil Dubey",
        "student_id": 10331244,
        "pizza_toppings": ["PICKLED GINGER", "MINCED MUTTON", "PANEER"],
        "movies": [
            {"title": "Baahubali:The Beginning",
            "genre": "Epic Fantasy"},
            {"title": "Rangasthalam",
            "genre": "Drama"}
        ]}

   

    # TODO: Step 3 - Add another movie to the data structure
    student_profile["movies"].append({"title": "KGF: chapter 2","genre": "Action"})

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(data):
    full_name = data["full_name"]
    first_name = full_name.split()[0]
    student_id = data["student_id"]
    print(f"My name is {full_name}, but you can call me Sir {first_name}.")
    print(f"My student ID is {student_id}.")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(data, toppings):
    data["pizza_toppings"].extend(toppings)
    data["pizza_toppings"] = sorted([topping.lower() for topping in data["pizza_toppings"]])
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()