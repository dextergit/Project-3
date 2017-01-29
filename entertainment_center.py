import media
import fresh_tomatoes

# REFERENCES:

# http://stackoverflow.com/questions/14676265/how-to-read-text-file-into-a-list-or-array-with-python
# Udacity class + zip attachments

# toy_story1 = media.Movie("Toy Story", "Toys come to life.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=ZZv1vki4ou4")
# toy_story2 = media.Movie("Toy Story", "Toys come to life.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=ZZv1vki4ou4")
# toy_story3 = media.Movie("Toy Story", "Toys come to life.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=ZZv1vki4ou4")
#
#
# #print (toy_story.storyline)
# #toy_story.show_trailer()
# #print (toy_story.__name__)
# #print (media.Movie.__name__)
#
# movies = []
#
# movies.append(toy_story1)
# movies.append(toy_story2)
# movies.append(toy_story3)

# fresh_tomatoes.open_movies_page(movies)

#for movie in movies:
#	print movie.storyline


def get_movies(movie_file):
	movies_file = open(movie_file, 'r')
	movie_inputs = movies_file.readlines()
	movies = []

	for entry in movie_inputs:
		entry_columns = entry.split("|")
		title = entry_columns[0]
		story = entry_columns[1]
		image = entry_columns[2]
		trailer = entry_columns[3]

		movie_instance = media.Movie(title, story, image, trailer)
		movies.append(movie_instance)

	movies_file.close()
	return movies

fresh_tomatoes.open_movies_page(get_movies("movies.txt"))
