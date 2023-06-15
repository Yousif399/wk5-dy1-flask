from app import app

from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fav5')
def page():
    lis =[{'name' : 'yousif'},]
    favorite_art = ['1-Leonardo da vinci', '2-vermeer', '3-delacroix', '4-van gogh','5-edvard munch']
    favorite_sport = ['1-socer','2-tennis','3-chess','4-swimming','5-boxing']
    return render_template('fav5.html', artist_list = favorite_art, sport = favorite_sport)
    


