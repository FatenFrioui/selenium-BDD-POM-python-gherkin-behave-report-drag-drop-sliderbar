import time

from behave import given,when,then
from selenium import webdriver
from selenium.webdriver import ActionChains
from numpy.testing import assert_equal


@given(u'The user navigate to the drag and drop URL')
def step_impl(context):

    context.dd.setup("https://qavbox.github.io/demo/dragndrop/")


@when(u'he move the drag box to drop box')
def step_impl(context):

    context.dd.drag()
    time.sleep(3)

@then(u'he see the message change to Dropped!')
def step_impl(context):
    msg=context.dd.msg()
    assert_equal(msg,"Dropped!")

