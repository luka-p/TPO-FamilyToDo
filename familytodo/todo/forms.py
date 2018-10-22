from django import forms
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator

class TodoForm(forms.Form):
    text = forms.CharField(max_length=40,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Task', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn', 'size' : 200}))
    CHOICES = (('1','Low'),('2','Medium'),('3','High'))
    importance = forms.ChoiceField(widget=forms.RadioSelect(attrs={'display': 'inline-block'}), choices=CHOICES, initial=2)

class ParentForm(forms.Form):
    username = forms.CharField(max_length=10,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Family name', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn', 'size' : 200}))
    password = forms.CharField(max_length=10,
        widget=forms.PasswordInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Password', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn', 'size' : 200}))

class KidForm(forms.Form):
    username = forms.CharField(max_length=10,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Family name', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn', 'size' : 200}))

class KidAddForm(forms.Form):
    name = forms.CharField(max_length=10,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Kid name', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn', 'size' : 200}))

class FamilyForm(forms.Form):
    familyname = forms.CharField(max_length=10,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Family name', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn', 'size' : 200}))
    fampass = forms.CharField(max_length=10,
        widget=forms.PasswordInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Password', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn', 'size' : 200}))

class Form1FRI(forms.Form):
    ime_priimek = forms.CharField(label="Ime in priimek", max_length=20, validators=[RegexValidator('^[a-zA-Z_ ]*$', message="Dovoljen vnos samo besed brez locil")],
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Student/ka', 'size' : 200}))
    bivalisce = forms.CharField(label="Bivalisce", max_length=40,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 's stalnim bivaliscem', 'size' : 200}))
    vpisnast = forms.CharField(label="Vpisna stevilka", max_length=9, min_length=9, validators=[RegexValidator('[0-9]', message="Dovoljen je samo vnos stevilk")],
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 's vpisno stevilko', 'size' : 9}))
    enaslov = forms.EmailField(label="E naslov", validators=[EmailValidator(message="Neveljaven vnos email naslova")],
        widget=forms.EmailInput(
            attrs={'class' : 'form-control', 'placeholder' : 's enaslovom'}))
    CHOICES1 = (('1','prvi'),('2','drugi'),('3','tretji'))
    letnik = forms.CharField(label='Letnik', widget=forms.Select(choices=CHOICES1, attrs={'placeholder' : 'letnik'}))
    CHOICES2 = (('BUN-RI','BUN-RI'),('BVS-RI','BVS-RI'),('BM-RI','BM-RI'),('BUN-RM','BUN-RM'),('BM-PRI','BM-PRI'),('BDR-RI','BDR-RI'))
    tip = forms.CharField(label='Tip', widget=forms.Select(choices=CHOICES2))
    ldodatno = "Tezave, telesne okvare oziroma posebne potrebe"
    dodatno = forms.CharField(label=ldodatno, widget=forms.Textarea(attrs={'rows':5, 'cols':70, 'style':'resize:none;', 'class' : 'form-control', 'placeholder' : ''}))
    CHOICES3 = (('Menje1','Mnenje1'),('Mnenje2','Mnenje2'),('Drugo','Drugo'))
    menje = forms.ChoiceField(label='Priloga', widget=forms.RadioSelect(attrs={'display': 'inline-block'}), choices=CHOICES3)
    drugo = forms.CharField(label='Drugo', max_length=50, required=False,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'ce ste izbrali drugu tukaj vpisite naslov priloge', 'size' : 200}))
    datoteka = forms.FileField(required=False)
    datum = forms.DateField(label='Datum oddaje (dan/mesec/leto)',
        widget=forms.widgets.DateTimeInput(format="%d/%m/%Y", attrs={'placeholder':"DD/MM/YY", 'class' : 'form-control'}))

