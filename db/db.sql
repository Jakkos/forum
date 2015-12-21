CREATE TABLE forum(
id_forum INT(3) NOT NULL AUTOINCREMENT,
theme CHAR(50) NOT NULL,
PRIMARY KEY(id_forum)
)DEFAULT CHARSET=utf8;

CREATE TABLE utilisateur(
id_utilisateur INT(3) NOT NULL AUTOINCREMENT,
pseudo CHAR(50) NOT NULL,
password CHAR(25) NOT NULL,
PRIMARY KEY(id_utilisateur)
)DEFAULT CHARSET=utf8;

CREATE TABLE message(
id_message INT(3) NOT NULL AUTOINCREMENT,
id_utilisateur INT(3) NOT NULL,
id_forum INT(3) NOT NULL,
texte CHAR(50) NOT NULL,
date_message DATETIME NOT NULL,
PRIMARY KEY(id_message),
FOREIGN KEY(id_utilisateur) REFERENCES utilisateur(id_utilisateur)
FOREIGN KEY(id_forum) REFERENCES forum(id_forum)
)DEFAULT CHARSET=utf8;

CREATE TABLE abonnement(
id_utilisateur INT(3) NOT NULL,
id_forum INT(3) NOT NULL,
PRIMARY KEY(id_utilisateur,id_forum),
FOREIGN KEY(id_utilisateur) REFERENCES utilisateur(id_utilisateur),
FOREIGN KEY(id_forum) REFERENCES forum(id_forum)
)DEFAULT CHARSET=utf8;