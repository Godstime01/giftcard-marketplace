from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from .models import UserModel

class AccountCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        counter = 0

        for visible in self.visible_fields():
           
           
            visible.field.widget.attrs['class'] = 'rounded-md w-full shadow block my-2'
            visible.field.widget.attrs['placeholder'] = visible.field.label

            if counter > 3:
                visible.field.widget.attrs['class'] =  'rounded-md w-full shadow border block my-2 col-span-full'
            
            counter += 1

    class Meta:
        model = UserModel
        fields = [ 'username', 'password1', 'password2']
        

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        print(self.visible_fields()[0])
        for visible in self.visible_fields():
           
            visible.field.widget.attrs['class'] = 'rounded-md w-full shadow border block my-2'
            visible.field.widget.attrs['placeholder'] = visible.field.label
            print(visible.label_tag)
            visible.label_tag(attrs={'class': 'text-purple-400 mb-5'}) 

        print(self.visible_fields()[0])

    class Meta:
        model = UserModel
        fields = ['username', 'password']
        