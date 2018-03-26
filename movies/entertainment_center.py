import media
import fresh_tomatoes

""" This module serves as a landing page for selected movies"""


# constructing movies
toy_story = media.Movie("Toy Story","A boy and his toys that come to life","https://images-na.ssl-images-amazon.com/images/I/91g2fEXursL._RI_SX200_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

u_turn = media.Movie("U Turn", "A story about what happens when people take a specific UTurn","https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/5cef3349158839.58aca1d84f0e1.jpg"
,"https://www.youtube.com/watch?v=Kdh5P8dtMXA")

udaan = media.Movie("Udaan", "THe story of a boy escaping abuse and chasing his dreams","https://ia.media-imdb.com/images/M/MV5BNzgxMzExMzUwNV5BMl5BanBnXkFtZTcwMDc2MjUwNA@@._V1_UY268_CR1,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=wEJxe2bE-cE")

cowspiracy = media.Movie("Cowspiracy","How Meat consumption is harming the planet","https://static1.squarespace.com/static/544dc5a1e4b07e8995e3effa/t/545175e3e4b0244829843c27/1414624744519/cowspiracy_cow.jpg?format=750w","https://www.youtube.com/watch?v=nV04zyfLyN4")

into_the_wild = media.Movie("Into the wild","A person's rejection of the material world","https://ia.media-imdb.com/images/M/MV5BMTAwNDEyODU1MjheQTJeQWpwZ15BbWU2MDc3NDQwNw@@._V1_UX182_CR0,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=g7ArZ7VD-QQ")

ondu_motteya_kathe = media.Movie("Ondu motteya kathe","Story of a bald person and his struggles to get married","https://c.saavncdn.com/899/Ondu-Motteya-Kathe-Kannada-2017-500x500.jpg","https://www.youtube.com/watch?v=UXv-9QdR3s8")

# populating the set of movies to show on the landing page
movies = [toy_story,udaan,u_turn,cowspiracy,into_the_wild,ondu_motteya_kathe]

# populate the landing page and open
fresh_tomatoes.open_movies_page(movies)

