# coding: utf-8

from pycti import OpenCTIApiClient

# Variables
api_url = "http://opencti:4000"
api_token = "bfa014e0-e02e-4aa6-a42b-603b19dcf159"

# OpenCTI initialization
opencti_api_client = OpenCTIApiClient(api_url, api_token)

# DEPRECATED >=6.2 & <6.5. Use `promote_to_indicator_v2` instead
obs1 = opencti_api_client.stix_cyber_observable.create(
    simple_observable_key="IPv4-Addr.value", simple_observable_value="55.55.55.55"
)
observable = opencti_api_client.stix_cyber_observable.promote_to_indicator(
    id=obs1.get("id")
)
print("promoted observable, original observable is", observable)

# Please use promote_to_indicator_v2
obs2 = opencti_api_client.stix_cyber_observable.create(
    simple_observable_key="IPv4-Addr.value", simple_observable_value="55.55.55.99"
)
indicator = opencti_api_client.stix_cyber_observable.promote_to_indicator_v2(
    id=obs2.get("id")
)
print("promoted observable, indicator is", indicator)
