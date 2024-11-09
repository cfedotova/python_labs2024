from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('example.db', check_same_thread=False)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS movies
             (id INTEGER PRIMARY KEY, title TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS user_movie
             (user_id INTEGER, movie_id INTEGER, 
              PRIMARY KEY (user_id, movie_id),
              FOREIGN KEY (user_id) REFERENCES users(id),
              FOREIGN KEY (movie_id) REFERENCES movies(id))''')
conn.commit()


@app.route('/users', methods=['GET'])
def get_users():
    c.execute("""
        SELECT users.id, users.name, age.age, GROUP_CONCAT(movies.title) AS favorite_movies 
        FROM users
        JOIN age ON users.id = age.user_id
        LEFT JOIN user_movie ON users.id = user_movie.user_id 
        LEFT JOIN movies ON user_movie.movie_id = movies.id 
        GROUP BY users.id
    """)
    users = [{'id': row[0], 'name': row[1], 'age': row[2], 'favorite_movies': row[3].split(',') if row[3] else []} for
             row
             in c.fetchall()]
    return jsonify(users)


@app.route('/users/add_user', methods=['GET'])
def create_user():
    name = request.args.get('name')
    age = request.args.get('age')
    c.execute("INSERT INTO users (name)  VALUES (?)", (name,))
    user_id = c.lastrowid
    c.execute("INSERT INTO age (age, user_id) VALUES (?, ?)", (age, user_id))

    conn.commit()

    return jsonify({'id': user_id, 'name': name, 'age': age})


@app.route('/movies/add', methods=['GET'])
def create_movie():
    title = request.args.get('title')
    c.execute("INSERT INTO movies (title)  VALUES (?)", (title,))
    movie_id = c.lastrowid

    conn.commit()

    return jsonify({'id': movie_id, 'title': title})


@app.route('/users/assign_movies/<int:user_id>/<int:movie_id>', methods=['GET'])
def assign_movies(user_id, movie_id):
    c.execute("INSERT INTO user_movie (user_id, movie_id)  VALUES (?, ?)", (user_id, movie_id))

    conn.commit()

    return 'ok'


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    c.execute("""SELECT users.id, users.name, age.age, GROUP_CONCAT(movies.title) AS favorite_movies
              FROM users 
              JOIN age ON users.id = age.user_id
              LEFT JOIN user_movie ON users.id = user_movie.user_id
              LEFT JOIN movies ON user_movie.movie_id = movies.id
              WHERE users.id = ?
              """, (user_id,))

    user = c.fetchone()

    if user:
        return jsonify(
            {'id': user[0], 'name': user[1], 'age': user[2], 'favorite_movies': user[3].split(',')})
    else:
        return jsonify({'error': 'User not found'}), 404


@app.route('/users/delete/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    try:
        c.execute("SELECT id FROM users WHERE id = ?", (user_id,))
        if not c.fetchone():
            return jsonify({'error': 'User not found'}), 404
        c.execute("BEGIN TRANSACTION")
        c.execute("DELETE FROM user_movie WHERE user_id = ?", (user_id,))
        c.execute("DELETE FROM users WHERE id = ?", (user_id,))
        c.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        return jsonify({'message': f'User {user_id} and related records successfully deleted'}), 200
    except sqlite3.Error as e:
        conn.rollback()
        return jsonify({'error': f'Database error: {str(e)}'}), 500


@app.route('/movies/delete/<int:movie_id>', methods=['GET'])
def delete_movie(movie_id):
    try:
        c.execute("SELECT id FROM movies WHERE id = ?", (movie_id,))
        if not c.fetchone():
            return jsonify({'error': 'Movie not found'}), 404
        c.execute("DELETE FROM movies WHERE id=?", (movie_id,))
        conn.commit()
        return jsonify({'message': f'Movie {movie_id} successfully deleted'}), 200
    except sqlite3.Error as e:
        conn.rollback()
        return jsonify({'error': f'Database error: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True)
