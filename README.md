# 🎬 Movie recommendation system and chatbot team project
### 📆 March 16, 2020 - June 6, 2020
## 👨‍👩‍👧‍👧 What we did
- Crawling movie data

    <img src="https://img.shields.io/badge/IMDb-E6B91E?style=flat-square&logo=IMDb&logoColor=black"/>
    <img src="https://img.shields.io/badge/TMDB-01D277?style=flat-square&logo=TheMovieDatabase&logoColor=white"/>
    <img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/>


    <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white"/>
    <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=NumPy&logoColor=white"/>
    <img src="https://img.shields.io/badge/Anaconda-44A833?style=flat-square&logo=Anaconda&logoColor=white"/>
    <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=Jupyter&logoColor=white"/>
- Recommendation system
    
    <img src="https://img.shields.io/badge/Tensorflow-FF6F00?style=flat-square&logo=TensorFlow&logoColor=white"/>
    <img src="https://img.shields.io/badge/Scikit learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=black"/>
    
- Build Chatbot

    <img src="https://img.shields.io/badge/Tensorflow-FF6F00?style=flat-square&logo=TensorFlow&logoColor=white"/>
    <img src="https://img.shields.io/badge/Keras-D00000?style=flat-square&logo=Keras&logoColor=white"/>
    <img src="https://img.shields.io/badge/CentOS-262577?style=flat-square&logo=CentOS&logoColor=white"/>
    <img src="https://img.shields.io/badge/Google Cloud-4285F4?style=flat-square&logo=Google-Cloud&logoColor=white"/>
    <img src="https://img.shields.io/badge/Google Colab-F9AB00?style=flat-square&logo=Google-Colab&logoColor=white"/>
    <img src="https://img.shields.io/badge/FileZilla-BF0000?style=flat-square&logo=FileZilla&logoColor=white"/>
    
- Server & Application

    <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"/>
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white"/>
    <img src="https://img.shields.io/badge/JS-F7DF1E?style=flat-square&logo=JavaScript&logoColor=black"/>
    <img src="https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=Ubuntu&logoColor=white"/>
    <img src="https://img.shields.io/badge/Jinja-B41717?style=flat-square&logo=Jinja&logoColor=white"/>
    <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=Flask&logoColor=white"/>


## 😎 What I did
- **Crawling movie data (WATCHA)**

    <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white"/>
    <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=NumPy&logoColor=white"/>
    <img src="https://img.shields.io/badge/Anaconda-44A833?style=flat-square&logo=Anaconda&logoColor=white"/>
    <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=Jupyter&logoColor=white"/>
    <img src="https://img.shields.io/badge/VSCode-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white"/>

- **Build chatbot**

    <img src="https://img.shields.io/badge/Tensorflow-FF6F00?style=flat-square&logo=TensorFlow&logoColor=white"/>
    <img src="https://img.shields.io/badge/Keras-D00000?style=flat-square&logo=Keras&logoColor=white"/>
    <img src="https://img.shields.io/badge/CentOS-262577?style=flat-square&logo=CentOS&logoColor=white"/>
    <img src="https://img.shields.io/badge/Google Cloud-4285F4?style=flat-square&logo=google-cloud&logoColor=white"/>
    <img src="https://img.shields.io/badge/Google Colab-F9AB00?style=flat-square&logo=google-colab&logoColor=white"/>
    <img src="https://img.shields.io/badge/FileZilla-BF0000?style=flat-square&logo=FileZilla&logoColor=white"/>


# 🤷‍♂️How did I make WATCHA crawler in python

## ❓ Why didn't I develop the crawler as a module?
Due to the characteristics of the crawler, we had to borrow computer resources from team members and ***ask them to operate the crawler.***

So instead of making repetitive functions or classes a module, we've made it easy for the team to crawl with **just one Jupyter Notebook.** 

This is why crawlers were not developed in modules.

---

