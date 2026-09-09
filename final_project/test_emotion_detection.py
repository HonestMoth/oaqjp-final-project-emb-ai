from EmotionDetection import emotion_detector


def test_joy():
    """Test that the dominant emotion is joy."""
    result = emotion_detector("I am glad this happened")
    assert result["dominant_emotion"] == "joy"


def test_anger():
    """Test that the dominant emotion is anger."""
    result = emotion_detector("I am really mad about this")
    assert result["dominant_emotion"] == "anger"


def test_disgust():
    """Test that the dominant emotion is disgust."""
    result = emotion_detector("I feel disgusted just hearing about this")
    assert result["dominant_emotion"] == "disgust"


def test_sadness():
    """Test that the dominant emotion is sadness."""
    result = emotion_detector("I am so sad about this")
    assert result["dominant_emotion"] == "sadness"


def test_fear():
    """Test that the dominant emotion is fear."""
    result = emotion_detector("I am really afraid that this will happen")
    assert result["dominant_emotion"] == "fear"