-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 17, 2020 at 09:41 PM
-- Server version: 5.7.28-0ubuntu0.18.04.4
-- PHP Version: 7.2.24-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `facerecognition`
--

CREATE DATABASE IF NOT EXISTS facerecognition;

-- --------------------------------------------------------

DROP TABLE IF EXISTS `Account`, `Branch`, `CurrentAccount`, `Customer`, `Log_History`, `Merchant`, `Phone`, `SavingsAccount`, `Transaction`;

CREATE TABLE `Customer` (
  `customer_id` int NOT NULL,
  `name.first` varchar(50) NOT NULL,
  `name.last` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `address.city` varchar(50) NOT NULL,
  `address.street` varchar(500) NOT NULL,
  `address.flat_no` varchar(50) NOT NULL,
  `address.country` varchar(50) NOT NULL,
  PRIMARY KEY(`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Phone`(
  `customer_id` int NOT NULL,
  `phoneNumbers` varchar(50) NOT NULL,
  PRIMARY KEY(`customer_id`, `phoneNumbers`),
  FOREIGN KEY (`customer_id`) REFERENCES `Customer`(`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Log_History` (
  `customer_id` int NOT NULL,
  `login.time` time NOT NULL,
  `login.date` date NOT NULL,
  PRIMARY KEY(`customer_id`, `login.date`,`login.time`),
  FOREIGN KEY (`customer_id`) REFERENCES `Customer`(`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Branch`(
  `branch_id` int NOT NULL,
  `location` varchar(50) NOT NULL,
  PRIMARY KEY(`branch_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Account`(
  `account_no` int NOT NULL,
  `customer_id` int NOT NULL,
  `branch_id` int NOT NULL,
  PRIMARY KEY(`account_no`),
  FOREIGN KEY (`customer_id`) REFERENCES `Customer`(`customer_id`),
  FOREIGN KEY (`branch_id`) REFERENCES `Branch`(`branch_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `CurrentAccount`(
  `account_no` int NOT NULL,
  `balance` float NOT NULL,
  PRIMARY KEY(`account_no`),
  FOREIGN KEY (`account_no`) REFERENCES `Account`(`account_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `SavingsAccount`(
  `account_no` int NOT NULL,
  `balance` float NOT NULL,
  `currency` varchar(50) NOT NULL,
  PRIMARY KEY(`account_no`, `currency`),
  FOREIGN KEY (`account_no`) REFERENCES `Account`(`account_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Merchant`(
  `merchant_id` int NOT NULL,
  `business_type` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY(`merchant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Transaction`(
  `tx_id` int NOT NULL,
  `created_by.account_no` int NOT NULL,
  `pay_to.merchant_id` int NOT NULL,
  `amount` float NOT NULL,
  `description` varchar(50),
  `creation_time` time NOT NULL,
  `creation_date` date NOT NULL,
  PRIMARY KEY(`tx_id`),
  FOREIGN KEY (`created_by.account_no`) REFERENCES `Account`(`account_no`),
  FOREIGN KEY (`pay_to.merchant_id`) REFERENCES `Merchant`(`merchant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- -- -- delete data (for debugging)
-- DELETE FROM `Transaction`; DELETE FROM `Merchant`; DELETE FROM `CurrentAccount`; DELETE FROM `SavingsAccount`; DELETE FROM `Account`; DELETE FROM `Branch`; DELETE FROM `Phone`; DELETE FROM `Log_History`; DELETE FROM `Customer`;


-- INSERT DATA

INSERT INTO `Customer` VALUES (1, "Aayush", "Batwara", "Aayush_Batwara", "1234Batwara", "Delhi", "Hennessy", "506", "India");
INSERT INTO `Customer` VALUES (2, "Aditya", "Gupta", "Aditya_Gupta", "1234Gupta", "Oslo", "Brooklyn", "2033", "Norway");
INSERT INTO `Customer` VALUES (3, "Emad", "Akhras", "Emad_Akhras", "1234Akhras", "Berlin", "Central", "1013", "Germany");
INSERT INTO `Customer` VALUES (4, "Dhruv", "Aggarwal", "Dhruv_Aggarwal", "1234Aggarwal", "Rome", "Admiralty", "201", "Italy");
INSERT INTO `Customer` VALUES (5, "Arnav", "Rajiv", "Arnav_Rajuv", "1234Rajiv", "Cairo", "Kwoloon", "810", "Egypt");

INSERT INTO `Phone` VALUES (1, "324534");
INSERT INTO `Phone` VALUES (1, "932312");
INSERT INTO `Phone` VALUES (1, "223211");
INSERT INTO `Phone` VALUES (2, "984563");
INSERT INTO `Phone` VALUES (2, "123463");
INSERT INTO `Phone` VALUES (3, "347598");
INSERT INTO `Phone` VALUES (4, "578632");
INSERT INTO `Phone` VALUES (5, "453879");

INSERT INTO `Log_History` VALUES (1, CURTIME(), CURDATE());
INSERT INTO `Log_History` VALUES (2, CURTIME(), "2021-11-02");
INSERT INTO `Log_History` VALUES (3, "17:32:23", CURDATE());
INSERT INTO `Log_History` VALUES (4, "23:46:10", "2019-05-01");
INSERT INTO `Log_History` VALUES (5, "15:49:11", "1999-11-30");
INSERT INTO `Log_History` VALUES (3, "04:28:09", "1999-11-30");
INSERT INTO `Log_History` VALUES (2, "07:28:35", "2004-06-25");
INSERT INTO `Log_History` VALUES (4, "14:28:30", "2013-07-19");
INSERT INTO `Log_History` VALUES (1, "17:50:38", "2022-04-29");
INSERT INTO `Log_History` VALUES (5, "10:28:57", "2010-04-05");
INSERT INTO `Log_History` VALUES (4, "18:17:45", "2009-09-09");
INSERT INTO `Log_History` VALUES (2, "22:29:30", "2020-12-30");
INSERT INTO `Log_History` VALUES (1, "19:01:10", "2021-11-22");

INSERT INTO `Branch` VALUES (1, "HKU");
INSERT INTO `Branch` VALUES (2, "Central");
INSERT INTO `Branch` VALUES (3, "New Territories");
INSERT INTO `Branch` VALUES (4, "Repulse");
INSERT INTO `Branch` VALUES (5, "Lantau");
INSERT INTO `Branch` VALUES (6, "Mui Wo");

INSERT INTO `Account` VALUES (1, 1, 1);
INSERT INTO `Account` VALUES (2, 1, 2);
INSERT INTO `Account` VALUES (3, 2, 3);
INSERT INTO `Account` VALUES (4, 5, 3);
INSERT INTO `Account` VALUES (5, 3, 1);
INSERT INTO `Account` VALUES (6, 2, 6);
INSERT INTO `Account` VALUES (7, 4, 5);
INSERT INTO `Account` VALUES (8, 3, 4);
INSERT INTO `Account` VALUES (9, 5, 5);
INSERT INTO `Account` VALUES (10, 4, 6);
INSERT INTO `Account` VALUES (11, 1, 3);
INSERT INTO `Account` VALUES (12, 4, 2);
INSERT INTO `Account` VALUES (13, 2, 2);
INSERT INTO `Account` VALUES (14, 3, 2);

INSERT INTO `CurrentAccount` VALUES (1, 1500);
INSERT INTO `CurrentAccount` VALUES (3, 4000);
INSERT INTO `CurrentAccount` VALUES (4, 570);
INSERT INTO `CurrentAccount` VALUES (5, 350);
INSERT INTO `CurrentAccount` VALUES (7, 10500);

INSERT INTO `SavingsAccount` VALUES (2, 6000, "HKD");
INSERT INTO `SavingsAccount` VALUES (6, 500, "USD");
INSERT INTO `SavingsAccount` VALUES (8, 490, "GBP");
INSERT INTO `SavingsAccount` VALUES (9, 6000, "HKD");
INSERT INTO `SavingsAccount` VALUES (10, 9300, "HKD");
INSERT INTO `SavingsAccount` VALUES (11, 120, "USD");
INSERT INTO `SavingsAccount` VALUES (12, 500, "HKD");
INSERT INTO `SavingsAccount` VALUES (13, 4300, "HKD");
INSERT INTO `SavingsAccount` VALUES (14, 5000, "HKD");

INSERT INTO `Merchant` VALUES (1, "Food", "Subway (HKU)");
INSERT INTO `Merchant` VALUES (2, "Entertainment", "Cyberport Cinema");
INSERT INTO `Merchant` VALUES (3, "Education", "Coursera");
INSERT INTO `Merchant` VALUES (4, "Transportation", "MTR");
INSERT INTO `Merchant` VALUES (5, "Medical", "Queen Mary");


-- Customer1txs(1 current1 500HKD, 2saving 6000HKD,11 saving 120 USD)
INSERT INTO `Transaction` VALUES (1, 1, 1, 40, NULL, "12:19:30", "2021-11-04");
INSERT INTO `Transaction` VALUES (2, 2, 3, 2000, "Machine Learning Course", "21:50:39", "2020-02-11");
INSERT INTO `Transaction` VALUES (3, 1, 4, 12, NULL, "07:22:10", "2021-09-23");
INSERT INTO `Transaction` VALUES (4, 1, 4, 7.6, NULL, "19:42:27", "2021-09-23");
INSERT INTO `Transaction` VALUES (5, 2, 4, 3.6, NULL, "19:42:27", "2021-09-23");

-- – Customer 2txs(3current4000HKD,6saving500USD,13saving4300 HKD)
INSERT INTO `Transaction` VALUES (6, 3, 2, 200, "Iron Man", "20:20:14", "2021-12-01");
INSERT INTO `Transaction` VALUES (7, 6, 3, 2500, "Blockchain", "08:44:15", "2020-05-06");
INSERT INTO `Transaction` VALUES (8, 13, 5, 750, "Optician", "10:30:00", "2019-07-21");
INSERT INTO `Transaction` VALUES (9, 3, 4, 8.9, NULL, "14:13:17", "2021-03-14");
INSERT INTO `Transaction` VALUES (10, 3, 1, 76, NULL, "22:52:57", "2020-06-07");

-- – Customer 3 txs(5 current 350HKD,8saving490GBP,14saving5000 HKD)
INSERT INTO `Transaction` VALUES (11, 5, 1, 99, NULL, "13:42:16", "2021-06-06");
INSERT INTO `Transaction` VALUES (12, 8, 3, 3000, "Big data","08:10:03", "2020-08-05");
INSERT INTO `Transaction` VALUES (13, 14, 5, 1000, "Check-up", "09:30:00", "2020-10-27");
INSERT INTO `Transaction` VALUES (14, 5, 4, 17.5, NULL, "23:25:10", "2021– 07-08");

-- – Customer 4 txs(7current10500HKD,10saving9300HKD,12saving500 USD)
INSERT INTO `Transaction` VALUES (15, 7, 1, 120, NULL, "11:33:22", "2021-11-12");
INSERT INTO `Transaction` VALUES (16, 12, 3, 3000, "Big Data", "09:09:11", "2020-12-24");
INSERT INTO `Transaction` VALUES (17, 10, 5, 400, "Medicine", "17:19:44", "2019-04-09");
INSERT INTO `Transaction` VALUES (18, 7, 4, 17.5, NULL, "07:14:02", "2021– 07-08");
INSERT INTO `Transaction` VALUES (19, 7, 4, 17.5, NULL, "07:12:10", "2021– 07-16");
INSERT INTO `Transaction` VALUES (20, 7, 2, 240, "Spiderman", "20:33:14", "2021-10-11");

-- – Customer 5 txs(4current570HKD,9saving6000HKD)
INSERT INTO `Transaction` VALUES (21, 14, 1, 60, NULL, "10:50:20", "2021-04-19");
INSERT INTO `Transaction` VALUES (22, 9, 2, 150, "Thor", "22:25:41", "2021-10-17");
INSERT INTO `Transaction` VALUES (23, 9, 3, 5000, "Tuition", "09:20:14", "2020-11-22");
INSERT INTO `Transaction` VALUES (24, 4, 4, 5.4, NULL, "18:45:29", "2021-10-17");


--  -- --- --  no idea what this means
-- LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
-- UNLOCK TABLES;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
