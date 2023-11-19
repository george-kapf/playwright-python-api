import json
from playwright.sync_api import sync_playwright
import pytest


# Sample data
sample_data = {
    "signature": {"source": "NASA/JPL SBDB Close Approach Data API", "version": "1.5"},
    "count": 3,
    "fields": ["des", "orbit_id", "jd", "cd", "dist", "dist_min", "dist_max", "v_rel", "v_inf", "t_sigma_f", "h",
               "diameter", "diameter_sigma", "fullname"],
    "data": [
        ["153814", "174", "2461948.724524223", "2028-Jun-26 05:23", "0.00166253924938707",
         "0.00166237672775144", "0.00166270177137481", "10.2426019613426", "10.084918538826", "< 00:01", "18.33",
         "0.932", "0.011", "153814 (2001 WN5)"],
        ["99942", "206", "2462240.407091595", "2029-Apr-13 21:46", "0.000254099098170977",
         "0.000254085852623379", "0.000254112343772133", "7.42249308586014", "5.84135545611464", "< 00:01", "19.7",
         "0.34", "0.04", " 99942 Apophis (2004 MN4)"],
        ["2001 AV43", "42", "2462452.142037054", "2029-Nov-11 15:25", "0.00209271674918052",
         "0.00209125158265035", "0.00209418316351851", "3.99789389003422", "3.66561381185116", "00:03", "24.6", None,
         None, "       (2001 AV43)"]
    ]
}

def fetch_data():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the NASA API page
        page.goto('https://ssd-api.jpl.nasa.gov/cad.api')

        # Fetch data from the NASA API and return it
        fetched_data_str = page.evaluate('() => fetch("https://ssd-api.jpl.nasa.gov/cad.api").then(response => response.json())')

        fetched_data = json.dumps(fetched_data_str)

        return fetched_data


def test_data_type():
    # Fetch data from the NASA API
    fetched_data_str = fetch_data()
    fetched_data = json.loads(fetched_data_str)

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

def test_data_values():
    # Fetch data from the NASA API
    fetched_data_str = fetch_data()
    fetched_data = json.loads(fetched_data_str)

    # Check for null values in the sample data
    for row in fetched_data["data"]:
        assert None not in row

# Run the tests and generate an HTML report
if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html", __file__])