class Form2FRI(forms.Form):

    ph1 = "Pojasnite, kaj je problem, ki ga želite reševati, in podajte motivacijo za delo. Pri opisu motivacije se navežite na literaturo in nerešene probleme, ki jih bo naslavljala vaša magistrska naloga. Delo umestite v ožje področje dela. Besedilo naj obsega približno 800 znakov s presledki vred."
    ph2 = "Opišite pregled sorodnih del na ožjem področju, na katerem nameravate opravljati magistrsko nalogo. Vsako delo naj bo na kratko opisano v nekaj stavkih, besedilo pa naj poudari njegove glavne prednosti, slabosti ali posebnosti. Sklicujte se na dela, navedena v razdelku 3.5 Literatura in viri. Pregled naj bo fokusiran in naj obsega približno pol strani A4."
    ph3 = "Opišite predvidene prispevke magistrske naloge s področja računalništva in informatike, ki so lahko strokovni ali znanstveni. Poudarite in opišite predvideni napredek ali novost vašega dela v primerjavi z obstoječim stanjem na strokovnem (ali znanstvenem) področju. Opis naj obsega približno 500 znakov s presledki vred."
    ph4 = "Na kratko opredelite metodologijo, ki jo nameravate uporabiti pri svojem delu. Metodologija vsebuje metode, ki jih nameravate uporabiti (npr. razvoj v izbranem programskem jeziku, izdelava strojne opreme itd.), postopek analize, postopek evalvacije vašega prispevka in primerjavo s sorodnimi deli. Opis naj obsega približno 500 znakov s presledki vred."
    ph5 = "Tu navedite vse vire, ki jih citirate v predlogu teme. Citiranje naj bo v skladu z znanstveno-strokovnimi standardi citiranja, na primer, [1]. Seznam naj vsebuje vsaj nekaj del, objavljenih v zadnjih petih letih. Prednostno naj bodo navedene objave s konferenc, revij, oziroma drugih priznanih virov."

    # OSEBNE INFO
    ime_priimek = forms.CharField(label="Ime in priimek", max_length=20, validators=[RegexValidator('^[a-zA-Z_ ]*$', message="Dovoljen vnos samo besed brez locil")],
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Student/ka', 'size' : 200}))
    bivalisce = forms.CharField(label="Bivalisce", max_length=40,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 's stalnim bivaliscem', 'size' : 200}))
    vpisnast = forms.CharField(label="Vpisna stevilka", max_length=9, min_length=9, validators=[RegexValidator('[0-9]', message="Dovoljen je samo vnos stevilk")],
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 's vpisno stevilko', 'size' : 9}))
    # INFO O DELU
    naslov_slo = forms.CharField(label="Naslov slovensko", max_length=40,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'SLO, max=40', 'size' : 200}))
    naslo_en = forms.CharField(label="Naslov angleško", max_length=40,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'EN, max=40', 'size' : 200}))
    mentor_ime_priimek = forms.CharField(label="Ime in priimek mentorja", max_length=20, validators=[RegexValidator('^[a-zA-Z_ ]*$', message="Dovoljen vnos samo besed brez locil")],
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Mentor/ka', 'size' : 200}))
    mentor_ustanova = forms.CharField(label="Ustanova", max_length=40,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'zaposlen v ustanovi', 'size' : 200}))
    mentor_enaslov = forms.EmailField(label="E naslov mentorja", validators=[EmailValidator(message="Neveljaven vnos email naslova")],
        widget=forms.EmailInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enaslov'}))
    somentor_ime_priimek = forms.CharField(label="Ime in priimek somentorja", max_length=20, validators=[RegexValidator('^[a-zA-Z_ ]*$', message="Dovoljen vnos samo besed brez locil")],
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Somentor/ka', 'size' : 200}))
    somentor_ustanova = forms.CharField(label="Ustanova", max_length=40,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'zaposlen v ustanovi', 'size' : 200}))
    somentor_enaslov = forms.EmailField(label="E naslov somentorja", validators=[EmailValidator(message="Neveljaven vnos email naslova")],
        widget=forms.EmailInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enaslov'}))
    datum_izpolnitve = forms.DateField(label='Datum izpolnitve (dan/mesec/leto)',
        widget=forms.widgets.DateTimeInput(format="%d/%m/%Y", attrs={'placeholder':"DD/MM/YY", 'class' : 'form-control'}))
    # PREDLOG
    podrocje_slo = forms.CharField(label="1.1 Področje slovensko", widget=forms.Textarea(attrs={'rows':3, 'cols':70, 'style':'resize:none;', 'class' : 'form-control', 'placeholder' : 'računalništvo in informatika, računalniška arhitektura'}))
    podrocje_en = forms.CharField(label="1.2 Področje angleško", widget=forms.Textarea(attrs={'rows':3, 'cols':70, 'style':'resize:none;', 'class' : 'form-control', 'placeholder' : 'computer science, computer architecture'}))
    kljucne_besede_slo = forms.CharField(label="2.1 Ključne besede slovensko", widget=forms.Textarea(attrs={'rows':3, 'cols':70, 'style':'resize:none;', 'class' : 'form-control', 'placeholder' : 'slovensko'}))
    kljucne_besede_en = forms.CharField(label="2.2 Ključne besede angleško", widget=forms.Textarea(attrs={'rows':3, 'cols':70, 'style':'resize:none;', 'class' : 'form-control', 'placeholder' : 'angleško'}))
    uvod_in_opis_problema = forms.CharField(label="3.1 Uvod in opis problema", max_length=800, widget=forms.Textarea(attrs={'rows':5, 'cols':70, 'style':'resize:none;', 'class' : 'form-control', 'placeholder' : ph1}))
    pregled_sorodnih_del = forms.CharField(label="3.2 Pregled sorodnih del", max_length=500, widget=forms.Textarea(attrs={'rows':5, 'cols':70, 'style':'resize:none;', 'class' : 'form-control', 'placeholder' : ph2}))
    predvideni_prispevki = forms.CharField(label="3.3 Predvideni prispevki", max_length=500, widget=forms.Textarea(attrs={'rows':5, 'cols':70, 'style':'resize:none;', 'class' : 'form-control', 'placeholder' : ph3}))
    metodologija = forms.CharField(label="3.4 Metodologija", max_length=500, widget=forms.Textarea(attrs={'rows':5, 'cols':70, 'style':'resize:none;', 'class' : 'form-control', 'placeholder' : ph4}))
    literatura_viri = forms.CharField(label="3.5 Literatura in viri", max_length=500, widget=forms.Textarea(attrs={'rows':5, 'cols':70, 'style':'resize:none;', 'class' : 'form-control', 'placeholder' : ph5}))

class Form3FRI(forms.Form):
    # OSEBNE INFO
    ime_priimek = forms.CharField(label="Ime in priimek", max_length=20, validators=[RegexValidator('^[a-zA-Z_ ]*$', message="Dovoljen vnos samo besed brez locil")],
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Student/ka', 'size' : 200}))
    bivalisce = forms.CharField(label="Bivalisce", max_length=40,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 's stalnim bivaliscem', 'size' : 200}))
    vpisnast = forms.CharField(label="Vpisna stevilka", max_length=9, min_length=9, validators=[RegexValidator('[0-9]', message="Dovoljen je samo vnos stevilk")],
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 's vpisno stevilko', 'size' : 9}))
    letnik = forms.CharField(label="Letnik vpisa", max_length=4, min_length=4, validators=[RegexValidator('[0-9]', message="Dovoljen je samo vnos stevilk")],
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'vpisan/a leta', 'size' : 4}))
    GSM = forms.CharField(label="GSM", max_length=9, min_length=9, validators=[RegexValidator('[0-9]', message="Dovoljen je samo vnos stevilk")],
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'telefon, samo stevilke', 'size' : 9}))
    enaslov = forms.EmailField(label="E naslov", validators=[EmailValidator(message="Neveljaven vnos email naslova")],
        widget=forms.EmailInput(
            attrs={'class' : 'form-control', 'placeholder' : 'enaslov'}))
    CHOICES2 = (('BUN-RI','BUN-RI'),('BVS-RI','BVS-RI'),('BM-RI','BM-RI'),('BUN-RM','BUN-RM'),('BM-PRI','BM-PRI'),('BDR-RI','BDR-RI'))
    tip = forms.CharField(label='Tip', widget=forms.Select(choices=CHOICES2))
    C1 = "izdajo sklepa o določitvi pogojev za nadaljevanje študija po prekinitvi za več kot dve leti se plača na račun FRI po prejetem računu (po veljavnem ceniku UL)"
    C2 = "izdaja slepa o določitvi pogojev za nadaljevanje študija po prekinitvi za več kot deset let se plača na račun FRI po prejetem računu (po veljavnem ceniku UL)"
    CHOICES3 = ((C1,C1),(C2,C2))
    prosi_za = forms.CharField(label='UL FRI prosi za:', widget=forms.RadioSelect(choices=CHOICES3))
    utemeljitev = forms.CharField(label="Utemeljitev", widget=forms.Textarea(attrs={'rows':5, 'cols':70, 'style':'resize:none;', 'class' : 'form-control', 'placeholder' : ''}))
    datum_izpolnitve = forms.DateField(label='Datum izpolnitve (dan/mesec/leto)',
        widget=forms.widgets.DateTimeInput(format="%d/%m/%Y", attrs={'placeholder':"DD/MM/YY", 'class' : 'form-control'}))
