from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DISTRICT_CHOICES = (
		('Thrissur', 'Thrissur'),
		('Alappuzha', 'Alappuzha'),
		('Ernakulam', 'Ernakulam'),
		('Idukki', 'Idukki'),
		('Kannur', 'Kannur'),
		('Kasaragod', 'Kasaragod'),
		('Kollam', 'Kollam'),
		('Kozhikode', 'Kozhikode'),
		('Malappuram', 'Malappuram'),
		('Palakkad', 'Palakkad'),
		('Pathanamthitta', 'Pathanamthitta'),
		('Thiruvananthapuram', 'Thiruvananthapuram'),
		('Wayanad', 'Wayanad'),
		('Kottayam', 'Kottayam'),

	)

	STATE_CHOICES = (
		('Kerala', 'Kerala'), 
		('###', '###'),
	)

	PAYMENT_METHOD_CHOICES = (
		('Paypal', 'Paypal'),
		('Credit Card','Credit Card')
	)

	district = forms.ChoiceField(choices=DISTRICT_CHOICES)
	state =  forms.ChoiceField(choices=STATE_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'city', 'district', 'state', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
