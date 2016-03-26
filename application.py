import random

from flask import Flask, jsonify

from dataservice import retrieve_movie_info                                                                        
from dataservice import retrieve_user_review_history
from recommenderM2M import calculate_top_5_movie

app = Flask(__name__)


@app.route('/healthcheck/')
def root():
    return '1'

@app.route('/recommend/movie/<string:movie_id>/')
def recommend_movies_from_movie(movie_id):
    if not movie_id.isdigit():
        return 'BAD_REQUEST', 400
    #we don't have any data now 
    #movie_info = retrieve_movie_info()
    #user_review_history = retrieve_user_review_history()
    #movies = calculate_top_5_movie(movie_id, user_review_history.values())
    movies = random.sample(['1292052', '1295644', '1292720', '1291546', '1292063', '1295124','1295161'], 5)
    return_value = {'movies': movies}
    return jsonify(**return_value), 200

if __name__ == '__main__':
    app.debug = True
    app.run()
