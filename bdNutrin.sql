CREATE DATABASE Nutrin
go 
USE Nutrin
GO

CREATE TABLE Paciente(ID int  identity not null,
Nome varchar(50) not null,
Idade TINYINT not null,
Sexo char not null,
Profisao VARCHAR(30),
dataNascimento DATE not null,
Cpf int not NULL,
Telefone varchar(11),
Celular VARCHAR(11),
CONSTRAINT Paciente_PK PRIMARY KEY (ID))
GO

CREATE TABLE Atendimento(ID int identity not null,
idPaciente int not null,
Servico varchar(30)not null,
Preco float not null,
qtdRetorno TINYINT not null,
CONSTRAINT Atendimento_PK PRIMARY KEY (ID,idPaciente),
CONSTRAINT Atendimento_FK foreign KEY (idPaciente)
REFERENCES Paciente (ID))
GO

CREATE TABLE Agenda(ID int identity not null,
idPaciente int not null,
dataConsulta DATE not null,
Horario time not null,
Pagamento boolean,
CONSTRAINT Agenda_PK PRIMARY KEY(ID,idPaciente),
CONSTRAINT Agenda_FK foreign KEY (idPaciente)
REFERENCES Paciente (ID))

CREATE TABLE Consulta (ID int identity not null,
idPaciente int not null,
idAtendimento int not null,
idAgenda int not null,
Objetivo VARCHAR(100)not null,
CONSTRAINT Consulta_PK PRIMARY key (ID,idAgenda,idAtendimento,idPaciente),
CONSTRAINT Consulta_Paciente_FK foreign key(idAgenda)
REFERENCES Paciente(ID),
CONSTRAINT Consulta_Agenda_FK FOREIGN key  (idAgenda)
REFERENCES Agenda (id),
constraint Consulta_Atendimento_FK foreign key (idAtendimento)
REFERENCES Atendimento (ID))
GO

CREATE TABLE AvalicaoFisica(ID int identity not null,
idConsulta int not null,
pesoInicial float not null,
pesoAtual float not null,
programaFisico varchar(100)not null,
constraint AvalicaoFisica_PK PRIMARY key(ID,idConsulta),
constraint AvalicaoFisica_FK foreign key(idConsulta)
REFERENCES Consulta(ID))
GO

CREATE TABLE PlanejamentoAlimentar(ID int identity not null,
idAvaliacaoFisica int not null,
Alimentos varchar(100)not null,
Bebidas varchar(100)not null,
kiloCaloriasDia float not null,
constraint PlanejamentoAlimentar_PK PRIMARY key(ID,idAvaliacaoFisica),
constraint PlanejamentoAlimentar_FK foreign key(idAvaliacaoFisica)
REFERENCES AvalicaoFisica(ID))
GO

CREATE TABLE FichaPaciente(ID int identity not null,
qtdRetorno TINYINT not null,
idPaciente int not null,
idAvaliacaoFisica int not null,
idPanejamentoAlimentar int not null,
constraint FichaPaciente_PK PRIMARY key(ID,idPaciente,idAvaliacaoFisica,idPanejamentoAlimentar),
CONSTRAINT FichaPaciente_Paiente_FK foreign key(idPaciente)
REFERENCES Paciente(ID),
constraint FichaPaciente_AvaliacaoFisica_FK foreign key(idAvaliacaoFisica)
REFERENCES AvalicaoFisica (ID),
constraint FichaPaciente_PanejamentoAlimentar_FK foreign key(idPanejamentoAlimentar)
REFERENCES PlanejamentoAlimentar (ID))
go