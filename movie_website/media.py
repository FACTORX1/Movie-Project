class Movie():
    

    # Initialize instance of class Movie
    def __init__(self, movie_title, poster_image, trailer_youtube,
                 movie_storyline, movie_rating):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.storyline = movie_storyline
        self.rating_image_url = movie_rating