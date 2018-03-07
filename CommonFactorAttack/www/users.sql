-- Create table with `cat users.sql | sqlite3 users.db`

drop table if exists users;
drop table if exists messages;

create table users(
  id integer primary key autoincrement,
  name text,
  n integer,
  e integer
);

create table messages(
  id integer primary key autoincrement,
  content text,
  user_id integer,
  foreign key(user_id) references users(id)
);

insert into users(name, n, e) values('Félix', 1, 2);
