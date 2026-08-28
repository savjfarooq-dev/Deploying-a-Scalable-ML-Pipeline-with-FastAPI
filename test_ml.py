import pytest

# Add additional required imports
from ml.data import apply_label
from sklearn.ensemble import RandomForestClassifier
from ml.model import compute_model_metrics, train_model

# Implement first unit test.


def test_apply_label():
    """
    Test that apply_label returns the expected salary label.
    """
    prediction = [1]

    result = apply_label(prediction)

    assert result == ">50K"


# Implement second unit test.
def test_train_model():
    """
    Test that train_model returns a RandomForestClassifier.
    """
    X_train = [[1, 2], [2, 3], [3, 4], [4, 5]]
    y_train = [0, 0, 1, 1]

    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)


# Implement third unit test.
def test_compute_model_metrics():
    """
    Test that compute_model_metrics returns expected metric values.
    """
    y = [1, 1, 0, 0]
    preds = [1, 0, 0, 0]

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert precision == pytest.approx(1.0)
    assert recall == pytest.approx(0.5)
    assert fbeta == pytest.approx(2 / 3)
