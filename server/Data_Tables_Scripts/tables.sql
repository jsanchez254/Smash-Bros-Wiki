CREATE TABLE User
(
    u_userID INTEGER PRIMARY KEY,
    u_firstName CHAR(25) NOT NULL,
    u_lastName CHAR(25) NOT NULL,
    u_email CHAR(25) NOT NULL,
    u_userName CHAR(25) NOT NULL,
    u_admin INT(1),
    u_main CHAR(25) NOT NULL
);

CREATE TABLE Voting
(
    l_userID INT(4) NOT NULL,
    l_charID INT(4) NOT NULL,
    l_like INT NOT NULL,
    l_dislike INT NOT NULL
);

CREATE TABLE commSect
(
    cs_userID INT(4) NOT NULL,
    cs_charID INT(4) NOT NULL,
    cs_comment VARCHAR(199) NOT NULL
);

CREATE TABLE Character
(
    c_charID INTEGER PRIMARY KEY,
    c_name CHAR(25) NOT NULL,
    c_tier CHAR(25) NOT NULL,
    c_class CHAR(25) NOT NULL,
    c_desc VARCHAR(200) NOT NULL
);

CREATE TABLE Moves
(
    m_charID INT(4) NOT NULL,
    m_ultimate CHAR(25) NOT NULL,
    m_sideSmash CHAR(25) NOT NULL,
    m_bAttack CHAR(25) NOT NULL,
    m_recovery CHAR(100) NOT NULL
);

CREATE TABLE Games
(
    g_gameID INTEGER PRIMARY KEY,
    g_franchID INT(4) NOT NULL,
    g_console CHAR(25) NOT NULL,
    g_name CHAR(25) NOT NULL,
    g_releaseDate DATE NOT NULL
);

CREATE TABLE Franchise
(
    f_franchID INTEGER PRIMARY KEY,
    f_name CHAR(25) NOT NULL,
    f_initialRelease DATE NOT NULL
);

CREATE TABLE joinCandG
(
    j_joinID INTEGER PRIMARY KEY,
    j_charID INT(4) NOT NULL,
    j_gameID INT(4) NOT NULL
);