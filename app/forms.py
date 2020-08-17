from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired, InputRequired



class SetupGprForm(FlaskForm):
    num_numerical_settings = IntegerField(
        'Number for numerical settings',
        [InputRequired(message='Must be an integer')]
        )
    submit = SubmitField('Submit')


class MyBaseForm(FlaskForm):
    setting_name = StringField('Setting Name')
    setting_from = DecimalField('Lowest Setting Value')
    setting_to = DecimalField('Highest Setting Value')



class SpecifyGprForm(FlaskForm):
    def __init__(self, num_settings):
        self.num_settings = num_settings
    
        class DynamicForm(FlaskForm): pass
        
        for i in range(self.num_settings):
            setting_name = 'setting_name_' + str(i)
            setting_from = 'setting_from_' + str(i)
            setting_to = 'setting_to_' + str(i)

            setattr(DynamicForm, setting_name, StringField(setting_name))
            setattr(DynamicForm, setting_from, DecimalField(setting_from))
            setattr(DynamicForm, setting_to, DecimalField(setting_to))
            
        setattr(DynamicForm, 'submit', SubmitField('Submit'))

        self.dynamic_form = DynamicForm()

        for field in self.dynamic_form:
            print(field)



    
