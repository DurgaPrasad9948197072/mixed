-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: Dec 04, 2024 at 10:47 AM
-- Server version: 8.0.39
-- PHP Version: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inhouse`
--

-- --------------------------------------------------------

--
-- Table structure for table `customizationrequest`
--

CREATE TABLE `customizationrequest` (
  `rid` int NOT NULL,
  `poid` int NOT NULL,
  `id` int NOT NULL,
  `name` varchar(225) NOT NULL,
  `customize` varchar(225) NOT NULL,
  `status` int NOT NULL,
  `datetime` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `customizationrequest`
--

INSERT INTO `customizationrequest` (`rid`, `poid`, `id`, `name`, `customize`, `status`, `datetime`) VALUES
(1, 32, 6, 'Header', 'jbhhjb', 1, '2024-12-01 18:21:43.097086'),
(2, 32, 6, 'Header', 'kjbhnjm', 2, '2024-12-01 18:21:43.141134'),
(3, 32, 6, 'Product Card', 'jhbhjbn', 0, '2024-12-01 18:21:43.142051'),
(4, 33, 6, 'Header', 'ewfwsef', 1, '2024-12-02 05:20:08.302712'),
(5, 33, 6, 'Product Card', 'fdwesfws', 1, '2024-12-02 05:20:08.444912'),
(6, 33, 6, 'Checkout Process', 'edsefes', 0, '2024-12-02 05:20:08.447226'),
(7, 10, 6, 'footer', 'jhbhjv', 1, '2024-12-02 16:08:55.315542');

-- --------------------------------------------------------

--
-- Table structure for table `features`
--

CREATE TABLE `features` (
  `feid` int NOT NULL,
  `name` varchar(225) NOT NULL,
  `price` float NOT NULL,
  `plan_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `features`
--

