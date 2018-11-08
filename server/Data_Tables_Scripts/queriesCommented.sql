-- #///////////////////----GET STATEMENTS----///////////////////#

-- 1 #get character with most likes
-- select distinct c_name, l_like from Character, joinVandU, Voting  where
--  c_charID = jvu_charID and l_charID = jvu_charID group by c_name 
--  having l_like = (select max(l_like) from Voting);

-- 2 #get character with most dislikes
-- select distinct c_name, l_dislike from Character, joinVandU, Voting  where
--  c_charID = jvu_charID and l_charID = jvu_charID group by c_name 
--  having l_dislike = (select max(l_dislike) from Voting);

-- 3 #get character's games
-- select g_name from Games, joinCandG, Character where g_gameID = j_gameID and c_charID = j_charID
-- and c_name = "Link";

-- 4 #order characters DESC based on their chronological release date
-- select c_name, f_initialRelease from Character, Games, Franchise, joinCandG where c_charID = j_charID
-- and j_gameID = g_gameID and g_franchID = f_franchID group by c_name order by f_initialRelease;

-- 5 #get character's franchise
-- select c_name, f_name from Character, Games, Franchise, joinCandG where c_charID = j_charID
-- and j_gameID = g_gameID and g_franchID = f_franchID group by c_name order by f_name;

-- 6 #get character's moves! (specify by character)
-- select c_name, m_ultimate, m_sideSmash, m_bAttack, m_recovery from Character, Moves where m_charID = c_CharID
-- and c_name = "Ike";

-- 7 #order characters based on their tier, display name
-- select c_name, c_tier from Character order by c_tier;

-- 8 #get comments and UserName made about certain character (ask for char) display char and comment
-- select u_userName, cs_comment from User, commSect, Character where u_userID = cs_userID 
-- and c_charID = cs_charID and c_name = "Ike";

-- 9 #get character that most users main    
    
--    select u_main, count(u_userID) from User group by u_main having count(u_userID) 
--     = (select max(SQ1.countChar) from (select count(u_userID) as countChar from User
--     group by u_main) SQ1) ;

-- 10 #for each character get its franchise  
--     select c_name, f_name from Character, Games, Franchise, joinCandG 
--     where j_charID = c_charID and  j_gameID = g_gameID and  g_franchID = f_franchID group by c_name;

-- 11 #Get description from specific character
--     select c_desc from Character where c_name = "Ike";

-- #/////////////////-----INSERT------///////////////////#

-- 12 #create user account
-- INSERT INTO User (u_firstName, u_lastName, u_email, u_userName, u_admin, u_main)
-- VALUES ("kechu", "Quesadilla", "kechu@ucmerced.edu", "kechuarceus17", 0, "Toon Link");

-- 13 #post a comment about certain character
-- INSERT INTO commSect (cs_userID, cs_charID, cs_comment)
-- VALUES (14, 7, "wow that ike is very strong and fast");

-- 14 #like a character or dislike (here on action char id will be stores in table)
-- INSERT INTO joinVandU (jvu_charID, jvu_userID, jvu_like, jvu_dislike)
-- VALUES (2, 12, 1, 0);

-- WILL BE 1 IN DISLIKE OR 1 IN LIKE, DEPENDING ON ACTION, PYTHON WILL TAKE
-- CARE OF SPECIFICS
-- UPDATE Voting
-- SET l_like = (l_like + 1), l_dislike = (l_like + 0)
-- where l_charID = 2;

-- 15 #administrator add character (will depend on user Input)
-- INSERT INTO Character (c_name, c_tier, c_class, c_desc)
-- VALUES ("Piranha Plant", "A", "Melee", "Plant");

-- 16 #administrator add franchise (ask will ask administrator for details)
-- INSERT INTO Franchise (f_name, f_initialRelease)
-- VALUES ("Super Mario Bros", "1985-09-15");

-- 17 #administrator add game (ask will ask administrator for details)
-- INSERT INTO Games (g_franchID, g_console, g_name, g_releaseDate)
-- VALUES (7, "Super Nintendo", "Super Mario World", "1990-11-21");

-- 18 #administrator add moves to character
-- INSERT INTO Moves (m_charID, m_ultimate, m_sideSmash, m_bAttack, m_recovery)
-- VALUES (11 ,"demo special", "demo sidesmash", "demo bAttack", "demo recovery");

-- #///////////////////---UPDATE STATEMENTS---///////////////////#
-- #update userName (have to enter password)

-- 19 #delete user (enter username)
-- DELETE FROM User
-- where u_userID = 3;

-- DELETE FROM commSect
-- where cs_userID = 3;

-- DELETE FROM joinVandU
-- where jvu_userID = 3;

-- 20 #update userName (have to enter password)
-- UPDATE User 
-- SET userName = "demoUser"
-- where u_userID = 5;






