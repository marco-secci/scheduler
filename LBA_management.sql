DROP DATABASE IF EXISTS  LBA_management;
CREATE DATABASE IF NOT EXISTS LBA_management;
USE LBA_management;

CREATE TABLE IF NOT EXISTS società (
    codice_società INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL
);
ALTER TABLE società AUTO_INCREMENT = 10001;

CREATE TABLE IF NOT EXISTS impianto (
    codice_impianto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(75) NOT NULL,
    cod_proprietario INT NOT NULL,
    FOREIGN KEY (cod_proprietario) REFERENCES società (codice_società)
);
ALTER TABLE impianto AUTO_INCREMENT = 20001;

CREATE TABLE IF NOT EXISTS partita (
    codice_partita INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    codice_impianto INT NOT NULL,
    codice_casa INT NOT NULL,
    codice_trasferta INT NOT NULL,
    data DATE,
    orario TIME,
    risultato_finale VARCHAR(7),
    codice_vincitrice INT,
    FOREIGN KEY (codice_impianto) REFERENCES impianto (codice_impianto),
    FOREIGN KEY (codice_casa) REFERENCES società (codice_società),
    FOREIGN KEY (codice_trasferta) REFERENCES società (codice_società),
    FOReIGN KEY (codice_vincitrice) REFERENCES società (codice_società)
);
ALTER TABLE partita AUTO_INCREMENT = 30001;

INSERT INTO società (nome) VALUES
('Virtus Segafredo Bologna'),
('Vanoli Cremona'),
('UNAHOTELS Reggio Emilia'),
('Umana Reyer Venezia'),
('Openjobmetis Varese'),
('NutriBullet Treviso'),
('Happy Casa Brindisi'),
('Givova Scafati'),
('Gevi Napoli'),
('Germani Brescia'),
('Estra Pistoia'),
('EA7 Emporio Armani Milano'),
('Dolomiti Energia Trento'),
('Carpegna Prosciutto Basket Pesaro'),
('Bertram Derthona Basket Tortona'),
('Banco di Sardegna Sassari');

INSERT INTO impianto (cod_proprietario, nome) VALUES
(10001, 'Segafredo Arena'),
(10002, 'PalaRadi'),
(10003, 'PalaBigi'),
(10004, 'Palasport Taliercio'),
(10005, 'Enerxenia Arena'),
(10006, 'PalaVerde'),
(10007, 'PalaPentassuglia'),
(10008, 'PalaMangano'),
(10009, 'PalaBarbuto'),
(10010, 'PalaLeonessa'),
(10011, 'PalaCarrara'),
(10012, 'Mediolanum Forum'),
(10013, 'BLM Group Arena'),
(10014, 'Vitifrigo Arena'),
(10015, 'PalaFerraris'),
(10016, 'PalaSerradimigni');
