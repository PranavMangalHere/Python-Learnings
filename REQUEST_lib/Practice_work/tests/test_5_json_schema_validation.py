""" 
LEVEL 4 — Error Handling & Reliability
Task 15 — Retry Mechanism
Create retry utility.
Requirements:

Retry failed request 3 times
Retry only for:
500
timeout
Add delay between retries
Concepts
reliability
exception handling
retry logic
"""

import requests
import time
def retry_request(url, retries=3, delay=2):
    for attempt in range(1, retries + 1):
        try:
            print(f"\nAttempt {attempt}")
            response = requests.get(
                url,
                timeout=3
            )
            # -----------------------------
            # Retry for Server Errors
            # -----------------------------
            if response.status_code >= 500:

                print(
                    f"Server Error: "
                    f"{response.status_code}"
                )
                if attempt < retries:

                    print(
                        f"Retrying in {delay} seconds..."
                    )
                    time.sleep(delay)
                    continue
            # Success
            print("\nRequest Successful")
            return response
        # -----------------------------
        # Retry for Timeout
        # -----------------------------
        except requests.exceptions.Timeout:
            print("Request Timed Out")
            if attempt < retries:
                print(
                    f"Retrying in {delay} seconds..."
                )
                time.sleep(delay)
            else:
                print("\nMax retries reached")
        # -----------------------------
        # Handle Other Exceptions
        # -----------------------------
        except requests.exceptions.RequestException as e:
            print("\nRequest Failed:")
            print(e)
            break
    return None
# --------------------------------
# Test Retry Mechanism
# --------------------------------
test_url = "https://httpbin.org/status/500"
response = retry_request(test_url)
# print("\nFinal Response:")
# print(response)

# What is Retry Logic?
# Retry mechanism automatically retries temporary failures.
# Used for:
# unstable servers
# flaky APIs
# network issues
# temporary outages
# Very common in production systems.
# Retry Conditions
# Your task required retry only for:
# Condition	Reason
# 500 errors	temporary server issue
# timeout	temporary network issue
# Why NOT retry all failures?
# Example:
# Status	Retry?
# 401	❌ wrong auth
# 403	❌ permission issue
# 404	❌ resource missing
# 500	✅ server issue
# timeout	✅ network issue
# Retrying permanent failures wastes resources.
# Important Exception Handling
# except requests.exceptions.Timeout
# Handles request timeout.
# Very common production issue.
# Timeout Example
# requests.get(url, timeout=3)
# Means:
# Wait maximum 3 seconds.
# If server takes longer:
# requests.exceptions.Timeout
# raised.
# Important Reliability Concept
# Retries improve:
# fault tolerance
# reliability
# resilience
# especially in distributed systems.
# Important Interview Question
# What problems can retries cause?
# Answer:
# duplicate requests
# duplicate payments/orders
# server overload
# retry storms
# This is why retries should be carefully controlled.
# Important Idempotency Connection
# Retries are safer for:
# Method	Safe Retry?
# GET	✅
# PUT	✅
# DELETE	usually
# POST	risky
# Because POST may create duplicate resources.
# Industry-Level Improvements
# Real frameworks usually add:
# Feature	Purpose
# exponential backoff	avoid retry storms
# jitter	randomize retry timing
# retry logging	observability
# circuit breaker	stop endless retries


""" 
Task 16 — Timeout Testing
Tasks:
Add timeout to requests
Handle timeout exceptions
Print proper error messages
Concepts
timeout=
exceptions
"""





""" 
Task 18 — JSON Schema Validator

Validate response contains:

required keys
correct data types
non-empty values
Example
{
   "id": int,
   "name": str
}
Concepts
API contract testing
schema validation
"""

import requests


url = "https://jsonplaceholder.typicode.com/users/1"


def validate_schema(data, schema):

    for key, expected_type in schema.items():

        # --------------------------------
        # Required Key Validation
        # --------------------------------

        assert key in data, f"{key} is missing"

        # --------------------------------
        # Data Type Validation
        # --------------------------------

        assert isinstance(
            data[key],
            expected_type
        ), (
            f"{key} should be "
            f"{expected_type.__name__}"
        )
        # --------------------------------
        # Non-Empty Validation
        # --------------------------------
        if isinstance(data[key], str):

            assert data[key].strip() != "", (
                f"{key} is empty"
            )
    print("\nSchema Validation Successful")
def test_json_schema_validator():
    response = requests.get(url)
    data = response.json()
    # --------------------------------
    # Expected Schema
    # --------------------------------
    expected_schema = {
        "id": int,
        "name": str,
        "username": str,
        "email": str
    }
    # --------------------------------
    # Validate Schema
    # --------------------------------
    validate_schema(data, expected_schema)
    print("\nValidated Response:")
    print(data)
test_json_schema_validator()

""" 
What is Schema Validation?

Schema validation ensures API response follows expected structure.

Example:

{
   "id": 1,
   "name": "Leanne Graham"
}

Expected contract:

{
   "id": int,
   "name": str
}
What is API Contract Testing?

Contract testing verifies agreement between:

Component	Responsibility
Backend	send expected response
Frontend/client	consume expected structure

If API suddenly changes:

{
   "identifier": "abc"
}

instead of:

{
   "id": 1
}

frontend may break.

Schema validation catches this early.

Important Validations Performed
1. Required Keys
assert key in data

Ensures mandatory fields exist.

2. Correct Data Types
isinstance(data[key], int)

Ensures API returns correct types.

Example:

Expected	Invalid
int	"123"
str	123
3. Non-Empty Values
assert data[key].strip() != ""

Prevents empty strings.

Important Interview Question

Difference between:

Validation Type	Purpose
Functional validation	business logic
Schema validation	structure/types
Contract testing	API agreement
Real-World Schema Validation Libraries

Industry commonly uses:

Library	Purpose
jsonschema	JSON Schema validation
pydantic	model validation
marshmallow	serialization/validation

Example using jsonschema:

from jsonschema import validate
"""