import json
from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture
def fetched_data():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the NASA API page
        page.goto('https://ssd-api.jpl.nasa.gov/cad.api')

        # Fetch data from the NASA API and return it
        fetched_data_str = page.evaluate(
            '() => fetch("https://ssd-api.jpl.nasa.gov/cad.api").then(response => response.json())'
        )

        return json.loads(json.dumps(fetched_data_str))

def test_data_type(fetched_data):
    # Validate the structure of the fetched data
    assert set(fetched_data.keys()) == {"signature", "count", "fields", "data"}

    # Check the types of the fields
    field_types = {
        "signature": dict,
        "count": int,
        "fields": list,
        "data": list
    }
    for field, expected_type in field_types.items():
        assert isinstance(fetched_data[field], expected_type)

# Run the tests and generate an HTML report
if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html", __file__])
