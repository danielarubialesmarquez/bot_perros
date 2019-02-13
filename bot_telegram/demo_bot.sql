CREATE DATABASE perros;

USE perros;

CREATE TABLE raza(
    nombre varchar(25) NOT NULL PRIMARY KEY ,
    mensaje text NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

 
INSERT INTO raza (nombre, mensaje) VALUES
('labrador ',
'El Labrador Retriever siempre querra jugar zambullirse en el agua y lamernos la cara debes tener cuidado porque suelen sufrir obesidad por ser tan glotones en el mismo lugar del ranking estan tambien unos primos los Golden Retriever conocidos por su pelaje dorado y largo'),

('pastor Aleman',
'Los origenes de esta raza sajona necesitan un amo que haga de lider para ensenarle la socializacion y el entrenamiento de obediencia son fundamentales desde corta edad el Pastor Aleman es muy protector y atacara si la vida de sus seres queridos esta en peligro'),


('beagle',
'talla mediana y fue lanzado al estrellato debido al dibujo animado Snoopy El Beagle es originario de Gran Bretanaa se emplea en tareas de deteccion de drogas y explosivos por la policia Es un canino bastante tolerante con otros perros y muy tranquilo afectuoso y jugueton'),

('yorkshire Terrier',
'es muy energico y a pesar de su tamano ha demostrado ser bastante valiente Aunque sea algo territorial puede vivir con otras mascotas Es afectuoso con sus duenos y desconfiado con los extranos Si no se lo adiestra desde cachorro puede estar continuamente estresado y ansioso'),

('boxer',
'Es un animal muy jugueton y amigable siendo una ninera perfecta por su tolerancia y paciencia Le gusta saltar sobre las personas y se lleva bien con otras mascotas'),

('weimaraner ',
'El braco de Weimar es un perro de caza especialmente dotado como perro cobrador'),

('chihuahua',
'Perro originario de mexico es una de las razas de perros mas antiguas del continente americano ademas de ser el perro mas pequeno del mundo'),

('pug',
'El doguillo ​ comunmente llamado carlino o pug es una raza canina con origen historico en China pero con el patrocinio de Reino Unido Se trata de un perro pequeno de tipo molosoide utilizado como mascota');





SELECT * FROM raza;

CREATE USER 'danibot'@'localhost' IDENTIFIED BY 'danibot.2018';
GRANT ALL PRIVILEGES ON perros.* TO 'danibot'@'localhost';
FLUSH PRIVILEGES;