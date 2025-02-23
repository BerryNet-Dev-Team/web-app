-- Connect to DB --
\c docker

-- INSERT FIRST USER AND ITS REQUESTS --
INSERT INTO public.roles("id", "name")
VALUES (1, 'SUPERADMIN');

-- DONT FORGET ENCRYPTING THE PASSWORD sha256 --
INSERT INTO public.users("name", "lastName", "email", "password", "roleId")
VALUES ('SUPERADMIN', 'SUPER', 'test@testing.com', 'Pass$612345', 1);
