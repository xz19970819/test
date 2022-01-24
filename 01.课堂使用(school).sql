
create database if not exists school ;

use school ;

drop table IF EXISTS students;

create table students(
	studentNo int primary key auto_increment,
	`name` varchar(10),
	age int(3),
	sex enum('男','女'),
	class VARCHAR(5),
	card VARCHAR(20),
	city VARCHAR(10)
) ;

insert into students(studentNo,`name`,age,sex,class,card,city) values(1,'嬴政',52,'男','2班','1000200030004000','上海');
insert into students(studentNo,`name`,age,sex,class,card,city) values(2,'韩非子',29,'女','3班','1000200030003000','天津');
insert into students(studentNo,`name`,age,sex,class,card,city) values(3,'王剪',27,'女','4班','1000200030002000','河南');
insert into students(studentNo,`name`,age,sex,class,card,city) values(4,'刘邦',29,'男','5班','1000200030004000','北京');
insert into students(studentNo,`name`,age,sex,class,card,city) values(5,'韩信',32,'男','1班','','河北');
insert into students(studentNo,`name`,age,sex,class,card,city) values(6,'项宇',30,'女','5班','1000200030005000','天津');
insert into students(studentNo,`name`,age,sex,class,card,city) values(7,'李红广',40,'男','5班','1000200030008000','上海');
insert into students(studentNo,`name`,age,sex,class,card,city) values(8,'刘彻',39,'男','2班','1000200030007000','广州');
insert into students(studentNo,`name`,age,sex,class,card,city) values(9,'韩王',28,'女','6班',null,'上海');
insert into students(studentNo,`name`,age,sex,class,card,city) values(10,'韩大夫',21,'女','7班','1000200030009000','山东');
insert into students(studentNo,`name`,age,sex,class,card,city) values(11,'霍去病',29,'男','8班','1000200020004000','广州');
insert into students(studentNo,`name`,age,sex,class,card,city) values(12,'萧何',36,'男','3班','1000200030006000','上海');

drop table IF EXISTS scores;
create table scores(
studentNo int(3),
score int(3),
courseNo int(2)
);

insert into scores(studentNo,score,courseNo) values(1,90,1) ;
insert into scores(studentNo,score,courseNo) values(1,87,2) ;
insert into scores(studentNo,score,courseNo) values(1,92,1) ;
insert into scores(studentNo,score,courseNo) values(2,95,3) ;
insert into scores(studentNo,score,courseNo) values(2,75,4) ;
insert into scores(studentNo,score,courseNo) values(2,87,5) ;
insert into scores(studentNo,score,courseNo) values(3,77,2) ;
insert into scores(studentNo,score,courseNo) values(3,57,1) ;
insert into scores(studentNo,score,courseNo) values(3,87,3) ;
insert into scores(studentNo,score,courseNo) values(1,90,6) ;
insert into scores(studentNo,score,courseNo) values(2,82,5) ;
insert into scores(studentNo,score,courseNo) values(3,98,4) ;
insert into scores(studentNo,score,courseNo) values(2,83,7) ;
insert into scores(studentNo,score,courseNo) values(3,67,3) ;
insert into scores(studentNo,score,courseNo) values(3,75,2) ;


-- ===================================================================

drop table if EXISTS courses ;
create table courses(
	courseNo int PRIMARY key auto_increment,
	coursename varchar(20)
) ;

insert into courses(coursename) values('测试基础') ;
insert into courses(coursename) values('数据库') ;
insert into courses(coursename) values('python') ;
insert into courses(coursename) values('linux') ;
insert into courses(coursename) values('功能测试') ;
insert into courses(coursename) values('接口测试') ;
insert into courses(coursename) values('性能测试') ;
insert into courses(coursename) values('自动化测试') ;
