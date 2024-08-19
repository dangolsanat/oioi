--
-- PostgreSQL database dump
--

-- Drop existing sequences
DROP SEQUENCE IF EXISTS chats_id_seq;
DROP SEQUENCE IF EXISTS full_user_id_seq;
DROP SEQUENCE IF EXISTS messages_id_seq;
DROP SEQUENCE IF EXISTS post_images_id_seq;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Drop existing tables
DROP TABLE IF EXISTS public.chats;
DROP TABLE IF EXISTS public.full_user;
DROP TABLE IF EXISTS public.messages;
DROP TABLE IF EXISTS public.post_images;
DROP TABLE IF EXISTS public.posts;
DROP TABLE IF EXISTS public.users;

-- Create tables

CREATE TABLE public.users (
    id serial PRIMARY KEY,
    username character varying NOT NULL UNIQUE,
    password character varying NOT NULL
);

CREATE TABLE public.posts (
    id serial PRIMARY KEY,
    title character varying(50) NOT NULL,
    description text NOT NULL,
    address character varying(100) NOT NULL,
    neighbor character varying(50) NOT NULL,
    borough character varying(20) NOT NULL,
    price integer NOT NULL,
    neighborhood text NOT NULL,
    user_id integer NOT NULL REFERENCES public.users(id)
);

CREATE TABLE public.post_images (
    id serial PRIMARY KEY,
    file_name character varying(255) NOT NULL,
    post_id integer NOT NULL REFERENCES public.posts(id)
);

CREATE TABLE public.full_user (
    id serial PRIMARY KEY,
    first_name character varying(25) NOT NULL,
    last_name character varying(25) NOT NULL,
    email text NOT NULL UNIQUE,
    user_image text,
    dob date NOT NULL,
    bio character varying(250),
    intro text,
    user_id integer NOT NULL REFERENCES public.users(id)
);

CREATE TABLE public.messages (
    id serial PRIMARY KEY,
    sender_id integer NOT NULL REFERENCES public.users(id),
    receiver_id integer NOT NULL REFERENCES public.users(id),
    content text NOT NULL,
    "timestamp" timestamp without time zone NOT NULL
);

CREATE TABLE public.chats (
    id serial PRIMARY KEY,
    user_id1 integer NOT NULL REFERENCES public.users(id),
    user_id2 integer NOT NULL REFERENCES public.users(id)
);

-- Insert data

COPY public.users (id, username, password) FROM stdin WITH (FORMAT csv, DELIMITER E'\t', NULL 'NULL');
1	dexter	securepassword
2	bubbles	securepassword
3	courage	securepassword
4	moomin	securepassword
5	jerry	securepassword
6	cartman	securepassword
7	morty	securepassword
8	lisa	securepassword
9	spongebob	securepassword
10	edd	securepassword
11	tom	securepassword
12	bugs	securepassword
\.

COPY public.posts (id, title, description, address, neighbor, borough, price, neighborhood, user_id) FROM stdin WITH (FORMAT csv, DELIMITER E'\t', NULL 'NULL');
1	Dexter's Lab	Cozy studio apartment	1234 Elm St, New York, NY	Elmhurst	Queens	1500	Quiet and charming	1
2	Bubbles' Room	Charming 2-bedroom apartment	5678 Oak Ave, Brooklyn, NY	Prospect Lefferts Gardens	Brooklyn	2000	Spacious and modern	2
3	Courage's Place	Affordable room for rent	3456 Maple Rd, Manhattan, NY	Upper West Side	Manhattan	1200	Convenient and accessible	3
4	Moomin's Den	Quaint studio apartment	7890 Pine Blvd, Brooklyn, NY	Brooklyn Heights	Brooklyn	1700	Homey and comfortable	4
5	Jerry's Loft	Modern loft with a view	2345 Birch St, Queens, NY	Forest Hills	Queens	2200	Great city views	5
6	Edd's Crib	Spacious apartment with amenities	6789 Cedar Ave, Bronx, NY	North Bronx	Bronx	2500	Convenient location	6
7	Morty's Pad	Cheap room available	1234 Willow St, Queens, NY	Astoria	Queens	1300	Affordable and well-located	7
8	Lisa's Flat	Stylish apartment in the heart of the city	5678 Maple St, Manhattan, NY	Midtown	Manhattan	2300	Central and convenient	8
9	SpongeBob's House	Beachside cottage	9012 Ocean Blvd, Coney Island, NY	Coney Island	Brooklyn	1800	Sea views and fresh air	9
10	Edd's New Place	Large apartment with modern features	3456 Elm St, Brooklyn, NY	Flatbush	Brooklyn	2400	Contemporary and spacious	10
11	Tom's Loft	Cosy studio with modern amenities	2345 Oak St, Brooklyn, NY	Prospect Park	Brooklyn	1700	Charming and convenient	11
12	Bugs' Bungalow	Charming house with a garden	6789 Pine St, Manhattan, NY	Upper East Side	Manhattan	1900	Cozy and peaceful	12
\.