## 🎯 I specially developed these more focused !!
### 👉 [**12. watcha_get_user_info.ipynb**](https://github.com/pyunji/MovieProject/blob/master/crawling/watcha_get_user_info.md)
### 👉 [**11. watcha_user_rating_count.ipynb**](https://github.com/pyunji/MovieProject/blob/master/crawling/watcha_user_rating_count.md) 

---

## 💻 In what order was it developed?
### [1. watcha_title_to_search.ipynb](https://github.com/pyunji/MovieProject/blob/master/crawling/watcha_title_to_search.md)
    - Used files:
		- kobis_movie_filtered.csv
		- tmdb_movie_filtered.csv
	- Generated files: 
		- test1.csv
	
Converted the *movie_Nm* column of *kobis* and the *title* column of *tmdb* to the *title_kor* column.

Data Frame converted from *kobis'* *Movie_NmEn* column and *tmdb's* *original_title* column to *title_en* column was saved as *test1.csv*

### [2. watcha_get_mv_code.ipynb](https://github.com/pyunji/MovieProject/blob/master/crawling/watcha_get_mv_code.md)
	- Used files: 
		- mv_titles\file00~89.csv
	- Generated files: 
		- movie_series_en\movie_series00~89.csv
		- movie_series_kor\movie_series00~89.csv

Searched the column of movie title in WATCHA and got WATCHA's own movie code and saved it.

### [3. watcha_all_mv_code.ipynb](https://github.com/pyunji/MovieProject/blob/master/crawling/watcha_all_mv_code.md)
    - Used files: 
        - movie_series_en\movie_series00~89.csv
        - movie_series_kor\movie_series00~89.csv
            
    - Generated files:
        - watcha_all_mv_code.csv	


After concatting with series containing only movie codes, it was saved to *watcha_all_mv_code.csv* 

It has a total of **129653** movie codes.

### [4. watcha_get_diff_code.ipynb](https://github.com/pyunji/MovieProject/blob/master/crawling/watcha_get_diff_code.md)
	- Used files: 
		- mv_detail\mv_detail00~62.csv 
            - files with losses.
			- 125641 of movie codes
		- watcha_all_movie_code.csv
			- 129653 of movie codes
	- Generated files:
		- diff.csv
            - loss-recovered file

It has restored *4,012* movie codes that were not included due to mistakes in distributing film codes.

### [5. watcha_get_mv_detail.ipynb](https://github.com/pyunji/MovieProject/blob/master/crawling/watcha_get_mv_detail.md)
	- Used files:
		- watcha_all_mv_code.csv
		- diff.csv
	- Generated files: 
		- mv_detail\mv_detail00~62.csv
            - files with losses.
		- mv_detail\mv_detail_diff.csv
            - loss-recovered file 

Enter the collected movie code into url to search for details of the movie.

Detailed information is as follows.

`'casual_title', 'original_title', 'country', 'production_year', 'genre', 'running_time', 'director', 'main_actor', 'supporting_actor', 'extra', 'cast', 'cameo_special', 'cameo_friendship', 'voice_actor', 'narration', 'mean_ratings', 'voter', 'ratings_0.5', 'ratings_1.0', 'ratings_1.5', 'ratings_2.0', 'ratings_2.5', 'ratings_3.0', 'ratings_3.5', 'ratings_4.0', 'ratings_4.5', 'ratings_5.0','story'`

### [6. watcha_concat_mv_detail.ipynb](https://github.com/pyunji/MovieProject/blob/master/crawling/watcha_concat_mv_detail.md)
	- Used files: 
		- mv_detail\*
	- Generated files: 
		- watcha_mv_detail_final.csv

After concatting all files used, the column names that were not needed were removed or changed to column names that were easy-to-read column names.

### [7. watcha_mv_detail_voter_tonumeric.ipynb](https://github.com/pyunji/MovieProject/blob/master/crawling/watcha_mv_detail_voter_tonumeric.md)
	- Used files: 
		- watcha_mv_detail_final.csv
	- Generated files: 
		- watcha_mv_code_filtered.csv
		- watcha_mv_detail_voter_tonumeric.csv

