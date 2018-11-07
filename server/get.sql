-- #---GET STATEMENTS----#
-- #order characters DESC based on their chronological release date
-- #get character's franchise
-- #get character's moves!
-- #get character's certain move (from list in moves)
-- #order characters based on their tier, display name
-- #get comments made about certain character (ask for char) display char and comment
-- #check if user with same username or password is in the system

-- 1 #get character with most likes
-- select distinct c_name, l_like from Character, joinVandU, Voting  where
--  c_charID = jvu_charID and l_charID = jvu_charID group by c_name 
--  having l_like = (select max(l_like) from Voting);

-- 2 #get character's game
select g_name from Games, joinCandG, Character where g_gameID = j_gameID and c_charID = j_charID
where c_name = "Link";