COPY public.post_images (id, file_name, post_id) FROM stdin WITH (FORMAT csv, DELIMITER E'\t', NULL 'NULL');
1	dex1.jpg	1
2	dex2.jpg	1
3	dex3.jpg	1
4	dex4.jpg	1
5	bubbles.jpg	2
6	edd.webp	6
7	edd2.webp	6
8	edd3.webp	6
9	edd4.webp	6
10	edd5.webp	6
11	tom2.jpg	11
12	bugs1.jpg	12
13	bugs2.jpg	12
14	bugs3.jpg	12
15	bugs4.jpg	12
\.

COPY public.full_user (id, first_name, last_name, email, user_image, dob, bio, intro, user_id) FROM stdin WITH (FORMAT csv, DELIMITER E'\t', NULL 'NULL');
1	Dexter	McPherson	dexter@lab.com	https://cdn.costumewall.com/wp-content/uploads/2015/09/dexters-laboratory-costume.jpg	1990-03-24	This is Dexter's bio. I am a very passionate scientist. I like to do the dance with dee dee	I'm from small-town TN and moved to NYC for school; now working in financial planning. I've been here 8 years now, 5.5 of them living in this apartment. I'm very laid-back, enjoy both socializing and having time to myself, and try to keep the vibes good and the energy positive. Interests include gaming (video/card/board/etc.), tennis/ping pong/badminton, hiking, baking, mixology, reading, jamming out and building playlists, introspection/spirituality, and good times and conversations had in pubs.	1
2	Bubbles	Utonium	bubbles@powerpuff.com	https://i.ebayimg.com/images/g/kU4AAOSwpFxko1mu/s-l1200.jpg	1992-11-21	This is Bubble's bio	Hey there! I'm Tiffany, 32, I'm a transplant to the city from Charleston, SC. I'm easy going, always clean up after myself and live a relatively calm life at home. I enjoy cooking for my roommates on occasion and love to have a few friends over for chill dinner hangs.Lover of art, photography, music, coffee, biking and brews. @wolterpynaffit	2
3	Courage	Bagge	courage@cowardlymail.com	https://miro.medium.com/v2/resize:fit:1400/1*hDYUPYiUe0Nfcb9xIhdKKw.jpeg	1979-04-23	This is Courage's bio	\N	3
4	Moomin	Chubs	mooumin@example.com	https://yt3.googleusercontent.com/V9sqo4C6K-sbjDogTQdWLiyviw2MyGWPiHLjoF3Us71MKb677V3SQ8KqhorzqHMplgedG6iy=s900-c-k-c0x00ffffff-no-rj	1975-03-03	This is moumin's bio	\N	4
5	Jerry	Mousey	jerry@example.com	https://i.pinimg.com/736x/a5/96/d9/a596d930bcaadb46e5e138189bcd5245.jpg	1975-03-03	This is jerry's bio	\N	5
6	Eric	Cartman	cartoman@southpark.com	https://shorturl.at/jkD28	1981-03-03	This is Eric Cartman's bio	\N	6
7	Morty	Smith	morty@example.com	https://i.imgur.com/gTdmQmY.jpg	1992-12-12	This is Morty's bio	\N	7
8	Lisa	Simpson	lisa@example.com	https://i.imgur.com/sdcrxiD.jpg	1988-01-01	This is Lisa Simpson's bio	\N	8
9	SpongeBob	SquarePants	spongebob@example.com	https://i.imgur.com/cxFcXU0.jpg	1990-07-14	This is SpongeBob's bio	\N	9
10	Edd	Adams	edd@example.com	https://i.imgur.com/kLf7V77.jpg	1990-07-14	This is Edd's bio	\N	10
11	Tom	Mouse	tom@example.com	https://i.imgur.com/7cFczqA.jpg	1985-09-01	This is Tom Mouse's bio	\N	11
12	Bugs	Bunny	bugs@example.com	https://i.imgur.com/foU0Hq9.jpg	1980-01-01	This is Bugs Bunny's bio	\N	12
\.

COPY public.messages (id, sender_id, receiver_id, content, "timestamp") FROM stdin WITH (FORMAT csv, DELIMITER E'\t', NULL 'NULL');
1	1	2	Hi Bubbles, I'm interested in your room.	2024-08-11 23:00:00
2	2	1	Hi Dexter, I appreciate your interest.	2024-08-12 00:00:00
3	3	4	Hi Moomin, I saw your ad and I'm interested.	2024-08-12 01:00:00
4	4	3	Hi Courage, I'd love to show you the apartment.	2024-08-12 02:00:00
5	5	6	Hi Edd, I like your loft.	2024-08-12 03:00:00
6	6	5	Hi Jerry, I'm glad you like it.	2024-08-12 04:00:00
7	7	8	Hi Lisa, I saw your listing and I'm interested.	2024-08-12 05:00:00
8	8	7	Hi Morty, I'll send you more details.	2024-08-12 06:00:00
9	9	10	Hi Edd, I have some questions about the apartment.	2024-08-12 07:00:00
10	10	9	Hi SpongeBob, I'd be happy to answer your questions.	2024-08-12 08:00:00
\.

COPY public.chats (id, user_id1, user_id2) FROM stdin WITH (FORMAT csv, DELIMITER E'\t', NULL 'NULL');
1	1	2
2	3	4
3	5	6
4	7	8
5	9	10
\.
