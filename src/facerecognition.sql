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

-- --------------------------------------------------------

DROP TABLE IF EXISTS `Account`, `Branch`, `CurrentAccount`, `Customer`, `Descriptions`, `Loan`, `Phone`, `SavingsAccount`, `Transaction`;

CREATE TABLE `Customer` (
  `customerID` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `login_time` time NOT NULL,
  `login_date` date NOT NULL,
  `info.address.city` varchar(50) NOT NULL,
  `info.address.street` varchar(100) NOT NULL,
  `info.address.flatNumber` varchar(50) NOT NULL,
  `info.address.country` varchar(50) NOT NULL,
  `info.name.first` varchar(50) NOT NULL,
  `info.name.second` varchar(50) NOT NULL,
  PRIMARY KEY(`customerID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Branch`(
  `branchID` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  PRIMARY KEY(`branchID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Loan` (
  `loanID` int NOT NULL,
  `amount` int NOT NULL,
  `interest` float NOT NULL,
  `expiryDate` date NOT NULL,
  `branchID` int NOT NULL,
  PRIMARY KEY(`loanID`),
  FOREIGN KEY (`branchID`) REFERENCES `Branch`(`branchID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Account`(
  `accountNumber` int NOT NULL,
  `balance` int NOT NULL,
  `customerID` int NOT NULL,
  `branchID` int NOT NULL,
  PRIMARY KEY(`accountNumber`),
  FOREIGN KEY (`customerID`) REFERENCES `Customer`(`customerID`),
  FOREIGN KEY (`branchID`) REFERENCES `Branch`(`branchID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `SavingsAccount`(
  `accountNumber` int NOT NULL,
  `accountType.currency` varchar(50) NOT NULL,
  `accountType.ticker` varchar(50) NOT NULL,
  `balance` int NOT NULL,
  PRIMARY KEY(`accountNumber`),
  FOREIGN KEY (`accountNumber`) REFERENCES `Account`(`accountNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `CurrentAccount`(
  `accountNumber` int NOT NULL,
  `linkedSavingsAccount` int NOT NULL,
  `balance` int NOT NULL,
  PRIMARY KEY(`accountNumber`),
  FOREIGN KEY (`accountNumber`) REFERENCES `Account`(`accountNumber`),
  FOREIGN KEY (`linkedSavingsAccount`) REFERENCES `SavingsAccount`(`accountNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Phone`(
  `customerID` int NOT NULL,
  `phoneNumbers` varchar(50) NOT NULL,
  PRIMARY KEY(`customerID`, `phoneNumbers`),
  FOREIGN KEY (`customerID`) REFERENCES `Customer`(`customerID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Transaction`(
  `transactionID` int NOT NULL,
  `amount` int NOT NULL,
  `createdBy.accountNumber` int NOT NULL,
  `creationDate` date NOT NULL,
  `createdBy.city` varchar(50) NOT NULL,
  PRIMARY KEY(`transactionID`),
  FOREIGN KEY (`createdBy.accountNumber`) REFERENCES `Account`(`accountNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Descriptions`(
  `transactionID` int NOT NULL,
  `description` varchar(500) NOT NULL,
  PRIMARY KEY(`transactionID`, `description`),
  FOREIGN KEY (`transactionID`) REFERENCES `Transaction`(`transactionID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- InternalTransaction(internalTransactionID, transactionID, to.accountID, from.accountID)
-- - internalTransactionID referencing Transaction
-- - to.accountID referencing CurrentAccount
-- - from.accountID referencing CurrentAccount

--  -- --- --  no idea what this means
-- LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
-- UNLOCK TABLES;

--  -- -- test data
-- INSERT INTO `Customer` VALUES (1, "JACK", NOW(), '2021-09-01');


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
