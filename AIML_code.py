import pandas as pd

# Loading the dataset
dataset = pd.read_csv('/content/drive/MyDrive/imdb_top_1000.csv')
def recommend_movies(filters):
    # Applying filters to the datasetn
    filtered_data = dataset.copy()

    for filter_name, filter_value in filters.items():
        if filter_name == 'Movie name':
            filtered_data = filtered_data[filtered_data['Series_Title'].str.contains(filter_value, case=False)]
        elif filter_name == 'Genre':
            filtered_data = filtered_data[filtered_data['Genre'].str.contains(filter_value, case=False)]
        elif filter_name == 'Release year':
            filtered_data = filtered_data[filtered_data['Released_Year'] == int(filter_value)]
        elif filter_name == 'Director':
            filtered_data = filtered_data[filtered_data['Director'].str.contains(filter_value, case=False)]
        elif filter_name == 'Cast members':
            filtered_data = filtered_data[
                (filtered_data['Star1'].str.contains(filter_value, case=False)) |
                (filtered_data['Star2'].str.contains(filter_value, case=False)) |
                (filtered_data['Star3'].str.contains(filter_value, case=False)) |
                (filtered_data['Star4'].str.contains(filter_value, case=False))
            ]

    # Sorting the filtered data by IMDB rating and number of votes in descending order
    sorted_data = filtered_data.sort_values(by=['IMDB_Rating', 'No_of_Votes'], ascending=False)

    # Extracting the movie details for recommendation
    recommendations = sorted_data[['Series_Title', 'Genre', 'Released_Year', 'Director', 'Star1', 'Star2', 'Star3', 'Star4', 'IMDB_Rating', 'No_of_Votes']]

    return recommendations

# Getting user input for filters
filters = {}
print("Welcome to the Movie Recommendation System!")
print("Please select at least one filter from the following options:")
print("1. Movie name")
print("2. Genre")
print("3. Release year")
print("4. Director")
print("5. Cast members")
print()

while True:
    filter_option = int(input("Enter the filter option (1-5): "))
    if filter_option < 1 or filter_option > 5:
        print("Invalid filter option. Please try again.")
    else:
        filter_name = ""
        if filter_option == 1:
            filter_name = "Movie name"
        elif filter_option == 2:
            filter_name = "Genre"
        elif filter_option == 3:
            filter_name = "Release year"
        elif filter_option == 4:
            filter_name = "Director"
        elif filter_option == 5:
            filter_name = "Cast members"
        filter_value = input("Enter your preference for {}: ".format(filter_name))
        filters[filter_name] = filter_value

    continue_input = input("Do you want to add more filters? (yes/no): ")
    if continue_input.lower() == 'no':
        break

# Getting movie recommendations based on the selected filters
recommendations = recommend_movies(filters)
print("----------------------------------------------------------------------------------------------------------------------")
# Displaying the recommendations
print()
if len(recommendations) > 0:
    print("Movie recommendations:")
    print(recommendations.to_string(index=False))
else:
    print("No movies found based on the selected filters.")
import pandas as pd

# Loading the dataset
dataset = pd.read_csv('/content/drive/MyDrive/imdb_top_1000.csv')
def recommend_movies(filters):
    # Applying filters to the dataset
    filtered_data = dataset.copy()

    for filter_name, filter_value in filters.items():
        if filter_name == 'Movie name':
            filtered_data = filtered_data[filtered_data['Series_Title'].str.contains(filter_value, case=False)]
        elif filter_name == 'Genre':
            filtered_data = filtered_data[filtered_data['Genre'].str.contains(filter_value, case=False)]
        elif filter_name == 'Release year':
            filtered_data = filtered_data[filtered_data['Released_Year'] == int(filter_value)]
        elif filter_name == 'Director':
            filtered_data = filtered_data[filtered_data['Director'].str.contains(filter_value, case=False)]
        elif filter_name == 'Cast members':
            filtered_data = filtered_data[
                (filtered_data['Star1'].str.contains(filter_value, case=False)) |
                (filtered_data['Star2'].str.contains(filter_value, case=False)) |
                (filtered_data['Star3'].str.contains(filter_value, case=False)) |
                (filtered_data['Star4'].str.contains(filter_value, case=False))
            ]

    # Sorting the filtered data by IMDB rating and number of votes in descending order
    sorted_data = filtered_data.sort_values(by=['IMDB_Rating', 'No_of_Votes'], ascending=False)

    # Extracting the movie details for recommendation
    recommendations = sorted_data[['Series_Title', 'Genre', 'Released_Year', 'Director', 'Star1', 'Star2', 'Star3', 'Star4', 'IMDB_Rating', 'No_of_Votes']]

    return recommendations

# Getting user input for filters
filters = {}
print("-------------------------------------------------------------------------------------------------------")
print("Welcome to the Movie Recommendation System!")
print("Please select at least one filter from the following options:")
print("1. Movie name")
print("2. Genre")
print("3. Release year")
print("4. Director")
print("5. Cast members")
print()

while True:
    filter_option = int(input("Enter the filter option (1-5): "))
    if filter_option < 1 or filter_option > 5:
        print("Invalid filter option. Please try again.")
    else:
        filter_name = ""
        if filter_option == 1:
            filter_name = "Movie name"
        elif filter_option == 2:
            filter_name = "Genre"
        elif filter_option == 3:
            filter_name = "Release year"
        elif filter_option == 4:
            filter_name = "Director"
        elif filter_option == 5:
            filter_name = "Cast members"
        filter_value = input("Enter your preference for {}: ".format(filter_name))
        filters[filter_name] = filter_value

    continue_input = input("Do you want to add more filters? (yes/no): ")
    if continue_input.lower() == 'no':
        break

# Getting movie recommendations based on the selected filters
recommendations = recommend_movies(filters)
print("----------------------------------------------------------------------------------------------------------------------")
# Displaying the recommendations
print()
if len(recommendations) > 0:
    print("Movie recommendations:")
    print(recommendations.to_string(index=False))
else:
    print("No movies found based on the selected filters.")