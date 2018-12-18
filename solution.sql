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

DROP TABLE IF EXISTS scrore;
CREATE TABLE scrore(
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
  id_joueyr integer,
  nb_joueur integer

);

DROP TABLE IF EXISTS partie ;
CREATE TABLE partie(
  id_partie integer primary key AUTO_INCREMENT,
  id_joueur integer,
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
  typ_jeu varchar(5),
  pegi integer
);

