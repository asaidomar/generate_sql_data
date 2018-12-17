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


def generate_date(number_of_day=0, max_year=5, nb_date=1):
    result = list()
    for _ in range(int(nb_date)):
        number_of_days = int(number_of_day) or random.randint(1, 365 * max_year)
        past_day_obj = datetime.datetime.now() - datetime.timedelta(days=number_of_days)
        past_day_str = past_day_obj.strftime("%Y-%m-%d %H:%M:%S")
        result.append(past_day_str)
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


def generate_player(nb_player=100):
    heade_tab = ["name", "alias", "date", "score"]
    for i in range(nb_player):
        names = generate_name(nb_name=2)
        date_ = generate_date(nb_date=1)
        score = generate_int(start=1, end=10, nb_int=1)
        row = convert_list_to_str([i], names, date_, score, sep="\t")
        print(row)


def main():
    generate_player()


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
