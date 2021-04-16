import datetime
import types

from flask import url_for, abort
from flask import request
from flask import render_template as template

from flask_classful import FlaskView, route

from app import fake, turbo


from app.models.missions import Mission
from app.models.mission_items import MissionItem
from app.models.data_sources.facebook.users import FacebookUser
from app.models.data_sources.facebook.posts import FacebookPost

from app.controllers.data_sources.facebook.facebook import FacebookView


class MissionView(FlaskView):
    def index(self):
        return template("missions/index.html.j2")

    def show(self, id):
        with_solution = request.args.get("with_solution", False)
        if with_solution == "True":
            with_solution = True
        # print(request.kwargs)
        print(with_solution)
        print(type(with_solution))

        mission = self._load_mission("password_guesser")

        # set contents
        for source in mission.data_sources:
            if source.name == "browser":
                source.html = template(
                    "data_sources/browser/_browser.html.j2", html=fake.text()
                )
            elif source.name == "facebook":
                source.html = FacebookView().show(user=source.user)

        for action in mission.actions:
            if action.name == "facebook_login":
                action.html = FacebookView().login(user=source.user)

        return template("missions/show.html.j2", mission=mission, with_solution=with_solution)


    def _load_mission(self, mission_name):
        # WIP - pravděpodobně přesunout do json

        # Password guessing
        if mission_name == "password_guesser":
            # Define mission info
            mission = Mission(
                id=1,
                name="Uhodni Frantovo heslo na Facebook",
                info="""
                    Představ si, že sis nechal ve škole na počítači přihlášený svůj Facebook účet a tvůj kamarád Martin to využil, aby si z tebe udělal srandu.<br>
                    Napsal na tvůj profil ošklivej příspěvek, a než sis toho všiml, několik lidí už to okomentovalo a pak se ti smáli.<br>
                    Rád bys to Martinovi vrátil. Dával jsi pozor, jestli taky někdy nezapomene přihášení na školním počítači, ale dává si na to pozor.<br>
                    Tak tě napadlo, že zkusíš uhodnout jeho heslo, a tak se mu na profil dostat.<br> 
                    <p>
                    <hr>
                    Jak na to?<br>
                    Vzpomněl sis, že vám na informatice váš učitel jednou říkal o tom, jak snadný hesla si často lidi vymýšlí.<br>
                    Že často používají svoje jméno, jméno někoho z rodiny, nebo třeba domácího mazlíčka.<br>
                    Taky víš, že po tobě Facebook chce, abys měl v hesle velký písmeno a nějaký číslo.<br>
                    Hm, jaký číslo by si tam mohl dát? A kam - na začátek, doprostřed, nakonec?<br>
                    A co se zkusit podívat na nějaký Frantovy facebookový statusy, třeba nám to poradí...
                    """,
                solution="""
                    Super, přišel jsi na to, jak odhalit Frantovo heslo. Bylo by fajn Frantovi říct, aby si ho změnil na něco lepšího, protože příště by se mu do účtu mohl dostat někdo, kdo by udělal něco fakt zlýho.<br>
                    A možná nejenom do tohohle účtu...<br>
                    <hr>
                    A co ty?<br>
                    Máš na svém účtu lepší heslo?<br>
                    A kdyby někdo nějak zjistil jedno tvoje heslo, dostane se i do dalších účtů?<br>

                    <hr>

                    Pokud si nejsi jistý, radši si to zjisti a do budoucna pohlídej.<br>
                    Pomoct ti může několik rad, jak se svými hesly zacházet:<br>
                    <ul>
                        <li><strong>Heslo by mělo být dostatečně dlouhé.</strong></li>
                            Pak jsi víc chráněn před tím, když někdo zkouší všechny kombinace písmen (říká se tomu <em>brute force attack</em>).
                            Doporučovaná délka záleží na spoustě věcech, ale dá se říct, že pokud budeš používat jenom písmena, mělo by mít heslo třeba 25 znaků, pokud používáš i čísla a znaky, může stačit kolem deseti - proto taky často někde chtějí, aby heslo obsahovalo číslo a znak (ale sami jsme viděli, jak to funguje). 
                        <li><strong>Heslo musí být náhodné</strong></li>
                            Pokud je heslo celé nebo z většiny existujícím slovem (větou, souslovím), výrazně to snižuje jeho
                            bezpečnost. Heslo by mělo být náhodné – buď řetězec náhodných znaků, nebo (lépe zapamatovatelné) kombinace více náhodně vybraných slov.
                        <li><strong>Heslo musí být unikátní</strong></li>
                            Pokud používáš stejné heslo pro více účtů, při úniku hesla (a to se prostě stává) je ohrožení větší. Je tedy zásadní mít odlišná hesla v různých službách.
                    </ul>

                    Tak snad už máš lepší představu, jak se starat o svoje hesla.<br>
                    <hr>

                    A ještě jedna věc - <strong style="color:red;">ve skutečném světě nezkoušej hádat hesla ostatních lidí</strong>. Kdyby ses jim bez jejich vědomí přihlásil do účtu, porušuješ tím zákon!<br>
                    Tady jsme si to mohli vyzkoušet, abychom viděli, že se něco takového může stát.


                """
            )

            # Define data sources
            facebook_user = FacebookUser(
                full_name="František Ryba",
                password="Bramburek99",
                phone_number="733264215",
                e_mail="franta.ryba@seznam.cz",
                profile_picture_path="mission_data/password_guesser/photos/profile.jpg",
            )
            facebook_user.posts = [
                FacebookPost(
                    text=f"Nejlepší narozeniny, je mi 22.",
                    picture_path="mission_data/password_guesser/photos/birthday_cake.jpg",
                    created_at=datetime.datetime(2021, 3, 21, 15, 12, 1),
                ),
                # FacebookPost.random_post(),
                FacebookPost(
                    text=f"Konečně mi rodiče dovolili psa! Jmenuje se Brambůrek a je rozkošnej.",
                    picture_path="mission_data/password_guesser/photos/dog.jpg",
                    created_at=datetime.datetime(2020, 12, 6, 10, 13, 56),
                ),
                FacebookPost(
                    text=f"Smazaly se mi kontakty v telefonu, tak pokud chcete, abych si vás přidal, ozvěte se mi na 733264215",
                    created_at=datetime.datetime(2019, 2, 16, 16, 0, 0),
                ),
            ]
            mission.data_sources = [MissionItem(name="facebook", user=facebook_user)]
            # mission.data_sources["facebook"]["user"] = facebook_user

            # Define action pages
            mission.actions = [
                MissionItem(
                    name="facebook_login", human_name="Zadat heslo", user=facebook_user,
                )
            ]

        else:
            abort(404)

        return mission
