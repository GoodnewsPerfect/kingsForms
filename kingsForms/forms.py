from django import forms

# Create your forms here.
CHOICE_TITLES = [('1', 'Zonal Director'), ('2', 'Zonal Secretary'), ('3', 'Group Pastor'), ('4', 'Chapter Pastor'),
                 ('5', 'Asst Chapter Pastor'), ('6', 'Cell Leader')]
CHOICE_ZONES = [('1', 'NIGERIA ZONE A'), ('2', 'NIGERIA ZONE B'), ('3', 'NIGERIA ZONE C'), ('4', 'NIGERIA ZONE D'),
                ('5', 'NIGERIA ZONE E'), ('6', 'NIGERIA ZONE F'), ('7', 'NIGERIA ZONE G'), ('8', 'NIGERIA ZONE H'),
                ('9', 'NIGERIA ZONE I'), ('10', 'NIGERIA ZONE J'), ('11', 'NIGERIA ZONE K'),
                ('12', 'NIGERIA ZONE L'), ('13', 'UK ZONE A'), ('14', 'UK ZONE B'), ('15', 'GHANA ZONE A'),
                ('16', 'GHANA ZONE B'), ('17', 'SOUTH AFRICA ZONE A'), ('18', 'SOUTH AFRICA ZONE B'),
                ('19', 'SOUTH AFRICA ZONE C'), ('20', 'SOUTH AFRICA ZONE D'), ('21', 'SOUTH AFRICA ZONE E'),
                ('22', 'KENYA ZONE'), ('23', 'USA GROUP 1'), ('24', 'USA GROUP 2'), ('25', 'USA GROUP 3'),
                ('26', 'USA GROUP 4'), ('27', 'CAMEROON GROUP 1'), ('28', 'CAMEROON GROUP 2'), ('29', 'UGANDA GROUP'),
                ('30', 'BLW INTERNATIONAL MISSIONS'), ('31', 'SIERRA LEONE GROUP'), ('32', 'ETHIOPIA GROUP'),
                ('33', 'SECOND TIER CHURCHES'), ('34', 'CANADA CHAPTERS'), ('35', 'NORTH CYPRUS CHAPTERS'),
                ('36', 'EUROPE CHAPTERS'), ('37', 'ASIA CHAPTERS'), ('38', 'MIDDLE EAST CHAPTERS'),
                ('39', 'OCEANIA CHAPTERS')]
CHOICE_BOOLS = [('1', 'Yes'), ('2', 'No')]


class Title(forms.Form):
    title = forms.ChoiceField(required=True, widget=forms.Select, choices=CHOICE_TITLES)


class FullName(forms.Form):
    full_name = forms.CharField(required=True, max_length=100)


class KingsChat(forms.Form):
    kingsChat_number = forms.CharField(required=True, max_length=50)


class ActiveKcId(forms.Form):
    active_kc_id = forms.CharField(required=True, max_length=50)


class Zone(forms.Form):
    zone = forms.ChoiceField(required=True, widget=forms.Select, choices=CHOICE_ZONES)


class Church(forms.Form):
    church = forms.CharField(required=True, max_length=50)


class Attendance(forms.Form):
    attendance = forms.ChoiceField(required=True, widget=forms.Select, choices=CHOICE_BOOLS)


class Certification(forms.Form):
    certification = forms.ChoiceField(required=True, widget=forms.Select, choices=CHOICE_BOOLS)


class Badge(forms.Form):
    badge = forms.ChoiceField(required=True, widget=forms.Select, choices=CHOICE_BOOLS)


class Feedback(forms.Form):
    feedback = forms.CharField(required=False, widget=forms.Textarea, max_length=2000)


class Observation(forms.Form):
    observation = forms.CharField(required=True, widget=forms.Textarea, max_length=2000)
