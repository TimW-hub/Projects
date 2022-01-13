USE SunFunToursRevisedtsw0050

--Q1
SELECT guest_id AS 'Guest', booking_date AS 'Booking date', nights AS 'Number of nights' FROM booking
WHERE guest_id = '1183';

--Q2
SELECT booking.arrival_time AS 'Arrival time', guest.first_name + ' ' + guest.last_name AS 'Guest full name',
booking.booking_date AS 'Booking date' FROM booking

INNER JOIN guest ON booking.guest_id = guest.id
WHERE booking.booking_date = '2016-11-05'
ORDER BY booking.arrival_time;

--Q3
SELECT b.booking_id, rate.room_type AS 'Room type', rate.occupancy AS 'Number of Occupants',
rate.amount AS 'Amount' FROM booking AS b

INNER JOIN rate ON b.room_type_requested = rate.room_type
WHERE b.booking_id IN ('5152', '5165', '5154', '5295')
ORDER BY b.booking_id;

--Q4
SELECT b.room_no, b.booking_date, g.first_name, g.last_name, g.address FROM booking AS b
INNER JOIN guest AS g ON b.guest_id = g.id
WHERE b.room_no = 101 AND b.booking_date = '2016-12-03';

--Q5
SELECT guest_id, COUNT(booking_id) AS 'Total number of bookings', SUM(nights) AS 'Total number of nights'
FROM booking
WHERE guest_id IN (1185, 1270)
GROUP BY guest_id;

--Q6
SELECT room.id AS 'Rooms free on 25-11-2016' FROM booking AS b1
INNER JOIN room ON room.id = b1.room_no

WHERE NOT EXISTS (
	SELECT room_no from booking as b2
	WHERE b2.room_no = room.id
	AND (b2.booking_date <= '2016-11-25' AND DATEADD(d, nights, b2.booking_date) > '2016-11-25')
	)
GROUP BY room.id;

--Q7
SELECT SUM(b.nights * rate.amount) AS 'Ruth Cadbury - payable amount' FROM booking AS b
INNER JOIN rate ON b.room_type_requested = rate.room_type
INNER JOIN guest ON b.guest_id = guest.id
WHERE guest.first_name = 'Ruth' AND guest.last_name = 'Cadbury';

--Q8
SELECT SUM(b.nights * rate.amount) + SUM(e.amount) AS 'Total bill' FROM booking AS b
INNER JOIN rate ON b.room_type_requested = rate.room_type
INNER JOIN extra AS e ON e.booking_id = b.booking_id
WHERE b.booking_id = '5346'

--Q9
SELECT g.first_name, g.last_name, g.address,
	CASE
		WHEN SUM(b.nights) IS NULL THEN 0 ELSE SUM(b.nights)
	END
	AS nights
FROM booking as b
INNER JOIN guest AS g ON b.guest_id = g.id
WHERE g.address LIKE '%Edinburgh%'
GROUP BY g.first_name, g.last_name, g.address
ORDER BY g.first_name, g.last_name;

--Q10
SELECT booking_date AS 'Date', COUNT(booking_id) AS 'Arrivals' FROM booking
WHERE booking_date BETWEEN '2016-11-25' AND '2016-12-01'
GROUP BY booking_date
ORDER BY booking_date

--Q11
SELECT SUM(occupants) AS 'Number of Guests' FROM booking
WHERE booking_date <= '2016-11-21'
AND DATEADD(d, nights, booking_date)>'2016-11-21';

--Q12
SELECT DISTINCT a.last_name, a.first_name, b.first_name
FROM (SELECT * FROM booking INNER JOIN guest ON booking.guest_id = guest.id) AS a
INNER JOIN (SELECT * FROM booking INNER JOIN guest ON booking.guest_id = guest.id) AS b
ON a.last_name = b.last_name
AND a.booking_date <= b.booking_date
AND DATEADD(d, a.nights-1, a.booking_date) >= b.booking_date
AND a.first_name > b.first_name
ORDER BY a.last_name;

--Q13
SELECT DATEADD(d, nights, booking_date) AS 'Date vacated',
SUM(CASE WHEN room_no LIKE '1%' THEN 1 ELSE 0 END) AS 'First floor',
SUM(CASE WHEN room_no LIKE '2%' THEN 1 ELSE 0 END) AS 'Second floor',
SUM(CASE WHEN room_no LIKE '3%' THEN 1 ELSE 0 END) AS 'Third floor'
FROM booking
WHERE DATEADD(d, nights, booking_date) BETWEEN '2016-11-14' AND '2016-11-20'
GROUP BY DATEADD(d, nights, booking_date);


SELECT * FROM rate
-- calendar / guest / rate / room / room_type / booking / extra


--Q14
DECLARE @row_number int;
SET @row_number = 0;

SELECT room.id,	DATEADD(d, -rc.room_availability_streak + 1, rc.i) AS i
FROM
	(SELECT a.i, a.room_no,	@row_number1 :=
		CASE
			WHEN b.room_no IS NULL
			THEN @row_number1 + 1
			ELSE 0
		END
	AS room_availability_streak
	FROM
		(SELECT	* FROM calendar	INNER JOIN
			(SELECT DISTINCT room_no FROM booking)
			AS c)
		AS a
	LEFT JOIN
	(SELECT
		booking_date,
		DATEADD(d, nights, booking_date) AS checkout_date,
		room_no
	FROM
		booking)
	AS b
	ON a.i >= b.booking_date
	AND a.i < b.checkout_date
	AND a.room_no = b.room_no,
	(SELECT @row_number1 := 0)
	AS counter_int
	WHERE
	a.i BETWEEN '2016-11-03' AND '2016-12-19'
	ORDER BY a.room_no,	a.i
)
AS rc
INNER JOIN room	ON rc.room_no = room.id
WHERE
	rc.room_availability_streak = 7
	AND room.room_type = 'double'
ORDER BY
	i LIMIT 2;



--Q15
SELECT
	DATE_ADD(MAKEDATE(2016, 7), INTERVAL WEEK(DATE_ADD(booking.booking_date, INTERVAL booking.nights - 5 DAY), 0) WEEK) AS i,
	SUM(booking.nights * rate.amount) + SUM(e.amount) AS Total
FROM
	booking
	JOIN
		rate
		ON (booking.occupants = rate.occupancy
		AND booking.room_type_requested = rate.room_type)
	LEFT JOIN
		(
			SELECT
				booking_id,
				SUM(amount) as amount
			FROM
				extra
			group by
				booking_id
		)
		AS e
		ON (e.booking_id = booking.booking_id)
GROUP BY
	i;