Movie with no one to rate a movie was saved separately in *watcha_mv_code_filtered.csv*.

A string representing a number, such as '~만, ~천' in the column, was converted to a number and saved as *watcha_mv_detail_voter_tonumeric.csv*

### [8. watcha_mv_code_sort_by_voter_final.ipynb](https://github.com/pyunji/MovieProject/blob/master/crawling/watcha_mv_code_sort_by_voter_final.md)
	- Used files: 
		- watcha_mv_detail_tonumeric.csv
	- Generated files: 
		- watcha_mv_code_sort_by_voter_final.csv

After sorting the number of voters in descending order, only the movie code was extracted and saved as *watcha_mv_code_sort_by_voter_final.csv*
It had 74,277 movie codes.

### [9. watcha_get_mv_review.ipynb](https://github.com/pyunji/MovieProject/blob/master/crawling/watcha_get_mv_review.md)
	- Used files: 
		- watcha_mv_code_sort_by_voter_final.csv
	- Generated files: 
		- mv_review\mv_review_before\mv_review0~75000.csv

When searching with film codes, the movie brought in all reviewers' IDs, nicknames, reviews, ratings, and likes numbers of reviews.

### [10. watcha_review_processing.ipynb](https://github.com/pyunji/MovieProject/blob/master/crawling/watcha_review_processing.md)
	- Used files:
		mv_review\mv_review_before\*
	- Generated files:
		- mv_review\mv_review_after\리뷰가 없는 영화들.csv
		- mv_review\mv_review_after\reviewed_mv.csv
		- mv_review\mv_review_after\user_id.csv 
            - #215260 -> #215448
		    - watcha_user/user_id.csv (changed path)
		

Stored user id of non-reviewable movies, reviewed movies, and reviewed separately.

These were all concatenated, deduplicated and stored.


### [**11. watcha_user_rating_count.ipynb**](https://github.com/pyunji/MovieProject/blob/master/crawling/watcha_user_rating_count.md)
	- Used files:
		- mv_review\mv_review_after\user_id.csv
		    - watcha_user\user_id.csv (changed path)
	- Generated files:
		- mv_review\mv_review_after\user_id_sort_by_rating_count.csv
		    - watcha_user\temp\user_id_sort_by_rating_count1~3.csv (changed path)

#### ❓ Why did I collect rating_count?
    Add the number of movies evaluated by the user to the *rating_count* column and sort them in descending order.

    Due to WATCHA's infinite scrolling characteristics, dynamic crawling was carried out using selenium.

    But due to delays between requests of scrolling down and the driver's response time, the next user's information was often crawled over without getting all user-specific data. 

    To overcome this, I decided to set specific guidelines even if I took extra time. 

    I was worried about the team members because there was not enough time for the project, but I persuaded them to come up with the best way not to waste time for a better quality recommendation system. 

    I thought the guideline could be the "number of movies evaluated by users(rating_count)" that showed when search user's profile. 

    This reduces time by collecting guidelines through static crawl because dynamic crawl is not required. 

    This allowed us to build an algorithm that would repeat the loop if the guideline and the data being collected differed by more than a certain number of times, and then move on to the next step if the loop was repeated more than a certain number of times. 

    Eventually, I created a complete crawler that went nonstop for two days, and they were able to collect about 89 million movies and stars that users evaluated.

### [**12. watcha_get_user_info.ipynb**](https://github.com/pyunji/MovieProject/blob/master/crawling/watcha_get_user_info.md)
	- Used files:
		- watcha_user/user_id_sort_by_rating_count_final.csv
	- Generated files:
		- watcha_user/temp2/user_data{numbering}-{numbering}.csv
		- watcha_user/temp3/error_user_data{numbering}-{numbering}.csv

Got as accurately as possible the movies and ratings user's rate based on *rating_count*.

The number of users who rated more than six movies was 207,793. 

In the case of users who re-run the loop more than 20 times, stored separately in another directory because thought to occur the error.