INSERT INTO `features` (`feid`, `name`, `price`, `plan_id`) VALUES
(21, 'iOS Development', 10, NULL),
(22, 'Android Development', 15, NULL),
(23, 'Web Development', 15, NULL),
(24, 'Admin Dashboard', 10, NULL),
(25, 'Application Sources', 10, NULL),
(26, 'Digital Marketing', 10, NULL),
(27, 'SEO', 10, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `housedeviceimages`
--

CREATE TABLE `housedeviceimages` (
  `dimd` int NOT NULL,
  `poid` int NOT NULL,
  `device_name` varchar(225) NOT NULL,
  `image_url` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `housedeviceimages`
--

INSERT INTO `housedeviceimages` (`dimd`, `poid`, `device_name`, `image_url`) VALUES
(2, 10, 'ios', 'https://i.ibb.co/HzBz8Nt/Screenshot-2024-11-13-000244-removebg-preview.png'),
(4, 12, 'ios', 'https://i.ibb.co/FmGTv2f/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg'),
(5, 10, 'Android', 'https://i.ibb.co/FmGTv2f/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg'),
(6, 10, 'Web', 'https://i.ibb.co/HzBz8Nt/Screenshot-2024-11-13-000244-removebg-preview.png'),
(7, 11, 'web ', 'https://i.ibb.co/FmGTv2f/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg'),
(8, 11, 'iOS', 'https://i.ibb.co/HzBz8Nt/Screenshot-2024-11-13-000244-removebg-preview.png'),
(9, 11, 'Android', 'https://i.ibb.co/GnBgM6n/Screenshot-2024-11-13-000001-removebg-preview.png');

-- --------------------------------------------------------

--
-- Table structure for table `houseimages`
--

CREATE TABLE `houseimages` (
  `imd` int NOT NULL,
  `images` varchar(225) NOT NULL,
  `poid` int NOT NULL,
  `datetime` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `houseimages`
--

INSERT INTO `houseimages` (`imd`, `images`, `poid`, `datetime`) VALUES
(1, 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 10, '2024-11-27 13:02:27.291159'),
(5, 'https://i.ibb.co/d7cfdBX/heroforice.jpg', 11, '2024-11-27 13:04:09.331294'),
(9, 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 12, '2024-11-27 17:29:36.136128'),
(10, 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 12, '2024-11-27 17:29:36.249906'),
(11, 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 12, '2024-11-27 17:29:36.250929'),
(12, 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 12, '2024-11-27 17:29:36.251545'),
(13, 'https://i.ibb.co/sHtznbW/heroforice.jpg', 11, '2024-12-01 12:48:16.330295'),
(16, 'https://i.ibb.co/FmGTv2f/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 10, '2024-12-01 14:04:18.693687'),
(18, 'https://i.ibb.co/sHtznbW/heroforice.jpg', 11, '2024-12-01 14:37:45.598298'),
(19, 'https://i.ibb.co/FmGTv2f/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 11, '2024-12-02 10:10:14.209215'),
(20, 'https://i.ibb.co/gmDsByM/heroforice-removebg-preview.png', 10, '2024-12-02 16:30:50.225020'),
(21, 'https://i.ibb.co/WnNcM91/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 13, '2024-12-02 16:32:13.877062'),
(22, 'https://i.ibb.co/rdYsk8d/Screenshot-2024-11-13-000244-removebg-preview.png', 13, '2024-12-02 16:32:13.883699'),
(23, 'https://i.ibb.co/vvq5rc0/Screenshot-2024-11-13-000001-removebg-preview.png', 13, '2024-12-02 16:32:13.884525');

-- --------------------------------------------------------

--
-- Table structure for table `houseoffers`
--

CREATE TABLE `houseoffers` (
  `oid` int NOT NULL,
  `poid` int NOT NULL,
  `discountpercentage` varchar(225) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `startdate` varchar(22) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `enddate` varchar(22) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `datetime` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `status` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `houseoffers`
--

INSERT INTO `houseoffers` (`oid`, `poid`, `discountpercentage`, `startdate`, `enddate`, `datetime`, `status`) VALUES
(5, 10, '7', '2024-11-27', '2024-11-27', '2024-11-27 19:15:30.507769', 0),
(7, 11, '29', '2024-11-29', '2024-11-29', '2024-11-29 17:27:17.070823', 0),
(8, 33, '20', '2024-12-01', '2024-12-06', '2024-12-01 08:47:21.801566', 0);

-- --------------------------------------------------------

--
-- Table structure for table `houseorders`
--

CREATE TABLE `houseorders` (
  `oid` int NOT NULL,
  `id` int DEFAULT NULL,
  `pid` int NOT NULL,
  `date` date DEFAULT NULL,
  `status` int NOT NULL DEFAULT '0',
  `datetime` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `houseorders`
--

INSERT INTO `houseorders` (`oid`, `id`, `pid`, `date`, `status`, `datetime`) VALUES
(1, 1, 1, '2024-09-03', 0, '2024-09-03 16:13:45.744149'),
(2, 3, 1, '2024-09-03', 0, '2024-09-03 16:14:29.947263');

-- --------------------------------------------------------

--
-- Table structure for table `houseproductcompatibility`
--

CREATE TABLE `houseproductcompatibility` (
  `cid` int NOT NULL,
  `poid` int NOT NULL,
  `name` varchar(225) DEFAULT NULL,
  `datetime` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `status` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `houseproductcompatibility`
--

INSERT INTO `houseproductcompatibility` (`cid`, `poid`, `name`, `datetime`, `status`) VALUES
(1, 4, 'Compatibility 1', '2024-09-20 13:31:23.697744', 1),
(2, 5, 'Compatibility 1', '2024-09-20 13:34:48.595725', 1),
(3, 6, 'Compatibility 1', '2024-09-20 13:34:57.284646', 1),
(4, 7, 'Compatibility 1', '2024-09-20 13:35:08.314364', 1),
(5, 8, 'Compatibility 1', '2024-09-20 13:35:19.168597', 1),
(6, 9, 'Compatibility 1', '2024-09-20 14:15:48.568930', 1),
(25, 35, 'name', '2024-12-01 16:32:01.877233', 1);

-- --------------------------------------------------------

--
-- Table structure for table `houseproductcustomelements`
--

CREATE TABLE `houseproductcustomelements` (
  `cpid` int NOT NULL,
  `poid` int NOT NULL,
  `name` varchar(225) NOT NULL,
  `description` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `houseproductcustomelements`
--

INSERT INTO `houseproductcustomelements` (`cpid`, `poid`, `name`, `description`) VALUES
(3, 35, 'header', 'dkjubnhj'),
(4, 35, 'conent', 'jybhj'),
(8, 13, 'ngvh', 'jbhj'),
(11, 10, 'footer', 'dkjnuk'),
(16, 44, 'ygthvb', 'jyjbj');

-- --------------------------------------------------------

--
-- Table structure for table `houseproductfeature`
--

CREATE TABLE `houseproductfeature` (
  `fid` int NOT NULL,
  `poid` int NOT NULL,
  `name` varchar(225) NOT NULL,
  `status` int NOT NULL DEFAULT '0',
  `datetime` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `houseproductfeature`
--

INSERT INTO `houseproductfeature` (`fid`, `poid`, `name`, `status`, `datetime`) VALUES
(1, 4, 'Feature 1', 1, '2024-09-20 13:31:23.702478'),
(2, 4, 'Feature 2', 1, '2024-09-20 13:31:23.704021'),
(3, 4, 'Feature 2', 1, '2024-09-20 13:31:23.704713'),
(4, 5, 'Feature 1', 1, '2024-09-20 13:34:48.596951'),
(5, 5, 'Feature 2', 1, '2024-09-20 13:34:48.597804'),
(6, 5, 'Feature 2', 1, '2024-09-20 13:34:48.598722'),
(7, 6, 'Feature 1', 1, '2024-09-20 13:34:57.287717'),
(8, 6, 'Feature 2', 1, '2024-09-20 13:34:57.288940'),
(9, 6, 'Feature 2', 1, '2024-09-20 13:34:57.289969'),
(10, 7, 'Feature 1', 1, '2024-09-20 13:35:08.316248'),
(11, 7, 'Feature 2', 1, '2024-09-20 13:35:08.317777'),
(12, 7, 'Feature 2', 1, '2024-09-20 13:35:08.319093'),
(13, 8, 'Feature 1', 1, '2024-09-20 13:35:19.169977'),
(14, 8, 'Feature 2', 1, '2024-09-20 13:35:19.170989'),
(15, 8, 'Feature 2', 1, '2024-09-20 13:35:19.171794'),
(16, 9, 'Feature 1', 1, '2024-09-20 14:15:48.574222'),
(17, 9, 'Feature 2', 1, '2024-09-20 14:15:48.576128'),
(18, 9, 'Feature 2', 1, '2024-09-20 14:15:48.577733'),
(19, 9, 'Feature 2', 1, '2024-09-20 14:15:48.579340'),
(163, 32, 'jhb', 1, '2024-11-30 18:34:40.177052'),
(164, 32, 'efs', 1, '2024-11-30 18:34:40.189825'),
(171, 12, 'Feature 1', 1, '2024-11-30 19:05:14.824739'),
(172, 12, 'Feature 2', 1, '2024-11-30 19:05:14.827347'),
(173, 12, 'Feature 1', 1, '2024-11-30 19:05:14.828258'),
(174, 12, 'Feature 2', 1, '2024-11-30 19:05:14.828930'),
(175, 31, 'mjhb jn', 1, '2024-11-30 19:05:38.500953'),
(176, 31, 'hgvh', 1, '2024-11-30 19:05:38.504886'),
(181, 20, 'Feature 1', 1, '2024-12-01 07:26:27.243973'),
(182, 20, 'Feature 2', 1, '2024-12-01 07:26:27.248909'),
(183, 20, 'Feature 1', 1, '2024-12-01 07:26:27.249880'),
(184, 20, 'Feature 2', 1, '2024-12-01 07:26:27.250727'),
(185, 16, 'Feature 1', 1, '2024-12-01 07:26:32.500319'),
(186, 16, 'Feature 2', 1, '2024-12-01 07:26:32.503413'),
(187, 16, 'Feature 1', 1, '2024-12-01 07:26:32.504498'),
(188, 16, 'Feature 2', 1, '2024-12-01 07:26:32.506659'),
(189, 18, 'Feature 1', 1, '2024-12-01 07:26:39.224173'),
(190, 18, 'Feature 2', 1, '2024-12-01 07:26:39.226449'),
(191, 18, 'Feature 1', 1, '2024-12-01 07:26:39.228535'),
(192, 18, 'Feature 2', 1, '2024-12-01 07:26:39.229992'),
(193, 17, 'Feature 1', 1, '2024-12-01 07:26:45.224641'),
(194, 17, 'Feature 2', 1, '2024-12-01 07:26:45.226280'),
(195, 17, 'Feature 1', 1, '2024-12-01 07:26:45.227441'),
(196, 17, 'Feature 2', 1, '2024-12-01 07:26:45.228902'),
(197, 19, 'Feature 1', 1, '2024-12-01 07:26:50.906404'),
(198, 19, 'Feature 2', 1, '2024-12-01 07:26:50.909582'),
(199, 19, 'Feature 1', 1, '2024-12-01 07:26:50.911118'),
(200, 19, 'Feature 2', 1, '2024-12-01 07:26:50.912235'),
(201, 23, 'Feature 1', 1, '2024-12-01 07:26:57.146398'),
(202, 23, 'Feature 2', 1, '2024-12-01 07:26:57.149530'),
(203, 23, 'Feature 1', 1, '2024-12-01 07:26:57.150663'),
(204, 23, 'Feature 2', 1, '2024-12-01 07:26:57.151409'),
(205, 26, 'susyem', 1, '2024-12-01 07:27:04.204814'),
(206, 27, 'kiuhnji', 1, '2024-12-01 08:37:29.455487'),
(207, 14, 'Feature 1', 1, '2024-12-01 08:38:11.005396'),
(208, 14, 'Feature 2', 1, '2024-12-01 08:38:11.007770'),
(209, 14, 'Feature 1', 1, '2024-12-01 08:38:11.008438'),
(210, 14, 'Feature 2', 1, '2024-12-01 08:38:11.008867'),
(211, 15, 'Feature 1', 1, '2024-12-01 08:38:16.515396'),
(212, 15, 'Feature 2', 1, '2024-12-01 08:38:16.516090'),
(213, 15, 'Feature 1', 1, '2024-12-01 08:38:16.516711'),
(214, 15, 'Feature 2', 1, '2024-12-01 08:38:16.517479'),
(215, 21, 'Feature 1', 1, '2024-12-01 08:38:22.306909'),
(216, 21, 'Feature 2', 1, '2024-12-01 08:38:22.308895'),
(217, 21, 'Feature 1', 1, '2024-12-01 08:38:22.309529'),
(218, 21, 'Feature 2', 1, '2024-12-01 08:38:22.309909'),
(219, 22, 'Feature 1', 1, '2024-12-01 08:38:27.954471'),
(220, 22, 'Feature 2', 1, '2024-12-01 08:38:27.955139'),
(221, 22, 'Feature 1', 1, '2024-12-01 08:38:27.955551'),
(222, 22, 'Feature 2', 1, '2024-12-01 08:38:27.956033'),
(223, 24, 'juhybuj', 1, '2024-12-01 08:38:34.458150'),
(224, 28, 'jhbgj', 1, '2024-12-01 08:38:47.300282'),
(225, 28, 'hjnj', 1, '2024-12-01 08:38:47.300882'),
(226, 33, 'delievry app', 1, '2024-12-01 08:46:29.466053'),
(227, 33, 'tracking', 1, '2024-12-01 08:46:29.470549'),
(240, 35, 'name', 1, '2024-12-01 16:32:01.883100'),
(247, 13, 'Feature 1', 0, '2024-12-01 16:58:57.586179'),
(248, 13, 'Feature 2', 0, '2024-12-01 16:58:57.587809'),
(249, 13, 'Feature 1', 0, '2024-12-01 16:58:57.588668'),
(250, 13, 'Feature 2', 0, '2024-12-01 16:58:57.589391'),
(257, 10, 'name', 0, '2024-12-01 17:00:36.945207'),
(258, 10, 'name', 0, '2024-12-01 17:00:36.946555'),
(259, 10, 'name', 0, '2024-12-01 17:00:36.948145'),
(260, 10, 'name', 0, '2024-12-01 17:00:36.949572'),
(261, 10, 'name', 0, '2024-12-01 17:00:36.950663'),
(262, 10, 'name', 0, '2024-12-01 17:00:36.952201'),
(263, 11, 'Feature 1', 0, '2024-12-02 10:28:51.992204'),
(264, 11, 'Feature 2', 0, '2024-12-02 10:28:52.014051'),
(268, 44, 'dewdw', 0, '2024-12-02 18:31:02.392322');

-- --------------------------------------------------------

--
-- Table structure for table `houseproducts`
--

CREATE TABLE `houseproducts` (
  `poid` int NOT NULL,
  `name` varchar(225) DEFAULT NULL,
  `description` varchar(225) DEFAULT NULL,
  `datetime` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `status` int NOT NULL DEFAULT '0',
  `category` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `planscheme_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `houseproducts`
--

INSERT INTO `houseproducts` (`poid`, `name`, `description`, `datetime`, `status`, `category`, `image`, `planscheme_id`) VALUES
(10, 'houseupdate ne', 'This is a new house product 3 updated', '2024-09-21 16:18:10.450599', 1, 'Business', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(11, 'New House Product 3', 'This is a new house product 3', '2024-09-21 16:18:22.699442', 1, 'Business', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(12, 'New House Product 4', 'This is a new house product 3', '2024-09-21 16:18:35.547512', 1, 'Business', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(13, 'New House Product 5', 'This is a new house product 3', '2024-09-21 16:19:44.399144', 0, 'Portfolio', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(14, 'New House Product 6', 'This is a new house product 3', '2024-09-21 16:19:55.153933', 1, 'Portfolio', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(15, 'New House Product 8', 'This is a new house product 3', '2024-09-21 16:20:28.701198', 0, 'E-commerce', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(16, 'New House Product 10', 'This is a new house product 3', '2024-09-21 16:21:08.858419', 0, 'E-commerce', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(17, 'New House Product 11', 'This is a new house product 15', '2024-09-21 16:21:55.771563', 1, 'Blog', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(18, 'New House Product 12', 'This is a new house product 15', '2024-09-21 16:22:04.457539', 0, 'Blog', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(19, 'New House Product 15', 'This is a new house product 15', '2024-09-21 16:22:31.338324', 1, 'Landing Pages', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(20, 'New House Product 16', 'This is a new house product 15', '2024-09-21 16:22:48.321994', 0, 'Landing Pages', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(21, 'New House Product 17', 'This is a new house product 15', '2024-09-21 16:23:17.161388', 1, 'Agency', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(22, 'New House Product 18', 'This is a new house product 15', '2024-09-21 16:28:04.297073', 0, 'Agency', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(23, 'New House Product 19', 'This is a new house product 15', '2024-09-21 16:28:11.663459', 1, 'Agency', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(24, 'hgyu', 'jyguhgvyujg kihui', '2024-11-25 18:09:42.414305', 0, 'E-commerce', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(25, 'whjbh', 'hgvghvgh', '2024-11-25 19:06:39.639791', 1, 'Portfolio', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(26, 'new testing', 'the contact tyhe cdeisjkhsd uygujgbs hvysbhj', '2024-11-26 06:03:07.115141', 0, 'Business', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(27, 'dfvds', 'jhybyuj jujygbuj jujby', '2024-11-26 06:22:39.002213', 0, 'Portfolio', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(28, 'kjunhj', 'jhbj', '2024-11-26 06:42:17.766137', 0, 'Portfolio', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(29, 'jyhgbhj', 'jygbhj', '2024-11-26 09:55:08.283885', 0, 'Agency', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(30, 'hygvhu', 'hygftyhfgvtyfy', '2024-11-26 10:07:06.377887', 1, 'Landing Pages', 'https://i.ibb.co/VQQbV7y/Hello-Guys-I-m-excited-to-introduce-my-food-delivery-mobile-app-UI-design-which-was-created-specific.jpg', 469259),
(31, 'dscs', 'kjnbhjb', '2024-11-26 13:21:19.795095', 1, 'E-commerce', 'https://i.ibb.co/wQHw1vF/Whats-App-Image-2024-11-24-at-5-46-35-AM.jpg', 469259),
(32, 'jybghj', 'jyhbjhb ', '2024-11-30 14:24:37.347733', 1, 'Business', 'https://i.ibb.co/wJGp1b2/DALL-E-2024-11-12-23-41-54-A-3-D-box-design-with-an-ice-cute-theme-incorporating-a-gradient-backgrou.webp', 469259),
(33, 'Biryanis', 'kjubnjhbjhbv\njvbhhjbv \njhbj\njhbjvb hvhvgcvgcgcvg jsgbdhj   gbhjb', '2024-12-01 08:46:29.381894', 1, 'Food', 'https://i.ibb.co/jkyVZ2Y/DALL-E-2024-11-02-11-00-12-A-professional-and-inviting-image-for-a-technology-landing-page-with-the.jpg', 469259),
(34, 'PIZZHUT', 'JHB J JBHYJhujknhj hbujKJU', '2024-12-01 16:31:36.957176', 0, 'Food', 'https://i.ibb.co/hgfdD1x/Hello-everyone-I-want-to-share-my-recent-exploration-of-the-online-Grocery-Shop-mobile-app-UI-design.jpg', 469259),
(35, 'PIZZHUT', 'JHB J JBHYJhujknhj hbujKJU', '2024-12-01 16:32:01.848774', 0, 'Food', 'https://i.ibb.co/hgfdD1x/Hello-everyone-I-want-to-share-my-recent-exploration-of-the-online-Grocery-Shop-mobile-app-UI-design.jpg', 469259),
(36, 'dcs', 'sdcsddcd', '2024-12-02 16:52:00.081730', 0, 'Food', 'https://i.ibb.co/609hHDC/Whats-App-Image-2024-11-24-at-5-46-35-AM.jpg', 469259),
(37, 'verggies', 'jhbghjb uygbyhuj uygu jyhb', '2024-12-02 18:14:01.782895', 0, 'Grocery', 'https://i.ibb.co/NrypzNx/DALL-E-2024-11-02-10-49-10-A-modern-professional-hero-image-for-a-technology-landing-page-titled-Tem.jpg', 469259),
(38, 'jybh j', 'jhb gj', '2024-12-02 18:15:01.844787', 0, 'Fashion', 'https://i.ibb.co/1mm1R8q/splash-animation.png', 469259),
(39, 'jybh j', 'jhb gj', '2024-12-02 18:16:58.103665', 0, 'Fashion', 'https://i.ibb.co/1mm1R8q/splash-animation.png', 469259),
(40, 'jybh j', 'jhb gj', '2024-12-02 18:20:35.311173', 0, 'Fashion', 'https://i.ibb.co/1mm1R8q/splash-animation.png', 469259),
(41, 'jhgb hj', 'jbhnj jjbyjh ', '2024-12-02 18:23:09.989078', 0, 'Agency', 'https://i.ibb.co/1mm1R8q/splash-animation.png', 469259),
(42, 'jhgb hj', 'jbhnj jjbyjh ', '2024-12-02 18:23:37.668835', 0, 'Agency', 'https://i.ibb.co/1mm1R8q/splash-animation.png', 469259),
(43, 'jhgb hj', 'jbhnj jjbyjh ', '2024-12-02 18:24:42.616492', 0, 'Agency', 'https://i.ibb.co/1mm1R8q/splash-animation.png', 469259),
(44, 'ngv gh', 'jbhj', '2024-12-02 18:28:16.622850', 0, 'Agency', 'https://i.ibb.co/TYgDfHt/pablo-merchan-montes-dc-JMu8lb5-U-unsplash.jpg', 469259);

-- --------------------------------------------------------

--
-- Table structure for table `houseproducttechnical`
--

CREATE TABLE `houseproducttechnical` (
  `tid` int NOT NULL,
  `poid` int NOT NULL,
  `name` varchar(225) DEFAULT NULL,
  `datetime` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `status` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `houseproducttechnical`
--

INSERT INTO `houseproducttechnical` (`tid`, `poid`, `name`, `datetime`, `status`) VALUES
(1, 4, 'Technical 1', '2024-09-20 13:31:23.707150', 1),
(2, 4, 'Technical 1', '2024-09-20 13:31:23.708624', 1),
(3, 4, 'Technical 1', '2024-09-20 13:31:23.709599', 1),
(4, 5, 'Technical 1', '2024-09-20 13:34:48.599783', 1),
(5, 5, 'Technical 1', '2024-09-20 13:34:48.600571', 1),
(6, 5, 'Technical 1', '2024-09-20 13:34:48.601405', 1),
(7, 6, 'Technical 1', '2024-09-20 13:34:57.291198', 1),
(8, 6, 'Technical 1', '2024-09-20 13:34:57.292463', 1),
(9, 6, 'Technical 1', '2024-09-20 13:34:57.296753', 1),
(10, 7, 'Technical 1', '2024-09-20 13:35:08.321364', 1),
(11, 7, 'Technical 1', '2024-09-20 13:35:08.322719', 1),
(12, 7, 'Technical 1', '2024-09-20 13:35:08.324129', 1),
(13, 8, 'Technical 1', '2024-09-20 13:35:19.173144', 1),
(14, 8, 'Technical 1', '2024-09-20 13:35:19.174346', 1),
(15, 8, 'Technical 1', '2024-09-20 13:35:19.176381', 1),
(16, 9, 'Technical 1', '2024-09-20 14:15:48.636372', 1),
(17, 9, 'Technical 1', '2024-09-20 14:15:48.637929', 1),
(18, 9, 'Technical 1', '2024-09-20 14:15:48.638929', 1),
(19, 9, 'Technical 1', '2024-09-20 14:15:48.640045', 1),
(159, 32, 'fcs', '2024-11-30 18:34:40.194095', 1),
(160, 32, 'fe', '2024-11-30 18:34:40.198008', 1),
(167, 12, 'Technical 1', '2024-11-30 19:05:14.829852', 1),
(168, 12, 'Technical 1', '2024-11-30 19:05:14.830552', 1),
(169, 12, 'Technical 1', '2024-11-30 19:05:14.831259', 1),
(170, 12, 'Technical 1', '2024-11-30 19:05:14.831977', 1),
(175, 20, 'Technical 1', '2024-12-01 07:26:27.251892', 1),
(176, 20, 'Technical 1', '2024-12-01 07:26:27.256300', 1),
(177, 20, 'Technical 1', '2024-12-01 07:26:27.257614', 1),
(178, 20, 'Technical 1', '2024-12-01 07:26:27.258430', 1),
(179, 16, 'Technical 1', '2024-12-01 07:26:32.510186', 1),
(180, 16, 'Technical 1', '2024-12-01 07:26:32.511704', 1),
(181, 16, 'Technical 1', '2024-12-01 07:26:32.512772', 1),
(182, 16, 'Technical 1', '2024-12-01 07:26:32.514366', 1),
(183, 18, 'Technical 1', '2024-12-01 07:26:39.231491', 1),
(184, 18, 'Technical 1', '2024-12-01 07:26:39.232579', 1),
(185, 18, 'Technical 1', '2024-12-01 07:26:39.233579', 1),
(186, 18, 'Technical 1', '2024-12-01 07:26:39.235056', 1),
(187, 17, 'Technical 1', '2024-12-01 07:26:45.230631', 1),
(188, 17, 'Technical 1', '2024-12-01 07:26:45.232307', 1),
(189, 17, 'Technical 1', '2024-12-01 07:26:45.233589', 1),
(190, 17, 'Technical 1', '2024-12-01 07:26:45.234558', 1),
(191, 19, 'Technical 1', '2024-12-01 07:26:50.913469', 1),
(192, 19, 'Technical 1', '2024-12-01 07:26:50.914352', 1),
(193, 19, 'Technical 1', '2024-12-01 07:26:50.917290', 1),
(194, 19, 'Technical 1', '2024-12-01 07:26:50.918867', 1),
(195, 23, 'Technical 1', '2024-12-01 07:26:57.152421', 1),
(196, 23, 'Technical 1', '2024-12-01 07:26:57.153466', 1),
(197, 23, 'Technical 1', '2024-12-01 07:26:57.154551', 1),
(198, 23, 'Technical 1', '2024-12-01 07:26:57.155519', 1),
(199, 26, 'jhbj', '2024-12-01 07:27:04.207486', 1),
(200, 27, 'mhb j', '2024-12-01 08:37:29.464544', 1),
(201, 14, 'Technical 1', '2024-12-01 08:38:11.009435', 1),
(202, 14, 'Technical 1', '2024-12-01 08:38:11.009860', 1),
(203, 14, 'Technical 1', '2024-12-01 08:38:11.010205', 1),
(204, 14, 'Technical 1', '2024-12-01 08:38:11.011180', 1),
(205, 15, 'Technical 1', '2024-12-01 08:38:16.518567', 1),
(206, 15, 'Technical 1', '2024-12-01 08:38:16.519506', 1),
(207, 15, 'Technical 1', '2024-12-01 08:38:16.520075', 1),
(208, 15, 'Technical 1', '2024-12-01 08:38:16.520505', 1),
(209, 21, 'Technical 1', '2024-12-01 08:38:22.311177', 1),
(210, 21, 'Technical 1', '2024-12-01 08:38:22.311596', 1),
(211, 21, 'Technical 1', '2024-12-01 08:38:22.311948', 1),
(212, 21, 'Technical 1', '2024-12-01 08:38:22.312277', 1),
(213, 22, 'Technical 1', '2024-12-01 08:38:27.956832', 1),
(214, 22, 'Technical 1', '2024-12-01 08:38:27.957325', 1),
(215, 22, 'Technical 1', '2024-12-01 08:38:27.957767', 1),
(216, 22, 'Technical 1', '2024-12-01 08:38:27.958388', 1),
(217, 28, 'jhbhj', '2024-12-01 08:38:47.301453', 1),
(218, 28, 'limki', '2024-12-01 08:38:47.301841', 1),
(219, 33, 'admin dashboard', '2024-12-01 08:46:29.471834', 1),
(220, 33, 'anayalic', '2024-12-01 08:46:29.478151', 1),
(233, 35, 'name', '2024-12-01 16:32:01.886730', 1),
(240, 13, 'Technical 1', '2024-12-01 16:58:57.591474', 0),
(241, 13, 'Technical 1', '2024-12-01 16:58:57.594723', 0),
(242, 13, 'Technical 1', '2024-12-01 16:58:57.596292', 0),
(243, 13, 'Technical 1', '2024-12-01 16:58:57.597061', 0),
(250, 10, 'name', '2024-12-01 17:00:36.953580', 0),
(251, 10, 'name', '2024-12-01 17:00:36.954373', 0),
(252, 10, 'name', '2024-12-01 17:00:36.955373', 0),
(253, 10, 'name', '2024-12-01 17:00:36.956230', 0),
(254, 10, 'name', '2024-12-01 17:00:36.956994', 0),
(255, 10, 'name', '2024-12-01 17:00:36.957790', 0),
(256, 11, 'Technical 1', '2024-12-02 10:28:52.023830', 0),
(257, 11, 'Technical 1', '2024-12-02 10:28:52.025830', 0),
(260, 44, 'yghg', '2024-12-02 18:31:02.394209', 0);

-- --------------------------------------------------------

--
-- Table structure for table `houseuser`
--

CREATE TABLE `houseuser` (
  `id` int NOT NULL,
  `email` varchar(225) DEFAULT NULL,
  `password` varchar(225) DEFAULT NULL,
  `date` varchar(225) DEFAULT NULL,
  `date_time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `status` int NOT NULL DEFAULT '0',
  `username` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `houseuser`
--

INSERT INTO `houseuser` (`id`, `email`, `password`, `date`, `date_time`, `status`, `username`) VALUES
(1, 'string', 'string', 'string', '2024-09-03 15:14:06.454106', 0, NULL),
(2, 'string', 'string', '2024-09-03', '2024-09-03 15:20:05.343671', 0, NULL),
(3, 'user@example.com', '123', '2024-09-03', '2024-09-03 15:33:28.844614', 0, 'test'),
(4, 'test1@gmail.com', '123', '2024-09-04', '2024-09-04 16:40:33.353261', 0, 'test'),
(5, 'jhbdxj@gmail.com', '123', '2024-09-20', '2024-09-20 11:05:32.124357', 0, 'jshdj'),
(6, 'durga@gamil.com', 'string', '2024-11-22', '2024-11-22 16:20:19.036530', 0, 'durga prasad'),
(7, 'hgvh@gmail.com', '12345678', '2024-11-22', '2024-11-22 16:51:47.226651', 0, 'jhbyjbhj'),
(8, 'sdjhbvj@gmail.com', '12345678', '2024-11-22', '2024-11-22 17:26:13.220049', 0, 'testing new data');

-- --------------------------------------------------------

--
-- Table structure for table `houseusersettings`
--

CREATE TABLE `houseusersettings` (
  `sid` int NOT NULL,
  `field` varchar(225) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `value` varchar(225) NOT NULL,
  `id` int NOT NULL,
  `datetime` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `houseusersettings`
--

INSERT INTO `houseusersettings` (`sid`, `field`, `value`, `id`, `datetime`) VALUES
(2, 'emailNotifications', 'enabled', 6, '2024-11-24 09:48:53.117401'),
(3, 'marketingEmails', 'enabled', 6, '2024-11-24 09:48:55.231307'),
(4, 'newProductAlerts', 'enabled', 6, '2024-11-24 09:48:57.131164'),
(5, 'orderUpdates', 'enabled', 6, '2024-11-24 09:48:58.603596'),
(6, 'twoFactorAuth', 'enabled', 6, '2024-11-24 10:40:46.279063');

-- --------------------------------------------------------

--
-- Table structure for table `otp_verification`
--

CREATE TABLE `otp_verification` (
  `oid` int NOT NULL,
  `email` varchar(225) NOT NULL,
  `otp` varchar(225) NOT NULL,
  `expires_at` datetime(6) NOT NULL,
  `id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `otp_verification`
--

INSERT INTO `otp_verification` (`oid`, `email`, `otp`, `expires_at`, `id`) VALUES
(1, 'user@example.com', '721712', '2024-12-02 16:25:28.689037', 6);

-- --------------------------------------------------------

--
-- Table structure for table `plans`
--

CREATE TABLE `plans` (
  `pid` int NOT NULL,
  `name` varchar(225) NOT NULL,
  `base_price` float NOT NULL,
  `description` varchar(225) NOT NULL,
  `planscheme_id` int DEFAULT NULL,
  `includedFeatures` varchar(225) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `plans`
--

INSERT INTO `plans` (`pid`, `name`, `base_price`, `description`, `planscheme_id`, `includedFeatures`) VALUES
(30, 'Basic', 40, 'Get started with essential features', 469259, '23'),
(31, 'Pro', 70, 'Advanced features for professionals', 469259, '21,22,23,24'),
(32, 'Enterprise', 150, 'Full suite of features for large teams', 469259, '26,25,24,23,22,21');

-- --------------------------------------------------------

--
-- Table structure for table `price`
--

CREATE TABLE `price` (
  `pid` int NOT NULL,
  `poid` int NOT NULL,
  `amount` varchar(225) DEFAULT NULL,
  `name` varchar(225) DEFAULT NULL,
  `status` int NOT NULL DEFAULT '0',
  `datetime` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `description` varchar(225) DEFAULT NULL,
  `key` varchar(225) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `price`
--

INSERT INTO `price` (`pid`, `poid`, `amount`, `name`, `status`, `datetime`, `description`, `key`) VALUES
(1, 8, '500', 'testing', 0, '2024-09-04 17:01:05.369858', 'testing new', 'string'),
(2, 9, '1000', 'Standard Price', 1, '2024-09-20 14:15:48.645615', 'Basic price for the product', 'P123'),
(3, 10, '580', 'houseupdate ne', 0, '2024-09-21 16:18:10.642753', 'This is a new house product 3 updated', 'cyyaZnPF'),
(4, 11, '1000', 'New House Product 3', 0, '2024-09-21 16:18:22.788025', 'This is a new house product 3', 'qZPQJgmw'),
(5, 12, '1000', 'Standard Price', 1, '2024-09-21 16:18:35.606378', 'Basic price for the product', 'P123'),
(6, 13, '1000', 'Standard Price', 1, '2024-09-21 16:19:44.448899', 'Basic price for the product', 'P123'),
(7, 14, '1000', 'Standard Price', 1, '2024-09-21 16:19:55.225979', 'Basic price for the product', 'P123'),
(8, 15, '1000', 'Standard Price', 1, '2024-09-21 16:20:28.775015', 'Basic price for the product', 'P123'),
(9, 16, '1000', 'Standard Price', 1, '2024-09-21 16:21:08.903762', 'Basic price for the product', 'P123'),
(10, 17, '1000', 'Standard Price', 1, '2024-09-21 16:21:55.821370', 'Basic price for the product', 'P123'),
(11, 18, '1000', 'Standard Price', 1, '2024-09-21 16:22:04.542367', 'Basic price for the product', 'P123'),
(12, 19, '1000', 'Standard Price', 1, '2024-09-21 16:22:31.394156', 'Basic price for the product', 'P123'),
(13, 20, '1000', 'Standard Price', 1, '2024-09-21 16:22:49.065335', 'Basic price for the product', 'P123'),
(14, 21, '1000', 'Standard Price', 1, '2024-09-21 16:23:17.218036', 'Basic price for the product', 'P123'),
(15, 22, '1000', 'Standard Price', 1, '2024-09-21 16:28:04.362778', 'Basic price for the product', 'P123'),
(16, 23, '1000', 'Standard Price', 1, '2024-09-21 16:28:11.712139', 'Basic price for the product', 'P123'),
(17, 24, '500', 'hgyu', 0, '2024-11-25 18:09:42.558467', 'jyguhgvyujg kihui', 'OSYA51MB'),
(18, 25, '7', 'whjbh', 0, '2024-11-25 19:06:39.723369', 'hgvghvgh', '52wb6uiE'),
(19, 26, '500', 'new testing', 0, '2024-11-26 06:03:07.189323', 'the contact tyhe cdeisjkhsd uygujgbs hvysbhj', '8gmBsP9V'),
(20, 27, '800', 'dfvds', 0, '2024-11-26 06:22:39.055708', 'jhybyuj jujygbuj jujby', 'skICGw2F'),
(21, 28, '514', 'kjunhj', 0, '2024-11-26 06:42:17.875768', 'jhbj', 'oOVZDzFm'),
(22, 29, '568', 'jyhgbhj', 0, '2024-11-26 09:55:08.302372', 'jygbhj', 'WvYsxjCx'),
(23, 30, '855', 'hygvhu', 0, '2024-11-26 10:07:06.418228', 'hygftyhfgvtyfy', 'O14b6qju'),
(24, 31, '68597', 'dscs', 0, '2024-11-26 13:21:19.891552', 'kjnbhjb', 'pxV3pLYt');

-- --------------------------------------------------------

--
-- Table structure for table `subscriptions`
--

CREATE TABLE `subscriptions` (
  `suid` int NOT NULL,
  `id` int NOT NULL,
  `poid` int NOT NULL,
  `plan_name` varchar(225) NOT NULL,
  `amount` float NOT NULL,
  `payment_method` varchar(225) NOT NULL,
  `type_payment` varchar(225) DEFAULT NULL,
  `status` varchar(225) NOT NULL,
  `billing_cycle` varchar(225) NOT NULL,
  `billing_date` varchar(225) NOT NULL,
  `expiration_date` datetime(6) NOT NULL,
  `current_price` float NOT NULL,
  `selected_features` varchar(225) NOT NULL,
  `created_at` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `updated_at` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `subscriptions`
--

INSERT INTO `subscriptions` (`suid`, `id`, `poid`, `plan_name`, `amount`, `payment_method`, `type_payment`, `status`, `billing_cycle`, `billing_date`, `expiration_date`, `current_price`, `selected_features`, `created_at`, `updated_at`) VALUES
(25, 6, 10, 'Pro', 86.49, 'Credit Card', 'first_payment', 'canceled', 'monthly', '2024-12-02 12:46:27.256000', '2025-01-02 12:46:27.286000', 86.49, '21,22,23,24,25,26,27', '2024-12-02 12:46:27.497904', '2024-12-02 15:51:18.473475'),
(26, 6, 12, 'Enterprise', 148.8, 'Credit Card', 'first_payment', 'canceled', 'monthly', '2024-12-02 12:47:43.432000', '2025-01-02 12:47:43.432000', 148.8, '21,22,23,24,25,26,27', '2024-12-02 12:47:43.455897', '2024-12-02 15:51:27.634017'),
(27, 6, 10, 'Pro', 86.49, 'Credit Card', 'first_payment', 'active', 'monthly', '2024-12-02 18:34:51.746000', '2025-01-02 18:34:51.759000', 86.49, '21,22,23,24,25,26,27', '2024-12-02 18:34:51.916650', '2024-12-02 18:34:51.916650');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customizationrequest`
--
ALTER TABLE `customizationrequest`
  ADD PRIMARY KEY (`rid`);

--
-- Indexes for table `features`
--
ALTER TABLE `features`
  ADD PRIMARY KEY (`feid`);

--
-- Indexes for table `housedeviceimages`
--
ALTER TABLE `housedeviceimages`
  ADD PRIMARY KEY (`dimd`);

--
-- Indexes for table `houseimages`
--
ALTER TABLE `houseimages`
  ADD PRIMARY KEY (`imd`);

--
-- Indexes for table `houseoffers`
--
ALTER TABLE `houseoffers`
  ADD PRIMARY KEY (`oid`);

--
-- Indexes for table `houseorders`
--
ALTER TABLE `houseorders`
  ADD PRIMARY KEY (`oid`);

--
-- Indexes for table `houseproductcompatibility`
--
ALTER TABLE `houseproductcompatibility`
  ADD PRIMARY KEY (`cid`);

--
-- Indexes for table `houseproductcustomelements`
--
ALTER TABLE `houseproductcustomelements`
  ADD PRIMARY KEY (`cpid`);

--
-- Indexes for table `houseproductfeature`
--
ALTER TABLE `houseproductfeature`
  ADD PRIMARY KEY (`fid`);

--
-- Indexes for table `houseproducts`
--
ALTER TABLE `houseproducts`
  ADD PRIMARY KEY (`poid`);

--
-- Indexes for table `houseproducttechnical`
--
ALTER TABLE `houseproducttechnical`
  ADD PRIMARY KEY (`tid`);

--
-- Indexes for table `houseuser`
--
ALTER TABLE `houseuser`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `houseusersettings`
--
ALTER TABLE `houseusersettings`
  ADD PRIMARY KEY (`sid`);

--
-- Indexes for table `otp_verification`
--
ALTER TABLE `otp_verification`
  ADD PRIMARY KEY (`oid`);

--
-- Indexes for table `plans`
--
ALTER TABLE `plans`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `price`
--
ALTER TABLE `price`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `subscriptions`
--
ALTER TABLE `subscriptions`
  ADD PRIMARY KEY (`suid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customizationrequest`
--
ALTER TABLE `customizationrequest`
  MODIFY `rid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `features`
--
ALTER TABLE `features`
  MODIFY `feid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `housedeviceimages`
--
ALTER TABLE `housedeviceimages`
  MODIFY `dimd` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `houseimages`
--
ALTER TABLE `houseimages`
  MODIFY `imd` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `houseoffers`
--
ALTER TABLE `houseoffers`
  MODIFY `oid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `houseorders`
--
ALTER TABLE `houseorders`
  MODIFY `oid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `houseproductcompatibility`
--
ALTER TABLE `houseproductcompatibility`
  MODIFY `cid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `houseproductcustomelements`
--
ALTER TABLE `houseproductcustomelements`
  MODIFY `cpid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `houseproductfeature`
--
ALTER TABLE `houseproductfeature`
  MODIFY `fid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=269;

--
-- AUTO_INCREMENT for table `houseproducts`
--
ALTER TABLE `houseproducts`
  MODIFY `poid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `houseproducttechnical`
--
ALTER TABLE `houseproducttechnical`
  MODIFY `tid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=261;

--
-- AUTO_INCREMENT for table `houseuser`
--
ALTER TABLE `houseuser`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `houseusersettings`
--
ALTER TABLE `houseusersettings`
  MODIFY `sid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `otp_verification`
--
ALTER TABLE `otp_verification`
  MODIFY `oid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `plans`
--
ALTER TABLE `plans`
  MODIFY `pid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `price`
--
ALTER TABLE `price`
  MODIFY `pid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `subscriptions`
--
ALTER TABLE `subscriptions`
  MODIFY `suid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
