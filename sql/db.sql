CREATE DATABASE db; 

USE db;

CREATE TABLE personne(
    Id int not null AUTO_INCREMENT , 
    Nom VARCHAR(15) not null,
    Prenom VARCHAR(15) not null,
    PRIMARY key (Id)
);

INSERT INTO personne(Nom, Prenom)
VALUES("Gauvin", "Ludal"), ("Gauvin", "Kilyan");