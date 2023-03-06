
create table "pizza-warehouse" 
("id" SERIAl primary key,
"ingredient" varchar not null,
"brand" varchar not NULL,
"quantity/(kg)" INT NOT NULL,
"create_at " TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP) ; 



