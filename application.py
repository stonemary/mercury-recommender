from flask import Flask

from dataservice import retrieve_movie_info                                                                        
from dataservice import retrieve_user_review_history
from dataservice import update_movie_recommend
from recommenderM2M import calculate_top_5_movie

app = Flask(__name__)


@app.route('/')
def root():
    return '1'

@app.route('/recommend/movie/<string:movie_id>/')
def recommend_movies_from_movie(movie_id):
    if not movie_id.is_digit():
        return 'BAD_REQUEST', 400
    
    movie_info = retrieve_movie_info()
    user_review_history = retrieve_user_review_history()
    movies = calculate_top_5_movie(movie, user_review_history.values())
    return_value = {'movies': movies}
    return flask.jsonfy(**return_value), 200

if __name__ == '__main__':
    app.debug = True
    app.run()
