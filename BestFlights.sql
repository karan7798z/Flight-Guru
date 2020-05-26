SELECT a.AIRLINE, OP_CARRIER, ORIGIN, DEST, AVG(DEP_DELAY + ARR_DELAY) as 'TOTAL_AV_DELAY' 
from flight f join airline a on a.IATA_CODE = f.OP_CARRIER
where ORIGIN = "<Origin captured from user input>" and DEST = "<Destination captured from user input>"
and MONTH(FL_DATE) = MONTH('<Date captured from user input>')
group by(OP_CARRIER) 
order by AVG(DEP_DELAY + ARR_DELAY) LIMIT 5;