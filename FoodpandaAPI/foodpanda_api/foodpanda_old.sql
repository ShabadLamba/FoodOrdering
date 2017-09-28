-- phpMyAdmin SQL Dump
-- version 4.4.3
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 29, 2015 at 04:30 PM
-- Server version: 5.6.24
-- PHP Version: 5.6.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `foodpanda`
--

-- --------------------------------------------------------

--
-- Table structure for table `city`
--


--
-- Dumping data for table `city`
--

-- --------------------------------------------------------

--
-- Table structure for table `cuisine_restaurant`
--

CREATE TABLE IF NOT EXISTS `cuisine_restaurant` (
  `restaurant_id` varchar(255) NOT NULL,
  `cuisine_name` varchar(255) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `locality`
--

CREATE TABLE IF NOT EXISTS `locality` (
  `locality_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `city_id` varchar(255) NOT NULL,
  `data_resource` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `locality`
--


-- --------------------------------------------------------

--
-- Table structure for table `locality_restaurant`
--

CREATE TABLE IF NOT EXISTS `locality_restaurant` (
  `locality_id` varchar(255) NOT NULL,
  `restaurant_id` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE IF NOT EXISTS `menu` (
  `dish_id` varchar(255) NOT NULL,
  `restaurant_id` varchar(255) NOT NULL,
  `dish_name` varchar(255) NOT NULL,
  `cost` float NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  `data_resource` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `menu`
--


-- --------------------------------------------------------

--
-- Table structure for table `restaurants`
--

CREATE TABLE IF NOT EXISTS `restaurants` (
  `restaurant_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `rating_aggregate` float DEFAULT NULL,
  `delivery_fee` float DEFAULT NULL,
  `delivery_time` varchar(16) DEFAULT NULL,
  `takeaway_time` varchar(16) DEFAULT NULL,
  `minimum_order` float DEFAULT NULL,
  `payment_methods` tinyint(1) DEFAULT NULL,
  `voucher` tinyint(1) DEFAULT NULL,
  `data_resource` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `restaurants`
--

--
-- Indexes for dumped tables
--

--
-- Indexes for table `city`
--

--
-- Indexes for table `cuisine_restaurant`
--
ALTER TABLE `cuisine_restaurant`
  ADD PRIMARY KEY (`restaurant_id`,`cuisine_name`);

--
-- Indexes for table `locality`
--
ALTER TABLE `locality`
  ADD PRIMARY KEY (`locality_id`),
  ADD KEY `city_id` (`city_id`);

--
-- Indexes for table `locality_restaurant`
--
ALTER TABLE `locality_restaurant`
  ADD PRIMARY KEY (`locality_id`,`restaurant_id`);

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`dish_id`),
  ADD KEY `restaurant_id` (`restaurant_id`);

--
-- Indexes for table `restaurants`
--
ALTER TABLE `restaurants`
  ADD PRIMARY KEY (`restaurant_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `locality`
--
ALTER TABLE `locality`
  ADD CONSTRAINT `locality_ibfk_1` FOREIGN KEY (`city_id`) REFERENCES `city` (`city_id`) ON DELETE CASCADE;

--
-- Constraints for table `menu`
--
ALTER TABLE `menu`
  ADD CONSTRAINT `menu_ibfk_1` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurants` (`restaurant_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
