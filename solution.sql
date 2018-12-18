CREATE DATABASE IF NOT EXISTS GAMES;

USE GAMES;

DROP TABLE IF EXISTS joueur;
CREATE TABLE joueur(
  id_joueur  integer primary key AUTO_INCREMENT ,
  speudo varchar(50),
  mdp varchar(50),
  prenom varchar(50),
  nom varchar(50),
  date_naissance DATE,
  sexe varchar(3)


);

DROP TABLE IF EXISTS score;
CREATE TABLE score(
  id_joueur integer,
  id_partie integer,
  score integer,
  classement integer
);


DROP TABLE IF EXISTS editeur ;
CREATE TABLE editeur(
  id_editeur integer primary key AUTO_INCREMENT ,
  nom varchar(50),
  date_creation DATE

);

DROP TABLE IF EXISTS room ;
CREATE TABLE room(
  id_room integer,
  id_joueur integer,
  nb_joueur integer

);

DROP TABLE IF EXISTS partie ;
CREATE TABLE partie(
  id_partie integer primary key AUTO_INCREMENT,
  id_room integer,
  date_debut datetime,
  date_fin datetime
);


DROP TABLE IF EXISTS jeu ;
CREATE TABLE jeu(
  id_jeu integer primary key AUTO_INCREMENT ,
  nom varchar(50),
  id_editeur integer,
  date_sortie date,
  type_jeu varchar(5),
  pegi integer
);

-- nom	genre	editeur	date_sortie
USE GAMES
DROP TABLE IF EXISTS jeu_l ;
CREATE TABLE jeu_l(
  id_jeu integer primary key AUTO_INCREMENT ,
  nom varchar(255),
  type_jeu varchar(60),
  editeur varchar(200),
  date_sortie varchar(30)
);

LOAD DATA LOCAL INFILE "/Users/alisaidomar/generate_sql_data/game_new.txt"
  INTO TABLE jeu_l
  COLUMNS TERMINATED BY "\t"
  OPTIONALLY ENCLOSED BY "'"
  LINES TERMINATED BY "\n"
  IGNORE 1 LINES
  (nom, type_jeu, editeur, date_sortie);

TRUNCATE TABLE joueur;
LOAD DATA LOCAL INFILE "/Users/alisaidomar/generate_sql_data/player.csv"
  INTO TABLE joueur
  COLUMNS TERMINATED BY "\t"
  OPTIONALLY ENCLOSED BY "'"
  LINES TERMINATED BY "\n"


TRUNCATE TABLE score;
LOAD DATA LOCAL INFILE "/Users/alisaidomar/generate_sql_data/score.csv"
  INTO TABLE score
  COLUMNS TERMINATED BY "\t"
  OPTIONALLY ENCLOSED BY "'"
  LINES TERMINATED BY "\n"


TRUNCATE TABLE partie;
LOAD DATA LOCAL INFILE "/Users/alisaidomar/generate_sql_data/partie.csv"
  INTO TABLE partie
  COLUMNS TERMINATED BY "\t"
  OPTIONALLY ENCLOSED BY "'"
  LINES TERMINATED BY "\n"
 (id_room, date_debut, date_fin)

TRUNCATE TABLE room;
LOAD DATA LOCAL INFILE "/Users/alisaidomar/generate_sql_data/room.csv"
  INTO TABLE room
  COLUMNS TERMINATED BY "\t"
  OPTIONALLY ENCLOSED BY "'"
  LINES TERMINATED BY "\n"


-- calcul to top X