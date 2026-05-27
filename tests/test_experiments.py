from app.services.experiments import get_bucket


def test_bucket_assignment_is_deterministic():
    assert get_bucket(123, "homepage_test") == get_bucket(123, "homepage_test")


def test_bucket_is_in_percentage_range():
    bucket = get_bucket(123, "homepage_test")
    assert 0 <= bucket < 100
