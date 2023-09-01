![architecture](https://github.com/jainammshahh/Movie_Recommendation_System/assets/114266749/49eff172-abd6-4802-96d2-9e94fcd36a42)# Content-Based-Movie-Recommender-System-with-sentiment-analysis-using-AJAX


Content Based Recommender System recommends movies similar to the movie user likes and analyses the sentiments on the reviews given by the user for that movie. 

The details of the movies(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api, and using the IMDB id of the movie in the API, I did web scraping to get the reviews given by the user in the IMDB site using `beautifulsoup4` and performed sentiment analysis on those reviews.

Link to youtube demo: https://www.youtube.com/watch?v=dhVePtyECFw

## The Movie Cinema

I've developed a similar application called "The Movie Cinema" which supports all language movies. But the only thing that differs from this application is that I've used the TMDB's recommendation engine in "The Movie Cinema". The recommendation part developed by me in this application doesn't support for multi-language movies as it consumes 200% of RAM (even after deploying it to Heroku) for generating Count Vectorizer matrix for all the 700,000+ movies in the TMDB. 

Link to "The Movie Cinema" application: https://tmc.kishanlal.dev/

Don't worry if the movie that you are looking for is not auto-suggested. Just type the movie name and click on "enter". You will be good to go eventhough if you made some typo errors.

Source Code: https://github.com/kishan0725/The-Movie-Cinema



## How to get the API key?

Create an account in https://www.themoviedb.org/, click on the `API` link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your `API` sidebar once your request is approved.

## How to run the project?

1. Clone or download this repository to your local machine.

2. Install all the libraries mentioned in the requirements.txt file with the command `pip install -r requirements.txt`

3. Get your API key from https://www.themoviedb.org/. (Refer the above section on how to get the API key) 

4. Replace YOUR_API_KEY in **both** the places (line no. 15 and 29) of `static/recommend.js` file and hit save.

5. Open your terminal/command prompt from your project directory and run the file `main.py` by executing the command `python main.py`.

6. Go to your browser and type `http://127.0.0.1:5000/` in the address bar.

7. Hurray! That's it.

## Architecture
<img width="870" alt="Screenshot 2023-08-31 at 11 17 04 PM" src="https://github.com/jainammshahh/Movie_Recommendation_System/assets/114266749/5d18df24-4587-46ea-8d8a-5f1a4cd083ca">


### Measuring Similarity:

But how does the system ascertain the most akin item to the user's preference? This is where similarity scores step in.

A similarity score is a numerical metric that falls within the range of zero to one, aiding in the assessment of how closely two items resemble each other on a scale. This score is derived by gauging the resemblance between the textual attributes of both items. Essentially, the similarity score quantifies how alike the textual details of two items are. This process is achieved through the utilization of cosine similarity.

### How Cosine Similarity works?

Cosine similarity serves as a metric to gauge document similarity, disregarding their size. Mathematically, it quantifies the cosine of the angle between two vectors projected within a multi-dimensional space. This approach is beneficial because it accommodates situations where two akin documents might be distant in terms of Euclidean distance (owing to document size), yet retain a close orientation. A smaller angle signifies greater cosine similarity.

![70401457-a7530680-1a55-11ea-9158-97d4e8515ca4](https://github.com/jainammshahh/Movie_Recommendation_System/assets/114266749/ab55d273-672a-4c08-b6bd-f337493a75f3)

More about Cosine Similarity : [Understanding the Math behind Cosine Similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/)

### Sources of the datasets

1. [The Movies Database](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)  

3. [List of movies in 2018](https://en.wikipedia.org/wiki/List_of_American_films_of_2018)

4. [List of movies in 2019](https://en.wikipedia.org/wiki/List_of_American_films_of_2019)
   
5. [List of movies in 2020](https://en.wikipedia.org/wiki/List_of_American_films_of_2020)
