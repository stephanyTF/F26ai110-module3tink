# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

You may complete this model card for whichever version you used, or compare both if you explored them.

## 1. Model Overview

**Model type:**  
I used the rule based model only

**Intended purpose:**  
Classify short text messages as moods like positive, negative, neutral, or mixed.

**How it works (brief):**  
- Positive words increment score by 3
- Negative words decrement score by 3  
- Negation rules  
- Sarcasm  
- Threshold decisions for labels in scoring:
    - Positive: score > 3
    - Negative: score < -3
    - Neutral: score = 0
    - Mixed: -2 <= score <= 2
    - Sarcastic: score > 3 and sarcastic if flagged true



## 2. Data

**Dataset description:**  
Summarize how many posts are in `SAMPLE_POSTS` and how you added new ones.
13 posts are in `SAMPLE_POSTS` and I added new ones based on topics that haven't been covered yet and introduces complexity (ex: have positive and negative words)

**Labeling process:**  
I used a rigid ruling structure and conditional flags to mark certain cases such as negation or sarcasm that contribute to hte label scoring. 

**Important characteristics of your dataset:**  

- Some posts express mixed feelings  
- Contains short or ambiguous messages

**Possible issues with the dataset:**  
- Unable to add emojis so unable to test how model will perform with emoji embedded messages
- sentences are short and straightforward

## 3. How the Rule Based Model Works (if used)

**Your scoring rules:**  
Describe the modeling choices you made.  
Examples:  

- I love this class so much -> positive
- Today was a terrible day -> negative
- I love traffic -> sarcastic


**Strengths of this approach:**  
It's easy to define the rules and set up

**Weaknesses of this approach:**  
Rules are rigid and may not capture ambiguous or complex sentences accurately.

## 4. How the ML Model Works (if used)

**Features used:**  
Describe the representation.  
Example: “Bag of words using CountVectorizer.”

**Training data:**  
State that the model trained on `SAMPLE_POSTS` and `TRUE_LABELS`.

**Training behavior:**  
Did you observe changes in accuracy when you added more examples or changed labels?

**Strengths and weaknesses:**  
Strengths might include learning patterns automatically.  
Weaknesses might include overfitting to the training data or picking up spurious cues.

## 5. Evaluation

**How you evaluated the model:**  
Both versions can be evaluated on the labeled posts in `dataset.py`.  
Describe what accuracy you observed.

**Examples of correct predictions:**  
Provide 2 or 3 examples and explain why they were correct.

**Examples of incorrect predictions:**  
Provide 2 or 3 examples and explain why the model made a mistake.  
If you used both models, show how their failures differed.

## 6. Limitations

Describe the most important limitations.  
Examples:  

- The dataset is small  
- The model does not generalize to longer posts  
- It cannot detect sarcasm reliably  
- It depends heavily on the words you chose or labeled

## 7. Ethical Considerations

Discuss any potential impacts of using mood detection in real applications.  
Examples: 

- Misclassifying a message expressing distress  
- Misinterpreting mood for certain language communities  
- Privacy considerations if analyzing personal messages

## 8. Ideas for Improvement

List ways to improve either model.  
Possible directions:  

- Add more labeled data  
- Use TF IDF instead of CountVectorizer  
- Add better preprocessing for emojis or slang  
- Use a small neural network or transformer model  
- Improve the rule based scoring method  
- Add a real test set instead of training accuracy only
