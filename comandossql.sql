#Inseri aluno
INSERT INTO aluno (Nome, Matricula, SemestreAtual, Idade, Curso_idCurso) 
values('Matheus', 1019, 7, 22, 1);

#inseri o curso
insert into curso (Nome, HorasDuracao) values ('Eng Computacao', 700);
insert into curso (Nome, HorasDuracao) values ('Eng Biomedica', 700);
insert into curso (Nome, HorasDuracao) values ('Eng Telecomunicacoes', 700);

#inseri materia
insert into materia (Nome,NumAulas) values ('Banco de dados', 40);
insert into materia (Nome,NumAulas) values ('Antenas', 60);
insert into materia (Nome,NumAulas) values ('Anatomia', 80);

#vincula materia com curso
insert into curso_has_materia (Curso_idCurso,Materia_idMateria) 
values (1, 3);
insert into curso_has_materia (Curso_idCurso,Materia_idMateria) 
values (2, 2);
insert into curso_has_materia (Curso_idCurso,Materia_idMateria) 
values (3, 1);

#inseri nota em aluno e materia
insert into nota (NP1,NP2,Aluno_idAluno,Materia_idMateria) 
values (60, 100, 2, 1);


select * from aluno;
select * from materia;
select * from curso;
select idCurso, curso.nome from curso;
select * from curso_has_materia;
select * from nota;

#seleciona nome pertecentes aos cursos (pega todos)
select materia.Nome, curso.Nome from materia  
inner join curso_has_materia on Materia_idMateria = idMateria
inner join curso on Curso_idCurso = curso.idCurso;

#seleciona nome pertecentes aos cursos (pega todos)
select materia.Nome, curso.Nome from materia  
inner join curso_has_materia on Materia_idMateria = idMateria
inner join curso on Curso_idCurso = curso.idCurso;

#seleciona materia que o aluno faz (pega o especifico do aluno com id 2) 
select materia.Nome, aluno.Nome from materia  
inner join aluno_has_materia on Materia_idMateria = idMateria
inner join aluno on Aluno_idAluno = 2;

#seleciona nota da materia de um aluno (pega especifico do aluno com id 2)
select NP1, NP2, NP3, NF, Situacao,aluno.nome, materia.Nome from nota
inner join aluno on aluno.idAluno = 2
inner join materia on materia.idMateria = Materia_idMateria;

#seleciona aluno e o curso que faz
select aluno.Nome, Matricula, SemestreAtual, Idade, curso.Nome from aluno
inner join curso on curso.idCurso = Curso_idCurso;








