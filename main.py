from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
import webbrowser
import requests
import json

api_key='eJHIxbmiWxF7KHaI7uuGjz9pdPekbBzwFRagd4V_Xp2VrsN9TEe9wNcxRLuOEyRXKAWEflE2vtPlrhVG90Q1MScd42vNG5Xc3nn4ojBXz7G38w7E0TmoInLqhWIHYXYx'
headers = {'Authorization': 'Bearer %s' % api_key}
url='https://api.yelp.com/v3/businesses/search'

location_helper = """
MDTextField:
    hint_text: "Enter location preference"
    helper_text: "Just DEcide loL"
    helper_text_mode: "on_focus"
    icon_right: "apple"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:450
"""
class MainApp(MDApp):
    
    def build(self):
        self.screen = Screen()
        self.location = Builder.load_string(location_helper)
        button = MDRectangleFlatButton(text='Enter',size_hint=(.3, .1), pos_hint={'center_x': .5, 'center_y': .4}, on_release=self.locationFunc)
        self.screen.add_widget(self.location)
        self.screen.add_widget(button)
        self.a=0
        self.y = []
        self.urls=[]
        return self.screen
    def callLocation(self):
        self.location.text = ''
        self.location = Builder.load_string(location_helper)
        
    def locationFunc(self, obj):
        params = {'term':'food','location':self.location.text}  
        req=requests.get(url, params=params, headers=headers)
        #print('The status code is {}'.format(req.status_code))
        #json.loads(req.text)
        bizdata=json.loads(req.text)
        for index in range(0,len(bizdata['businesses'])):
            self.y.append(bizdata['businesses'][index]['name'])
            self.urls.append(bizdata['businesses'][index]['url'])
        self.callBox()

    def callBox(self):
        self.close_button =MDFlatButton(text='Close', on_release=self.close_dialog)
        self.more_button =MDFlatButton(text='More', on_release=self.clickedOnMore)
        self.link_button =MDFlatButton(text='Link', on_release=self.clickedonLink)
        self.dialog=MDDialog(title= 'YUMMY place to Eat', text=self.y[self.a]+'!!', size_hint=(.7,1), buttons=[self.close_button, self.link_button, self.more_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        self.location.text = ''
        self.y=[]
        self.urls=[]

    def clickedOnMore(self, obj):
        self.a+=1
        self.dialog.dismiss()
        self.close_button =MDFlatButton(text='Close', on_release=self.close_dialog)
        self.more_button =MDFlatButton(text='More', on_release=self.clickedOnMore)
        self.link_button =MDFlatButton(text='Link', on_release=self.clickedonLink)
        self.dialog=MDDialog(title= 'YUMMY place to Eat', text=self.y[self.a]+'!!', size_hint=(.7,1), buttons=[self.close_button, self.link_button, self.more_button])
        self.dialog.open()

    def clickedonLink(self,obj):
        webbrowser.open(self.urls[self.a])

    """ def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Clear the solution widget
            self.solution.text = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                # Don't add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                # First character cannot be an operator
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

 """
MainApp().run()

