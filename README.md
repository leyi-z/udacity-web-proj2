## API Reference



### Getting Started

#### Database Info

The local database I used was named `db_proj2` with owner `leyi_psql` and no password. You might want to adjust the `models.py` file for the project to run on your computer. If you want to use the `trivia.psql` file to populate the database, make sure to change the owner in it.


#### NPM Stuff

The frontend is run with npm. The `node_modules` file is needed, but I did not include it in the git repository since it's a huge file. In order to run the frontend, you wiil need to run the following command in the frontend directory:
```
$ npm install
```
Then run the frontend with
```
$ npm start
```


### Error Handling

Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 404,
    "message": "Not found"
}
```
The API will return four error types when requests fail:
- 400: Bad Request
- 404: Not found
- 405: Method not allowed
- 422: Unable to process 



### Endpoints

#### GET `/`, `/add`, `/play`

- These are placeholder endpoints that will return an empty JSON object
- Sample: `curl http://127.0.0.1:5000/add`


#### GET `/categories`

- Returns the success value and a list of all categories, including their ids and types
- Sample: `curl http://127.0.0.1:5000/categories` which will return
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
}
```


#### GET `/questions`

- Returns the success value, a list of all categories, a paginated list of questions, and the total number of questions
- The question list is paginated in groups of 10; page number starts by default at 1
- Sample: `curl http://127.0.0.1:5000/questions?page=2` which will return
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "questions": [
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }, 
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "Scarab", 
      "category": 4, 
      "difficulty": 4, 
      "id": 23, 
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ], 
  "success": true, 
  "total_questions": 19
}
```


#### GET `/categories/{category_id}`

- Returns the success value, a list of all categories, a paginated list of questions that are in the category of the given id, and the total number of questions in this category
- The question list is paginated in groups of 10; page number starts at 1
- Sample: `curl http://127.0.0.1:5000/categories/2` which will return
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": {
    "2": "Art"
  }, 
  "questions": [
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ], 
  "success": true, 
  "total_questions": 4
}
```


#### DELETE `/questions/{question_id}`

- Removes the success value and the question of the given id from the database; returns a paginated list of questions and the total number of questions after the deletion
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/20?page=2` which will remove the question of id 20 and return
```
{
  "id": 20, 
  "questions": [
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "Scarab", 
      "category": 4, 
      "difficulty": 4, 
      "id": 23, 
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ], 
  "success": true, 
  "total_questions": 18
}
```


#### POST `/questions`

- Adds a new question to the database using the provided question, answer, difficulty and category; returns the success value and the id of the newly added question
- Sample: `curl -X POST -H "Content-Type: application/json" -d '{"question": "This is a sample question", "answer": "This is the answer", "difficulty": "2", "category": "4"}' http://127.0.0.1:5000/questions` which will add the provided question into the database, and return
```
{
  "id": 24, 
  "success": true
}
```



#### POST `/questions/search_result`

- Returns the success value, a paginated list of all questions for whom the privided search input is a substring of the question, and the total number of questions that qualify as the seach result
- The question list is paginated in groups of 10; page number starts at 1
- Sample: `curl -X POST -H "Content-Type: application/json" -d '{"searchTerm":"Who"}' http://127.0.0.1:5000/questions/search_result` which will return
```
{
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }
  ], 
  "search_input": "Who", 
  "success": true, 
  "total_questions": 3
}
```


#### POST  `/quizzes`

- Depending on the provided value of previous questions and quiz category, there are two possible outcomes:
	- If the length of the previous questions list is smaller than the number of questions in the given quiz category, then the endpoint will return the success value, a 'false' force end value, the previous questions list, and a randomly selected question from the given category that is not already in the previous questions list
	- Otherwise, the endpoint will only return the success value, a 'true' force end value, and the previous questions list
- Sample: `curl -X POST -H "Content-Type: application/json" -d '{"previous_questions": [16, 17], "quiz_category": {"id": "2"}}' http://127.0.0.1:5000/quizzes` which will return a random question that is in category of id 2 and is not in previous questions list, assuming the category contains more than two questions:
```
{
  "forceEnd": false, 
  "previousQuestions": [
    16, 
    17
  ], 
  "question": {
    "answer": "Jackson Pollock", 
    "category": 2, 
    "difficulty": 2, 
    "id": 19, 
    "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
  }, 
  "success": true
}
```













