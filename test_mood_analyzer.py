'''
 !!! NOT part of the project, I just added myself to test the functions in mood_analyzer.py

'''

from mood_analyzer import MoodAnalyzer


analyzer = MoodAnalyzer()

#1 test preprocess
def test_happy():
    happy_tokens = analyzer.preprocess("I am happy.")
    assert happy_tokens == ["i", "am", "happy"], f"Expected ['i', 'am', 'happy'], but got {happy_tokens}"

def test_negation():
    negation_tokens = analyzer.preprocess("I am not happy.")
    assert negation_tokens == ["i", "am", "not_happy"], f"Expected ['i', 'am', 'not_happy'], but got {negation_tokens}"

#2 test score_text
def test_happy_score():
    happy_score = analyzer.score_text("I am happy.")
    assert happy_score > 0, f"Expected positive score for 'I am happy.', but got {happy_score}"

def test_sad_score():
    sad_score = analyzer.score_text("I am sad.")
    assert sad_score < 0, f"Expected negative score for 'I am sad.', but got {sad_score}"

def test_neutral_score():
    neutral_score = analyzer.score_text("I am neutral.")
    assert neutral_score == 0, f"Expected zero score for 'I am neutral.', but got {neutral_score}"

#3. Test predict_label
def test_predict_label_positive():
    label = analyzer.predict_label("I am happy.")
    assert label == "positive", f"Expected 'positive' for 'I am happy.', but got {label}"

def test_predict_label_negative():
    label = analyzer.predict_label("I am sad.")
    assert label == "negative", f"Expected 'negative' for 'I am sad.', but got {label}"

def test_predict_label_neutral():
    label = analyzer.predict_label("I am neutral.")
    assert label == "neutral", f"Expected 'neutral' for 'I am neutral.', but got {label}"