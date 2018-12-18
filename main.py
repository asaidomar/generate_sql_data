# -*- coding: utf-8; -*-
#

import random
import string
import datetime

import sys

MAX_USERS = 300
MAX_STUDENT = 3000

USERS="""Tora Towner  
Carline Frisch  
Meredith Asencio  
Pamula Merrick  
Juliana Josey  
Evelia Askey  
Veronique Fouch  
Lino Thurmond  
Margorie Twiford  
Akiko Segovia  
Deetta Mccurley  
Sima Haig  
Karren Mayne  
Eddie Montag  
Tad Asaro  
Rufus Elsberry  
Maximina Bastien  
Marchelle Difilippo  
Classie Chiang  
Tu Letchworth  
Kenia Patao  
Haywood Coley  
Erin Kirsh  
Christoper Goetzinger  
Rita Mulvey  
Terrell Pleas  
Wanita Crenshaw  
Isela Bertone  
Josephine Boudreaux  
Christinia Burgett  
Harriet Bliss  
Neta Bickham  
Darcy Vasquez  
Francene Boyles  
Manie Ballerini  
Rafael Emmons  
Nelson Landen  
Joselyn Mcelrath  
Karly Westfield  
Lillia Zahl  
Anamaria Duffer  
Keli Sartor  
Monika Baro  
Pearline Moad  
Parthenia Trivett  
Barb Chittenden  
Emogene Withey  
Carolynn Staller  
Janey Sparks  
Kimiko Danziger
Idella Frase  
Valrie Selden  
Stasia Holdeman  
Page Bosak  
Lajuana Catoe  
Joaquin Keech  
Ulysses Molton  
Dorthey Stegall  
Luann Braz  
Elmira Hamlin  
Janiece Lorenzana  
Vincenzo Master  
Mercy Oelke  
Halina Pisano  
Britni Pineo  
Robyn Mcquaid  
Esta Plumber  
Mina Kolman  
Graig Neuhaus  
Margareta Mathers  
Stephany Stonebraker  
Saturnina Teasley  
Ed Haymaker  
Caryn Pickles  
Daniela Guse  
Gabriella Dahn  
Laquanda Sytsma  
Boyd Ranger  
Stefania Grays  
Wallace Rudy  
Sandie Haith  
Ricardo Maddock  
Ayesha Redmond  
Piedad Leggio  
Hettie Rardin  
Arica Winder  
Eileen Dolloff  
Ilona Jovel  
Maren Hanzlik  
Jamel Luna  
Kathleen Speight  
Stanford Cooney  
Miriam Aarons  
Dulcie Staff  
Rosalba Rutigliano  
Carmelita Steil  
Lincoln Abell  
Gerda Scheck  
Kazuko Sears  
Shanti Saucier"""

NAMES = USERS.split()
MAX_END_INT = 2000
MAX_PLAYER = 100
MAX_PARTIE_PAR_JEUX = 10
MAX_JOUEUR_PAR_ROOM = 10

def generate_name(nb_name=1):
    result = list()
    for _ in range(int(nb_name)):
        result.append(random.choice(NAMES))
    return result


def generate_int(start=1, end=2000, nb_int=1):
    result = list()
    for _ in range(int(nb_int)):
        result.append(random.randint(start, end))
    return result


def generate_date(number_of_day=0, max_year=5, nb_date=1, from_date=datetime.datetime.now()):
    result = list()
    previous_date = None
    for i in range(int(nb_date)):
        number_of_days = int(number_of_day) or random.randint(1, 365 * max_year)
        if previous_date is None:
            past_day_obj = from_date - datetime.timedelta(days=number_of_days)
        else:
            # up to 180 minutes
            past_day_obj = previous_date + datetime.timedelta(minutes=random.randint(1, 60 * 3))

        past_day_str = past_day_obj.strftime("%Y-%m-%d %H:%M:%S")
        result.append(past_day_str)
        previous_date = past_day_obj
    return result


def loop_and_call(start=0, end=MAX_END_INT):
    for i in range(start, end):
        pass
        # print(i)


def convert_list_to_str(*lists, sep=","):
    """

    permet de convertir une liste de liste en str

    >>> convert_list_to_str(["me", "Saucier"], [1985, 1983], ["2014-08-14 18:04:08", "2014-08-14 18:04:08"])
    '"'me','Saucier','1985','1983','2014-08-14 18:04:08','2014-08-14 18:04:08'"'

    :param lists:
    :param sep:
    :return:
    """
    result = list()
    for l in lists:
        result.extend(l)
    return sep.join([repr(str(s)) for s in result if s])


def generate_player(nb_player=MAX_PLAYER):
    heade_tab = ["id_player", "speudo", "mdp", "prenom", "nom", "date_naissance", "sexe"]
    for i in range(1, nb_player):
        names = generate_name(nb_name=4)
        random_age = random.randint(11, 35)
        from_date = (datetime.datetime.now() - datetime.timedelta(days=365 * random_age))
        date_ = generate_date(nb_date=1, from_date=from_date)
        # score = generate_int(start=1, end=10, nb_int=1)
        sexe = random.choice(["M", "F"])
        row = convert_list_to_str([i], names, date_, sexe, sep="\t")
        print(row)


def generate_partie(nb_jeu=871):
    ids_room = list()
    heade_tab = ["id_partie", "id_room", "date_start", "date_end"]
    part_file = open("partie.csv", mode="w")
    for i in range(1, nb_jeu):
        nb_partie = random.randint(1, MAX_PARTIE_PAR_JEUX)
        for j in range(1, nb_partie):
            # names = generate_name(nb_name=2)
            id_room = "%d%d" % (i, j)
            date_s = generate_date(nb_date=2)
            # score = generate_int(start=1, end=10, nb_int=1)
            row = convert_list_to_str([i], [id_room], date_s, sep="\t")
            ids_room.append(str(id_room))
            print(row, file=part_file)
    return ids_room


def generate_room(ids_room):

    ids_joueurs = list(range(1, MAX_PLAYER))
    file_room = open("room.csv", mode="w")
    file_score = open("score.csv", mode="w")

    for partie_i, id_room in enumerate(ids_room, start=1):
        nb_joueur = random.randint(1, MAX_JOUEUR_PAR_ROOM)
        copy_ids_joueurs = ids_joueurs[:]
        for j in range(nb_joueur):
            try:
                random_index_joueur = random.choice(copy_ids_joueurs)
                copy_ids_joueurs.remove(random_index_joueur)
            except:
                random_index_joueur = 1

            row = convert_list_to_str([id_room], [random_index_joueur], [nb_joueur], sep="\t")
            print(row, file=file_room)

            score = random.randint(1, nb_joueur*1000)
            ranking = random.randint(1, nb_joueur)
            row_ranking = convert_list_to_str(
                [random_index_joueur], [partie_i], [score], [ranking], sep="\t")
            print(row_ranking, file=file_score)


def main():
    ids_room = generate_partie()
    generate_room(ids_room)


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        if sys.argv[1] == "test":
            function_name = sys.argv[2]
            try:
                funct = globals()[function_name]
                funct(*sys.argv[3:])
                exit(0)
            except TypeError as error:
                print(error, file=sys.stderr)

    main()

