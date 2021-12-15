--
-- Creates Animals Table
--
DROP TABLE IF EXISTS `animals`;
CREATE TABLE `animals` (
   `animal_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
   `species` varchar(45)  NOT NULL,
   `name` varchar(45)  NOT NULL,
   `volunteer_id` int(11),
   `location_id` int(11) NOT NULL,
   `arrival_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `animals` (`species`, `name`, `volunteer_id`, `location_id`, `arrival_date`)
VALUES 
("Dog", "Pete", 1, 1, 2021-11-10),
("Cat", "Beth", 2, 2, 2021-11-11);

--
-- Creates Volunteers Table
--
DROP TABLE IF EXISTS `volunteers`;
CREATE TABLE `volunteers` (
    `volunteer_id` int(11) AUTO_INCREMENT PRIMARY KEY,
    `first_name` varchar(255) NOT NULL,
    `last_name` varchar(255) NOT NULL,
    `street_address` int(11) NOT NULL,
    `street_name` varchar(255)  NOT NULL,
    `city` varchar(45) NOT NULL,
    `state` varchar(45) NOT NULL,
    `phone` int(11) NOT NULL,
    `email` varchar(255) NOT NULL,
    `location_id` int(11) NOT NULL,
    `mentor_id` int(11) NOT NULL,
    `exp_level` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO volunteers (`first_name`, `last_name`, `street_address`, `street_name`, `city`, `state`, `phone`, `email`, `location_ID`, `mentor_ID`, `exp_level`)
VALUES 
("John", "Smith", 123, "Main", "Springfield","Illinois", 12345678910, "jsmith@gmail.com", 1, 1, 3),
("Jane", "Smith", 532, "South St", "Springfield","Illinois", 3829443921, "snowboarder43@gmail.com", 1, 1, 2);

DROP TABLE IF EXISTS `mentors`;
CREATE TABLE `mentors` (
    `mentor_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `first_name` varchar(255) NOT NULL,
    `last_name` varchar(255) NOT NULL,
    `phone` int(11) NOT NULL,
    `email` varchar(255) NOT NULL,
    `location_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO mentors (`first_name`, `last_name`, `phone`, `email`, `location_ID`)
VALUES 
("Sarah", "Paulson", 9721832291, "paulson@yahoo.com", 1),
("Kumail", "Nanjiani", 9329219293, "fakeemail@aol.com", 2);

--
-- Creates Locations Table
--
DROP TABLE IF EXISTS `locations`;
CREATE TABLE `locations` (
    `location_id` int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `location_name` varchar(255) NOT NULL,
    `capacity` int(11) NOT NULL,
    `street_address` int(11) NOT NULL,
    `street_name` varchar(255) NOT NULL,
    `city` varchar(45) NOT NULL,
    `state` varchar(45) NOT NULL,
    `phone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO locations (`location_name`, `capacity`, `street_address`, `street_name`, `city`, `state`, `phone`)
VALUES 
("Animal Protective League", 100, 350, "Elm Street", "Springfield", "Illinois", 4328429234),
("Portland Animal Shelter", 105, 41, "Burnside", "Portland", "Oregon", 3923349192);

ALTER TABLE `animals`
  ADD UNIQUE KEY `animal_id` (`animal_id `),
  ADD CONSTRAINT `volunteer_id` FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id),
  ADD CONSTRAINT `location_id` FOREIGN KEY (location_id) REFERENCES locations(locaiton_id);

ALTER TABLE `volunteers`
  ADD CONSTRAINT volunteers UNIQUE(volunteer_id),
  ADD CONSTRAINT FOREIGN KEY (location_id) REFERENCES locations(location_id),
  ADD CONSTRAINT FOREIGN KEY (mentor_id) REFERENCES mentors(mentor_id);

ALTER TABLE `mentors`
  ADD CONSTRAINT mentors UNIQUE(mentor_id),
  ADD FOREIGN KEY (location_id) REFERENCES locations(location_id);

ALTER TABLE `locations`
  ADD CONSTRAINT locations UNIQUE(location_id);

DROP TABLE IF EXISTS `animals_volunteers`;
CREATE TABLE `animals_volunteers` (
    `animal_id` int(11),
   `volunteer_id` int(11)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `animals_volunteers`
  ADD FOREIGN KEY (animal_id) REFERENCES animals(animal_id),
  ADD FOREIGN KEY (volunteer_id) REFERENCES volunteer(volunteer_id);