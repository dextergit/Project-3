import media
import fresh_tomatoes

# References
# http://stackoverflow.com/questions/14676265/how-to-read-text-file-into-a-list-or-array-with-python
# Udacity class content, including videos, attachment, etc.
# YouTube (for trailers)
# Wikipedia (for images)

# >> Function - Gets a list of movies from a file, creates instances of the Movie object, and returns an array of Movie instances.
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
