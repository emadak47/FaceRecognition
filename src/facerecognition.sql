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

DROP TABLE IF EXISTS `Account`, `Branch`, `CurrentAccount`, `Customer`, `User`, `Merchant`, `Loan`, `Phone`, `SavingsAccount`, `Transaction`, `P2P`, `Payment`;

CREATE TABLE `User` (
  `user_id` int NOT NULL,
  `name.first` varchar(50) NOT NULL,
  `name.last` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `login.time` time NOT NULL,
  `login.date` date NOT NULL,
  `logout.time` time NOT NULL,
  `logout.date` date NOT NULL,
  `address.city` varchar(50) NOT NULL,
  `address.street` varchar(500) NOT NULL,
  `address.flat_no` varchar(50) NOT NULL,
  `address.country` varchar(50) NOT NULL,
  PRIMARY KEY(`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Phone`(
  `user_id` int NOT NULL,
  `phoneNumbers` varchar(50) NOT NULL,
  PRIMARY KEY(`user_id`, `phoneNumbers`),
  FOREIGN KEY (`user_id`) REFERENCES `User`(`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Customer`(
  `user_id` int NOT NULL,
  PRIMARY KEY(`user_id`),
  FOREIGN KEY (`user_id`) REFERENCES `User`(`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Merchant`(
  `user_id` int NOT NULL,
  `business_type` varchar(50) NOT NULL,
  PRIMARY KEY(`user_id`),
  FOREIGN KEY (`user_id`) REFERENCES `User`(`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Branch`(
  `branchID` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  PRIMARY KEY(`branchID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Account`(
  `account_no` int NOT NULL,
  `user_id` int NOT NULL,
  `branchID` int NOT NULL,
  PRIMARY KEY(`account_no`),
  FOREIGN KEY (`user_id`) REFERENCES `User`(`user_id`),
  FOREIGN KEY (`branchID`) REFERENCES `Branch`(`branchID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `CurrentAccount`(
  `account_no` int NOT NULL,
  `balance` int NOT NULL,
  PRIMARY KEY(`account_no`),
  FOREIGN KEY (`account_no`) REFERENCES `Account`(`account_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `SavingsAccount`(
  `account_no` int NOT NULL,
  `account_currency` varchar(50) NOT NULL,
  `balance` int NOT NULL,
  `linkedCurrentAccount` int NOT NULL,
  PRIMARY KEY(`account_no`),
  FOREIGN KEY (`account_no`) REFERENCES `Account`(`account_no`),
  FOREIGN KEY (`linkedCurrentAccount`) REFERENCES `CurrentAccount`(`account_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Transaction`(
  `tx_id` int NOT NULL,
  `amount` int NOT NULL,
  `description` varchar(50) NOT NULL,
  `created_by.account_no` int NOT NULL,
  `creation_time` time NOT NULL,
  `creation_day` int NOT NULL,
  `creation_month` int NOT NULL,
  `creation_year` int NOT NULL,
  PRIMARY KEY(`tx_id`),
  FOREIGN KEY (`created_by.account_no`) REFERENCES `Account`(`account_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `P2P`(
  `tx_id` int NOT NULL,
  PRIMARY KEY(`tx_id`),
  FOREIGN KEY (`tx_id`) REFERENCES `Transaction`(`tx_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Payment`(
  `tx_id` int NOT NULL,
  PRIMARY KEY(`tx_id`),
  FOREIGN KEY (`tx_id`) REFERENCES `Transaction`(`tx_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--  -- -- test data
-- INSERT INTO `User` VALUES (1, "JACK", NOW(), '2021-09-01');

--  -- --- --  no idea what this means
-- LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
-- UNLOCK TABLES;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
