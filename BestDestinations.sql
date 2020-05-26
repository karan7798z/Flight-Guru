select DEST, a.NAME, f.ORIGIN, count(*) as 'No_Of_Flights' 
from flight as f join airport as a on a.ORIGIN = f.DEST 
where f.ORIGIN = '<Origin captured from user input>' and MONTH(FL_DATE) = MONTH('<Date captured from user input>') 
group by DEST order by count(*) desc LIMIT 5;