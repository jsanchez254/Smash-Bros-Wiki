-- USER TABLE
-- INSERT INTO User (u_firstName, u_lastName, u_email, u_userName, u_admin, u_main)

-- VALUES ("Jesus", "Sanchez", "jsanchez254@ucmerced.edu", "kechuArceus", 1, "Ike"),
--        ("Jordan", "Pineda", "jpineda24@ucmerced.edu", "LuCkYCaPTaiN", 1, "Snake"),
--        ("Alec", "Mendiola", "alec@ucmerced.edu", "alec1", 1, "Snake"),
--        ("Enrique", "Mercado", "enrique@ucmerced.edu", "Enrique1", 0, "Snake"),
--        ("Christian", "Martin", "christian@ucmerced.edu", "christian1", 0, "Lucina"),
--        ("Gene", "Panferov", "gene@ucmerced.edu", "gene1", 0, "Snake"),
--        ("Shawn", "Liang", "shawn@ucmerced.edu", "shawn1", 0, "Snake"),
--        ("Tlaloc", "Barajas", "tlaloc@ucmerced.edu", "tlaloc1", 0, "Snake"),
--        ("Jonathan", "Chancey", "jonathan@ucmerced.edu", "coruscar", 0, "Lucina"),
--        ("Ricardo", "Sanchez", "ricardo@ucmerced.edu", "popocaca", 0, "Link"),
--        ("Yiying", "Jie", "yiying@ucmerced.edu", "yiying1", 0, "Bayonetta"),
--        ("Vivian", "Chen", "vivian@ucmerced.edu", "vivian1", 0, "Snake"),
--        ("Masahiro", "Sakurai", "sakuraiSenpai@nintendo.com", "sakuraiMaster", 0, "Fox"),
--        ("Florin", "Rusu", "florin@ucmerced.edu", "florin1", 0, "Falco");


-- COMMENT SECTION
-- INSERT INTO CommSect (cs_userID, cs_charID, cs_comment)

-- VALUES (1, 2 , "wow that character is super cool!"),
--        (2, 1 , "wow that character is super cool!"),
--        (3, 2 , "wow that character is super cool!"),
--        (4, 3 , "wow that character is super cool!"),
--        (5, 4 , "wow that character is super cool!"),
--        (6, 5 , "wow that character is super cool!"),
--        (7, 6 , "wow that character is super cool!"),
--        (8, 7 , "wow that character is super cool!"),
--        (9, 8 , "wow that character is super cool!"),
--        (10, 9 , "wow that character is super cool!"),
--        (11, 10 , "wow that character is super cool!"),
--        (12, 5 , "wow that character is super cool!"),
--        (13, 4 , "wow that character is super cool!"),
--        (14, 1 , "wow that character is super cool!");

-- VOTING
INSERT INTO Voting (l_charID, l_like, l_dislike)

VALUES  (1, 3, 1),
        (2, 3, 1),
        (3, 5, 2),
        (4, 3, 9),
        (5, 3, 1),
        (6, 8, 1),
        (7, 14, 0),
        (8, 4, 0),
        (9, 12, 1),
        (10, 11, 0)

