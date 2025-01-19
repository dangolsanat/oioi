from app import app, db
from models import Users, Full_user, Post, PostImage, Message
from flask_bcrypt import Bcrypt
from sqlalchemy import text
from datetime import datetime
import os

bcrypt = Bcrypt()

# Ensure that the app context is available
with app.app_context():
    # Drop all tables with cascade
    db.session.execute(text('''
        DROP TABLE IF EXISTS post_images CASCADE;
        DROP TABLE IF EXISTS posts CASCADE;
        DROP TABLE IF EXISTS full_user CASCADE;
        DROP TABLE IF EXISTS users CASCADE;
        DROP TABLE IF EXISTS messages CASCADE;

    '''))
    db.session.commit()

    # Create all tables
    db.create_all()

    # Create new users
    user1 = Users(username='uone', password=bcrypt.generate_password_hash('haha').decode('utf-8'))
    user2 = Users(username='utwo', password=bcrypt.generate_password_hash('haha').decode('utf-8'))
    user3 = Users(username='uthree', password=bcrypt.generate_password_hash('haha').decode('utf-8'))
    user4 = Users(username='ufour', password=bcrypt.generate_password_hash('haha').decode('utf-8'))
    user5 = Users(username='ufive', password=bcrypt.generate_password_hash('haha').decode('utf-8'))
    user6 = Users(username='usix', password=bcrypt.generate_password_hash('haha').decode('utf-8'))
    user7 = Users(username='useven', password=bcrypt.generate_password_hash('haha').decode('utf-8'))
    user8 = Users(username='ueight', password=bcrypt.generate_password_hash('haha').decode('utf-8'))
    user9 = Users(username='unine', password=bcrypt.generate_password_hash('haha').decode('utf-8'))
    user10 = Users(username='uten', password=bcrypt.generate_password_hash('haha').decode('utf-8'))
    user11 = Users(username='ueleven', password=bcrypt.generate_password_hash('haha').decode('utf-8'))
    user12 = Users(username='utwelve', password=bcrypt.generate_password_hash('haha').decode('utf-8'))


    # Add users to session and commit
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)
    db.session.add(user6)
    db.session.add(user7)
    db.session.add(user8)
    db.session.add(user9)
    db.session.add(user10)
    db.session.add(user11)
    db.session.add(user12)

    db.session.commit()

    # Create full_user entries linked to users
    full_user1 = Full_user(
        first_name='Dexter',
        last_name='McPherson',
        email='dexter@lab.com',
        user_image='https://cdn.costumewall.com/wp-content/uploads/2015/09/dexters-laboratory-costume.jpg',
        dob='1990-03-24',
        bio='This is Dexter\'s bio. I am a very passionate scientist. I like to do the dance with dee dee',
        intro="I'm from small-town TN and moved to NYC for school; now working in financial planning. I've been here 8 years now, 5.5 of them living in this apartment. I'm very laid-back, enjoy both socializing and having time to myself, and try to keep the vibes good and the energy positive. Interests include gaming (video/card/board/etc.), tennis/ping pong/badminton, hiking, baking, mixology, reading, jamming out and building playlists, introspection/spirituality, and good times and conversations had in pubs.",
        user_id=user1.id
    )

    full_user2 = Full_user(
        first_name='Bubbles',
        last_name='Utonium',
        email='bubbles@powerpuff.com',
        user_image='https://i.ebayimg.com/images/g/kU4AAOSwpFxko1mu/s-l1200.jpg',
        dob='1992-11-21',
        bio='This is Bubble\'s bio',
        intro="Hey there! I'm Tiffany, 32, I'm a transplant to the city from Charleston, SC. I'm easy going, always clean up after myself and live a relatively calm life at home. I enjoy cooking for my roommates on occasion and love to have a few friends over for chill dinner hangs.Lover of art, photography, music, coffee, biking and brews. @wolterpynaffit",
        user_id=user2.id
    )

    full_user3 = Full_user(
        first_name='Courage',
        last_name='Bagge',
        email='courage@cowardlymail.com',
        user_image='https://miro.medium.com/v2/resize:fit:1400/1*hDYUPYiUe0Nfcb9xIhdKKw.jpeg',
        dob='1979-04-23',
        bio='This is Courage\'s bio',
        intro="",
        user_id=user3.id
    )

    full_user4 = Full_user(
        first_name='Moomin',
        last_name='Chubs',
        email='mooumin@example.com',
        user_image='https://yt3.googleusercontent.com/V9sqo4C6K-sbjDogTQdWLiyviw2MyGWPiHLjoF3Us71MKb677V3SQ8KqhorzqHMplgedG6iy=s900-c-k-c0x00ffffff-no-rj',
        dob='1975-03-03',
        bio='This is moumin\'s bio',
        intro="",
        user_id=user4.id
    )

    full_user5 = Full_user(
        first_name='Jerry',
        last_name='Mousey',
        email='jerry@example.com',
        user_image='https://i.pinimg.com/736x/a5/96/d9/a596d930bcaadb46e5e138189bcd5245.jpg',
        dob='1975-03-03',
        bio='This is jerry\'s bio',
        intro="",
        user_id=user5.id
    )

    full_user6 = Full_user(
        first_name='Eric',
        last_name='Cartman',
        email='cartoman@southpark.com',
        user_image='https://shorturl.at/KKHvu',
        dob='1995-01-03',
        bio='This is Cartman\'s bio',
        user_id=user6.id
    )
    full_user7 = Full_user(
        first_name='Morty',
        last_name='Chauncey',
        email='morty@universe.com',
        user_image='https://shorturl.at/EuZJk',
        dob='2000-08-03',
        bio='This is Morty\'s bio',
        user_id=user7.id
    )

    full_user8 = Full_user(
        first_name='Lisa',
        last_name='Simpson',
        email='lisa@simpsons.com',
        user_image='https://graphicnovelty2.com/wp-content/uploads/2021/03/lisa-simpson.jpg?w=1400',
        dob='1997-08-03',
        bio='This is Lisa\'s bio',
        user_id=user8.id
    )
    full_user9 = Full_user(
        first_name='Spongebob',
        last_name='Squarepants',
        email='sponge@squarepants.com',
        user_image='https://shorturl.at/8nJJH',
        dob='1990-10-03',
        bio='This is Squarepants\'s bio',
        user_id=user9.id
    )

    full_user10 = Full_user(
        first_name='Edd',
        last_name='just_Edd',
        email='edd@ededdeddy.com',
        user_image='https://shorturl.at/CnTGC',
        dob='1990-10-03',
        bio='This is Squarepants\'s bio',
        user_id=user10.id
    )

    full_user11 = Full_user(
        first_name='Tom',
        last_name='Cat',
        email='rom@tomanderry.com',
        user_image='https://shorturl.at/Jm650',
        dob='1995-10-03',
        bio='This is Tom\'s bio',
        user_id=user11.id
    )

    full_user12 = Full_user(
        first_name='Bugs',
        last_name='Bunny',
        email='bugs@carrots.com',
        user_image='https://shorturl.at/QQAdk',
        dob='1989-10-03',
        bio='This is Bugs\'s bio',
        user_id=user12.id
    )

    # Add full_users to session and commit
    db.session.add(full_user1)
    db.session.add(full_user2)
    db.session.add(full_user3)
    db.session.add(full_user4)
    db.session.add(full_user5)
    db.session.add(full_user6)
    db.session.add(full_user7)
    db.session.add(full_user8)
    db.session.add(full_user9)
    db.session.add(full_user10)
    db.session.add(full_user11)
    db.session.add(full_user12)

    db.session.commit()

    # Create new posts
    post1 = Post(
        title='One mid-sized room',
        description="My roommate is moving out of her amazing room downstairs! Myself and the other roommate occupy the 2 upstairs bedrooms :) Here is what she has posted about her room: It's an incredible unit with TONS of space and privacy. Your room (6x75, unfurnished) will be downstairs along with a spacious living room, your own private entrance, private half bath and in unit washer/ dryer. Your two roomies will be upstairs where the kitchen/ full bath is located. There's a dishwasher, spiral staircase and localized heating system and big shared backyard and is superrrr quiet if you're a light sleeper like me. The apartment is conveniently located right next to the Graham/Grand stop on the L and is steps away from coffee shops, bodegas and bars. Thank you! P.S. Happy to sell the garment rack since there isn't a closet in the room. There is a shared closet off the kitchen upstairs for storage or you can get creative downstairs with it. $1,440 + utilities",
        address='140-17 84th Drive, 11435',
        neighborhood='jamaica',
        borough='queens',
        neighborhood_description='<li>1 block from the Franklin Av stop</li><li>2nd floor walk up</li><li>1 block from the Botanical Gardens & Brooklyn Museum</li><li>Great coffee shops / food options all round</li>',
        price='1800',
        user_id=user1.id
    )

    post2 = Post(
        title='one small room',
        description='Quiet, Peaceful and clean',
        address='90-02 63rd Dr, 11374',
        neighborhood='Flushing',
        borough='Queens',
        neighborhood_description='<li>1 block from the Franklin Av stop</li><li>2nd floor walk up</li><li>1 block from the Botanical Gardens & Brooklyn Museum</li><li>Great coffee shops / food options all round</li>',
        price='1300',
        user_id=user2.id
    )

    post3 = Post(
        title='Big room, fun roommate',
        description='fun loving, outgoing and clean',
        address='789 Pine St',
        neighborhood='bushwick',
        borough='brooklyn',
        neighborhood_description='<li>1 block from the Franklin Av stop</li><li>2nd floor walk up</li><li>1 block from the Botanical Gardens & Brooklyn Museum</li><li>Great coffee shops / food options all round</li>',
        price='1200',
        user_id=user3.id
    )
    post4 = Post(
        title="Juan's place in Astoria,Queens",
        description='Comfortable room available immediately in Astoria. One block away from the nearest train, and three stops away from the city! Shared, spacious living room, full kitchen w/ dishwasher. Your room can comfortably fit ',
        address='28-15 24th Ave,',
        neighborhood='Astoria',
        borough='Queens',
        neighborhood_description='<li>1 block from the Franklin Av stop</li><li>2nd floor walk up</li><li>1 block from the Botanical Gardens & Brooklyn Museum</li><li>Great coffee shops / food options all round</li>',
        price='1100',
        user_id=user4.id
    )

    post5 = Post(
        title="Dakota's place in Astoria,Queens",
        description='medium sized bedroom with a closet and large windows available in my 3BR Astoria apartment! huge common areas and beautiful kitchen. 2 bathrooms and a balcony. great, lovely and safe neighborhood and 2 mid 20s female professionals as roommates! we have one hypoallergenic cat and can accept one more cat for an additional $50 a month! ',
        address='31-90 30th street',
        neighborhood='Asotria',
        borough='Queens',
        neighborhood_description='<li>1 block from the Franklin Av stop</li><li>2nd floor walk up</li><li>1 block from the Botanical Gardens & Brooklyn Museum</li><li>Great coffee shops / food options all round</li>',
        price='1400',
        user_id=user5.id
    )
    post6 = Post(
        title="rental in Astoria,Queens",
        description="Looking for a roommate to join this great apartment. I thought I had someone, but they fell through at the last minute. Let my misfortune be your gain! Apartment is on the first floor. Living room and kitchen are fully furnished, all that is left is one spot for a roommate! ",
        address='789 Pine St',
        neighborhood='bushwick',
        borough='brooklyn',
        neighborhood_description='<li>1 block from the Franklin Av stop</li><li>2nd floor walk up</li><li>1 block from the Botanical Gardens & Brooklyn Museum</li><li>Great coffee shops / food options all round</li>',
        price='1250',
        user_id=user10.id
    )

    post7 = Post(
        title="Jerry's hole",
        description="Looking for a roommate to join this great apartment. I thought I had someone, but they fell through at the last minute. Let my misfortune be your gain! Apartment is on the first floor. Living room and kitchen are fully furnished, all that is left is one spot for a roommate! ",
        address='140-17 84th Drive,Briarwood',
        neighborhood='Jamaica',
        borough='Queens',
        neighborhood_description='<li>1 block from the Franklin Av stop</li><li>2nd floor walk up</li><li>1 block from the Botanical Gardens & Brooklyn Museum</li><li>Great coffee shops / food options all round</li>',
        price='1550',
        user_id=user7.id
    )

    post8 = Post(
        title="Tom's crib",
        description="Looking for a roommate to join this great apartment. I thought I had someone, but they fell through at the last minute. Let my misfortune be your gain! Apartment is on the first floor. Living room and kitchen are fully furnished, all that is left is one spot for a roommate! ",
        address='140-17 84th Drive,Briarwood',
        neighborhood='Jamaica',
        borough='Queens',
        neighborhood_description='<li>1 block from the Franklin Av stop</li><li>2nd floor walk up</li><li>1 block from the Botanical Gardens & Brooklyn Museum</li><li>Great coffee shops / food options all round</li>',
        price='850',
        user_id=user8.id
    )
    post9 = Post(
        title='one mid-sized room',
        description='Quiet, Peaceful and beautiful',
        address='123 Main St',
        neighborhood='jamaica',
        borough='queens',
        neighborhood_description='<li>1 block from the Franklin Av stop</li><li>2nd floor walk up</li><li>1 block from the Botanical Gardens & Brooklyn Museum</li><li>Great coffee shops / food options all round</li>',
        price='900',
        user_id=user9.id
    )

    post10 = Post(
        title='one small room',
        description='Quiet, Peaceful and clean',
        address='456 Elm St',
        neighborhood='upper west side',
        borough='manhattan',
        neighborhood_description='<li>1 block from the Franklin Av stop</li><li>2nd floor walk up</li><li>1 block from the Botanical Gardens & Brooklyn Museum</li><li>Great coffee shops / food options all round</li>',
        price='1800',
        user_id=user6.id
    )

    post11 = Post(
        title='Big room, fun roommate',
        description='fun loving, outgoing and clean',
        address='789 Pine St',
        neighborhood='bushwick',
        borough='brooklyn',
        neighborhood_description='<li>1 block from the Franklin Av stop</li><li>2nd floor walk up</li><li>1 block from the Botanical Gardens & Brooklyn Museum</li><li>Great coffee shops / food options all round</li>',
        price='2200',
        user_id=user11.id
    )
    post12 = Post(
        title="Bugs Bunny's place in Astoria,Queens",
        description='Comfortable room available immediately in Astoria. One block away from the nearest train, and three stops away from the city! Shared, spacious living room, full kitchen w/ dishwasher. Your room can comfortably fit ',
        address='28-15 24th Ave,',
        neighborhood='Astoria',
        borough='Queens',
        neighborhood_description='<li>1 block from the Franklin Av stop</li><li>2nd floor walk up</li><li>1 block from the Botanical Gardens & Brooklyn Museum</li><li>Great coffee shops / food options all round</li>',
        price='1100',
        user_id=user12.id
    )

    post13 = Post(
        title="Dakota's place in Astoria,Queens",
        description='medium sized bedroom with a closet and large windows available in my 3BR Astoria apartment! huge common areas and beautiful kitchen. 2 bathrooms and a balcony. great, lovely and safe neighborhood and 2 mid 20s female professionals as roommates! we have one hypoallergenic cat and can accept one more cat for an additional $50 a month! ',
        address='31-90 30th street',
        neighborhood='Asotria',
        borough='Queens',
        neighborhood_description='<li>1 block from the Franklin Av stop</li><li>2nd floor walk up</li><li>1 block from the Botanical Gardens & Brooklyn Museum</li><li>Great coffee shops / food options all round</li>',
        price='1000',
        user_id=user2.id
    )
    post14 = Post(
        title="rental in Astoria,Queens",
        description="Looking for a roommate to join this great apartment. I thought I had someone, but they fell through at the last minute. Let my misfortune be your gain! Apartment is on the first floor. Living room and kitchen are fully furnished, all that is left is one spot for a roommate! ",
        address='789 Pine St',
        neighborhood='bushwick',
        borough='brooklyn',
        neighborhood_description='<li>1 block from the Franklin Av stop</li><li>2nd floor walk up</li><li>1 block from the Botanical Gardens & Brooklyn Museum</li><li>Great coffee shops / food options all round</li>',
        price='1720',
        user_id=user1.id
    )

    post15 = Post(
        title="Tom's crib",
        description="Looking for a roommate to join this great apartment. I thought I had someone, but they fell through at the last minute. Let my misfortune be your gain! Apartment is on the first floor. Living room and kitchen are fully furnished, all that is left is one spot for a roommate! ",
        address='140-17 84th Drive,Briarwood',
        neighborhood='Jamaica',
        borough='Queens',
        neighborhood_description='<li>1 block from the Franklin Av stop</li><li>2nd floor walk up</li><li>1 block from the Botanical Gardens & Brooklyn Museum</li><li>Great coffee shops / food options all round</li>',
        price='1200',
        user_id=user11.id
    )

    post16 = Post(
        title="Kyle's crib",
        description="Looking for a roommate to join this great apartment. I thought I had someone, but they fell through at the last minute. Let my misfortune be your gain! Apartment is on the first floor. Living room and kitchen are fully furnished, all that is left is one spot for a roommate! ",
        address="South Park Hill, CO",
        neighborhood='Denver',
        borough='Denver',
        neighborhood_description='<li>1 block from the Franklin Av stop</li><li>2nd floor walk up</li><li>1 block from the Botanical Gardens & Brooklyn Museum</li><li>Great coffee shops / food options all round</li>',
        price='1100',
        user_id=user6.id
    )

    # Add posts to session and commit
    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(post4)
    db.session.add(post5)
    db.session.add(post6)
    db.session.add(post7)
    db.session.add(post8)
    db.session.add(post9)
    db.session.add(post10)
    db.session.add(post11)
    db.session.add(post12)
    db.session.add(post13)
    db.session.add(post14)
    db.session.add(post15)
    db.session.add(post16)

    db.session.commit()

    # Add images to posts
    img1 = PostImage(
        url='dex1.jpg',
        post_id=post1.id
    )

    img2 = PostImage(
        url='dex2.jpg',
        post_id=post1.id
    )

    img3 = PostImage(
        url='dex3.jpg',
        post_id=post1.id
    )

    img4 = PostImage(
        url='dex4.jpg',
        post_id=post1.id
    )

    img5 = PostImage(
        url='anime1.jpg',
        post_id=post2.id
    )

    img6 = PostImage(
        url='anime2.jpg',
        post_id=post2.id
    )

    img7 = PostImage(
        url='anime3.jpg',
        post_id=post2.id
    )

    img8 = PostImage(
        url='bubbles.jpg',
        post_id=post2.id
    )

    img9 = PostImage(
        url='cartman1.jpg',
        post_id=post3.id
    )

    img10 = PostImage(
        url='cartman2.jpg',
        post_id=post3.id
    )

    img11 = PostImage(
        url='cartman3.jpg',
        post_id=post3.id
    )

    img12 = PostImage(
        url='edd.webp',
        post_id=post3.id
    )

    img13 = PostImage(
        url='edd2.webp',
        post_id=post4.id
    )

    img14 = PostImage(
        url='edd3.webp',
        post_id=post4.id
    )

    img15 = PostImage(
        url='edd4.webp',
        post_id=post4.id
    )

    img16 = PostImage(
        url='edd5.webp',
        post_id=post4.id
    )

    img17 = PostImage(
        url='lisa1.jpg',
        post_id=post5.id
    )

    img18 = PostImage(
        url='lisa2.jpg',
        post_id=post5.id
    )

    img19 = PostImage(
        url='lisa3.jpg',
        post_id=post5.id
    )

    img20 = PostImage(
        url='lisa4.jpeg',
        post_id=post5.id
    )

    img21 = PostImage(
        url='morty1.jpg',
        post_id=post6.id
    )

    img22 = PostImage(
        url='morty2.jpg',
        post_id=post6.id
    )

    img23 = PostImage(
        url='morty3.jpg',
        post_id=post6.id
    )

    img24 = PostImage(
        url='morty4.jpg',
        post_id=post6.id
    )

    img25 = PostImage(
        url='sponge1.png',
        post_id=post7.id
    )

    img26 = PostImage(
        url='sponge2.jpg',
        post_id=post7.id
    )

    img27 = PostImage(
        url='sponge3.jpg',
        post_id=post7.id
    )

    img28 = PostImage(
        url='tom.jpg',
        post_id=post8.id
    )

    img29 = PostImage(
        url='tom2.jpg',
        post_id=post8.id
    )

    img30 = PostImage(
        url='tom.jpeg',
        post_id=post8.id
    )

    # Add images to session and commit
    db.session.add(img1)
    db.session.add(img2)
    db.session.add(img3)
    db.session.add(img4)
    db.session.add(img5)
    db.session.add(img6)
    db.session.add(img7)
    db.session.add(img8)
    db.session.add(img9)
    db.session.add(img10)
    db.session.add(img11)
    db.session.add(img12)
    db.session.add(img13)
    db.session.add(img14)
    db.session.add(img15)
    db.session.add(img16)
    db.session.add(img17)
    db.session.add(img18)
    db.session.add(img19)
    db.session.add(img20)
    db.session.add(img21)
    db.session.add(img22)
    db.session.add(img23)
    db.session.add(img24)
    db.session.add(img25)
    db.session.add(img26)
    db.session.add(img27)
    db.session.add(img28)
    db.session.add(img29)
    db.session.add(img30)

    db.session.commit()

    # Create some initial messages
    message1 = Message(sender_id=user1.id, receiver_id=user2.id, content="Hi Bubbles, I'm interested in your room.")
    message2 = Message(sender_id=user2.id, receiver_id=user1.id, content="Hi Dexter, thanks for reaching out! Let's talk more about it.")
    message3 = Message(sender_id=user3.id, receiver_id=user4.id, content="Hey Moomin, I'm looking for a place in Astoria.")
    message4 = Message(sender_id=user4.id, receiver_id=user3.id, content="Hi Courage, I have a room available. Let's chat!")
    message5 = Message(sender_id=user2.id, receiver_id=user1.id, content="Hi Dexter, why no reply?")
    message6 = Message(sender_id=user5.id, receiver_id=user1.id, content="THIS IS A SPAM!")
    message7 = Message(sender_id=user3.id, receiver_id=user1.id, content="where are you free for a showing?",)
    message8 = Message(sender_id=user4.id, receiver_id=user1.id, content="im interested")



    # Add messages to session and commit
    db.session.add(message1)
    db.session.add(message2)
    db.session.add(message3)
    db.session.add(message4)
    db.session.add(message5)
    db.session.add(message6)
    db.session.add(message7)
    db.session.add(message8)


    db.session.commit()

    print("Database seeded with messages!")
