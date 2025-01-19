create schema if not exists english_tutor;

drop table if exists english_tutor.user;

create table english_tutor.et_test_user (
	id uuid primary key, 
	phone text, 
	crm text, 
	telephony text,
	telegram_id int
);

