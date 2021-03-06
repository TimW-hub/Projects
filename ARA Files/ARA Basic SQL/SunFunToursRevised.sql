--DROP TABLE extra;
--DROP TABLE booking;
--DROP TABLE guest;
--DROP TABLE rate;
--DROP TABLE room;
--DROP TABLE room_type;
--DROP TABLE calendar;

CREATE DATABASE SunFunToursRevisedtsw0050
USE SunFunToursRevisedtsw0050

CREATE TABLE calendar (
  i date NOT NULL,
  PRIMARY KEY (i)
);
CREATE TABLE room_type (
  id varchar(6) NOT NULL,
  description varchar(100) DEFAULT NULL,
  PRIMARY KEY (id)
);
CREATE TABLE rate (
  room_type varchar(6) NOT NULL DEFAULT '',
  occupancy int NOT NULL DEFAULT '0',
  amount decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (room_type,occupancy),
  CONSTRAINT rate_ibfk_1 FOREIGN KEY (room_type) REFERENCES room_type (id)
);
CREATE TABLE room (
  id int NOT NULL,
  room_type varchar(6) DEFAULT NULL,
  max_occupancy int DEFAULT NULL,
  PRIMARY KEY (id),
  INDEX room_typeIDX (room_type),
  CONSTRAINT room_ibfk_1 FOREIGN KEY (room_type) REFERENCES room_type (id)
);
CREATE TABLE guest (
  id int NOT NULL,
  first_name varchar(50) DEFAULT NULL,
  last_name varchar(50) DEFAULT NULL,
  address varchar(50) DEFAULT NULL,
  PRIMARY KEY (id)
);
CREATE TABLE booking (
  booking_id int NOT NULL,
  booking_date date DEFAULT NULL,
  room_no int DEFAULT NULL,
  guest_id int NOT NULL,
  occupants int NOT NULL DEFAULT '1',
  room_type_requested varchar(6) DEFAULT NULL,
  nights int NOT NULL DEFAULT '1',
  arrival_time varchar(5) DEFAULT NULL,
  PRIMARY KEY (booking_id),
  INDEX room_no_IDX (room_no),
  INDEX guest_id_IDX (guest_id),
  INDEX room_type_requested_IDX (room_type_requested,occupants),
  CONSTRAINT booking_ibfk_1 FOREIGN KEY (room_no) REFERENCES room (id),
  CONSTRAINT booking_ibfk_2 FOREIGN KEY (guest_id) REFERENCES guest (id),
  CONSTRAINT booking_ibfk_3 FOREIGN KEY (room_type_requested) REFERENCES room_type (id),
  CONSTRAINT booking_ibfk_4 FOREIGN KEY (room_type_requested, occupants) REFERENCES rate (room_type, occupancy)
);
CREATE TABLE extra (
  extra_id int NOT NULL,
  booking_id int DEFAULT NULL,
  description varchar(50) DEFAULT NULL,
  amount decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (extra_id)
);
 
SELECT * FROM calendar
SELECT * FROM room_type
SELECT * FROM rate
SELECT * FROM room
SELECT * FROM guest
SELECT * FROM booking
SELECT * FROM extra


SELECT guest_ID AS 'Guest', booking_date AS 'Booking date', nights AS 'Number of nights' FROM booking
WHERE guest_id = '1183';