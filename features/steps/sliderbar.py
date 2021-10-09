import time
from behave import given,when,then
from numpy.testing import assert_equal





@when(u'he move a slider to 100 value')
def step_impl(context):
    context.dd.slider_bar()
    time.sleep(3)

@then(u'he achieved 100')
def step_impl(context):
    slidernbr = context.dd.msg_slider()
    assert_equal(slidernbr, "100")
