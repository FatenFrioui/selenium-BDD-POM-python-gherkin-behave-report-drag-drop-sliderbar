from selenium.webdriver import ActionChains

from Browser import Browser

objectToDrag = "draggable"
objectToDrop = "droppable"
x_offset = "280"
y_offset="16"
bar_slider='//body/form[@id="form1"]/fieldset[@id="regform"]/div[1]/div[5]/input[1]'
slide_nbr='// span[ @ id = "range"]'



class DragDrop(Browser):
    def setup(self,link):
        self.driver.get(link)
    def drag(self):
        drag1 = self.driver.find_element_by_id(objectToDrag)
        drop1 = self.driver.find_element_by_id(objectToDrop)
        ActionChains(self.driver).drag_and_drop(drag1, drop1).perform()
    def msg(self):
        msg = self.driver.find_element_by_id(objectToDrop).text
        return (msg)
    def slider_bar(self):
        slider = self.driver.find_element_by_xpath(bar_slider)
        ActionChains(self.driver).drag_and_drop_by_offset(slider, 280, 16).perform()
    def msg_slider(self):
        msg_s = self.driver.find_element_by_xpath(slide_nbr).text
        return (msg_s)