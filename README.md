# Content-Based-Movie-Recommender-System-with-sentiment-analysis-using-AJAX
![Uploading 68747470733a2f2f696d672e736869656c64<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="76" height="20" role="img" aria-label="Python: 3.8"><title>Python: 3.8</title><linearGradient id="s" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><clipPath id="r"><rect width="76" height="20" rx="3" fill="#fff"/></clipPath><g clip-path="url(#r)"><rect width="49" height="20" fill="#555"/><rect x="49" width="27" height="20" fill="blueviolet"/><rect width="76" height="20" fill="url(#s)"/></g><g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110"><text aria-hidden="true" x="255" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="390">Python</text><text x="255" y="140" transform="scale(.1)" fill="#fff" textLength="390">Python</text><text aria-hidden="true" x="615" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="170">3.8</text><text x="615" y="140" transform="scale(.1)" fill="#fff" textLength="170">3.8</text></g></svg>732e696f2f62616467652f507974686f6e2d332e382d626c756576696f6c6574.svg…]()


The Content-Based Recommender System suggests movies that share similarities with the user's preferred movie, alongside an examination of the sentiments expressed in the user's reviews for that particular film.

To acquire movie specifics such as title, genre, runtime, rating, poster, and more, an API provided by TMDB is utilized (https://www.themoviedb.org/documentation/api). By leveraging the movie's IMDB ID within the API, web scraping techniques are employed to extract user reviews from the IMDB site using the beautifulsoup4 library. Subsequently, a sentiment analysis process is applied to these collected reviews, shedding light on the emotional tones associated with them.

Link to demo: https://www.linkedin.com/posts/jainammshahh_movierecommendation-webapplication-techinnovation-activity-7086414544478072832-JXH7?utm_source=share&utm_medium=member_desktop

## The Movie Cinema

A web application has been crafted offering comprehensive support for movies spanning various languages. However, a notable distinction between this application and the one you described is that I've harnessed the recommendation engine provided by TMDB within "The Movie Cinema."

In this application, the recommendation component I've developed lacks compatibility with multi-language films. This limitation stems from resource constraints, as generating the Count Vectorizer matrix for over 700,000 movies from TMDB strains system memory, even after deploying it on Heroku.

If you find that the movie you're seeking isn't automatically suggested, there's no need for concern. You can simply input the movie's name and press "enter." This approach ensures a seamless experience, even if you've made slight typing errors.

Source Code: https://github.com/jainammshahh/Movie_Recommendation_System



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
<img width="771" alt="Screenshot 2023-08-31 at 11 18 11 PM" src="https://github.com/jainammshahh/Movie_Recommendation_System/assets/114266749/a47b6573-fade-448e-bcbb-301aaef534bd">


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
