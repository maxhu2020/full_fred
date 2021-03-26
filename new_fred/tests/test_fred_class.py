
import pytest
from new_fred.fred import Fred

# ensure method coverage
# test different realtime dates

@pytest.fixture
def fred():
    return Fred()

@pytest.fixture
def expected_get_category_id_125():
    expected = {
        'categories': [
            {'id': 125, 
            'name': 'Trade Balance', 
            'parent_id': 13}
            ]
        }
    return expected

@pytest.fixture
def expected_get_series_id():
    """
    The expected value associated with key 'id' in the map returned
    by fred.get_series('GNPCA')
    """
    return "GNPCA"

@pytest.fixture
def expected_get_series_title():
    """
    The expected value associated with key 'title' in the map returned
    by fred.get_series('GNPCA')
    """
    return "Real Gross National Product"

@pytest.mark.skip("passed")
def test_get_category_id_125_returns_trade_balance(
        fred: Fred, 
        expected_get_category_id_125: dict,
        ):
    expected = expected_get_category_id_125 
    assert fred.get_a_category(125) == expected

@pytest.fixture
def expected_names_get_categories_of_series():
    return ("Japan", "Monthly Rates",)

@pytest.mark.skip("passed")
def test_get_child_categories_id_13_returns_children_with_parentid_13(
        fred: Fred, 
        ):
    """
    New child categories may be added to the category subtree rooted 
    at "U.S. Trade and Transactions" (category_id 13) and make this 
    test fail despite fred.get_child_categories(13) returning the 
    requested data. Instead of testing equivalence it makes more 
    sense to test whether each category returned by the method call 
    has parent_id of 13
    """
    returned_correctly = False
    observed = fred.get_child_categories(13) 
    for i in range(len(observed["categories"])):
        a_category = observed["categories"][i]
        if "parent_id" not in a_category.keys():
            break
        if a_category["parent_id"] != 13:
            break
        if i == len(observed["categories"]) - 1:
            returned_correctly = True
    assert returned_correctly == True

def test_get_related_categories():
    """
    Unclear at this point how to test
    """
    pass


def test_get_series_in_a_category_category_id_NO():
    """
    Unclear at this point how to test
    """
    pass

@pytest.mark.skip("passed")
def test_get_series(
        fred: Fred,
        expected_get_series_id: str,
        expected_get_series_title: str,
        ):
    returned_correctly = False
    observed = fred.get_series("GNPCA")
    if "id" in observed.keys():
        if not observed["id"] == expected_get_series_id:
            assert returned_correctly == True
    if "title" in observed.keys():
        if not observed["title"] == expected_get_series_title: 
            assert returned_correctly == True
    returned_correctly = True
    assert returned_correctly == True

@pytest.mark.skip("passed")
def test_get_categories_of_series(
        fred: Fred,
        expected_names_get_categories_of_series: tuple,
        ):
    returned_correctly = False
    observed = fred.get_categories_of_series("EXJPUS")
    if not isinstance(observed, dict):
        assert returned_correctly == True
    if not "categories" in observed.keys():
        assert returned_correctly == True
    categories = observed["categories"] # categories is a list
    expected_keys = ("id", "name", "parent_id")
    for key in categories[0].keys():
        if key not in expected_keys:
            assert returned_correctly == True
    expected_names = expected_names_get_categories_of_series
    for a_category in categories:
        if expected_names[0] in a_category.values():
            returned_correctly = True
        if expected_names[1] in a_category.values():
            returned_correctly = True
    assert returned_correctly == True









