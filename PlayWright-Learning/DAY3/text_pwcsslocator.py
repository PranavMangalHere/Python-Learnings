import pytest
from playwright.sync_api import Page, expect

"""
tag id  tag#id
tag class    tag.class
tag attribute   tag[attribute = value]    tag:not([attribute = value])[attribute = value]
                tag[attribute = value]+tag {it will give the below tag }        tag+*
tag class attribute    tag.class[attribute=value]  
"""

def test_pwcsslocator(page:Page):

    page.goto("https://demowebshop.tricentis.com/")
    expect(page).to_have_url("https://demowebshop.tricentis.com/")

    page.locator("input#small-searchterms").fill("hello")
    page.wait_for_timeout(2000)