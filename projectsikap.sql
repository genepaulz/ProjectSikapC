-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 22, 2021 at 04:40 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `projectsikap`
--

-- --------------------------------------------------------

--
-- Table structure for table `applicant`
--

CREATE TABLE `applicant` (
  `id` bigint(20) NOT NULL,
  `age` int(11) NOT NULL,
  `position` varchar(100) NOT NULL,
  `applicantUser_id` bigint(20) NOT NULL,
  `ratings_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `applicant`
--

INSERT INTO `applicant` (`id`, `age`, `position`, `applicantUser_id`, `ratings_id`) VALUES
(1, 30, '', 1, 1),
(2, 43, '', 2, 2),
(3, 31, '', 3, 3),
(4, 43, '', 4, 4),
(5, 33, '', 5, 5),
(6, 23, '', 6, 6),
(7, 41, '', 7, 7),
(8, 37, '', 8, 8),
(9, 43, '', 9, 9),
(10, 38, '', 10, 10),
(11, 32, '', 11, 11),
(12, 43, '', 12, 12),
(13, 41, '', 13, 13),
(14, 27, '', 14, 14),
(15, 43, '', 15, 15),
(16, 23, '', 16, 16),
(17, 32, '', 17, 17),
(18, 27, '', 18, 18),
(19, 26, '', 19, 19),
(20, 30, '', 20, 20),
(21, 37, '', 21, 21),
(22, 44, '', 22, 22),
(23, 45, '', 23, 23),
(24, 26, '', 24, 24),
(25, 23, '', 25, 25),
(26, 45, '', 26, 26),
(27, 28, '', 27, 27),
(28, 31, '', 28, 28),
(29, 29, '', 29, 29),
(30, 45, '', 30, 30),
(31, 37, '', 31, 31),
(32, 26, '', 32, 32),
(33, 29, '', 33, 33),
(34, 23, '', 34, 34),
(35, 43, '', 35, 35),
(36, 38, '', 36, 36),
(37, 24, '', 37, 37),
(38, 36, '', 38, 38),
(39, 29, '', 39, 39),
(40, 41, '', 40, 40);

-- --------------------------------------------------------

--
-- Table structure for table `employer`
--

CREATE TABLE `employer` (
  `employerUser_id` bigint(20) NOT NULL,
  `companyName` varchar(100) NOT NULL,
  `matches` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employer`
--

INSERT INTO `employer` (`employerUser_id`, `companyName`, `matches`) VALUES
(41, 'Teslta', 0),
(42, 'Bookerface', 0),
(43, 'Congo', 0),
(44, 'AliBobo', 0),
(45, 'Doors', 0),
(46, 'Cebu Technologically Oriented School', 0),
(47, 'ShoeMart', 0),
(48, 'BackRow', 0),
(49, 'SubdiVision', 0),
(50, 'BathSolutions', 0);

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `id` bigint(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `region` varchar(10) NOT NULL,
  `province` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `age` int(11) NOT NULL,
  `industry` varchar(100) NOT NULL,
  `yearsOfExperience` int(11) NOT NULL,
  `position` varchar(100) NOT NULL,
  `dateAdded` datetime(6) NOT NULL,
  `isAgeViewable` int(11) NOT NULL,
  `isDeleted` int(11) NOT NULL,
  `applicantID_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `rating`
--

CREATE TABLE `rating` (
  `id` bigint(20) NOT NULL,
  `rating` double NOT NULL,
  `numOfRates` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rating`
--

INSERT INTO `rating` (`id`, `rating`, `numOfRates`) VALUES
(1, 0, 0),
(2, 0, 0),
(3, 0, 0),
(4, 0, 0),
(5, 0, 0),
(6, 0, 0),
(7, 0, 0),
(8, 0, 0),
(9, 0, 0),
(10, 0, 0),
(11, 0, 0),
(12, 0, 0),
(13, 0, 0),
(14, 0, 0),
(15, 0, 0),
(16, 0, 0),
(17, 0, 0),
(18, 0, 0),
(19, 0, 0),
(20, 0, 0),
(21, 0, 0),
(22, 0, 0),
(23, 0, 0),
(24, 0, 0),
(25, 0, 0),
(26, 0, 0),
(27, 0, 0),
(28, 0, 0),
(29, 0, 0),
(30, 0, 0),
(31, 0, 0),
(32, 0, 0),
(33, 0, 0),
(34, 0, 0),
(35, 0, 0),
(36, 0, 0),
(37, 0, 0),
(38, 0, 0),
(39, 0, 0),
(40, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `rating_rateremail`
--

CREATE TABLE `rating_rateremail` (
  `id` bigint(20) NOT NULL,
  `rating_id` bigint(20) NOT NULL,
  `employer_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` bigint(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `industry` varchar(100) NOT NULL,
  `region` varchar(10) NOT NULL,
  `province` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `isVerified` int(11) NOT NULL,
  `isDeleted` int(11) NOT NULL,
  `user_type` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `email`, `password`, `firstname`, `lastname`, `industry`, `region`, `province`, `city`, `isVerified`, `isDeleted`, `user_type`) VALUES
(1, 'ameerah_villarreal@email.com', '$pbkdf2-sha256$10$i3EuBcA4Z8y5t3auNcYYAw$ks7g3xmUapWCZsPiGBpi7OJGo930MTO1m1r2HdAxdGw', 'Ameerah', 'Villarreal', 'Technology', 'VII', 'Cebu', 'Cebu', 0, 0, 0),
(2, 'larry.portillo@email.com', '$pbkdf2-sha256$10$SWnNude6d66VMoaQ0tr7nw$M0y8LaIdjEirRTCjcS.YzLFZVTtdrlQEfLAtGhtWEEc', 'Larry', 'Portillo', 'Technology', 'VII', 'Cebu', 'Lapu-Lapu', 0, 0, 0),
(3, 'usmaan_simons@email.com', '$pbkdf2-sha256$10$DiFEyFmr9b73vpfS2vs/Zw$2P3hmjQrBkHCd8x93yPL1L8b9tVNgxQtuTnvEdcAvTw', 'Usmaan', 'Simons', 'BPO', 'VII', 'Cebu', 'Cebu', 0, 0, 0),
(4, 'adil_lane@email.com', '$pbkdf2-sha256$10$C6E0BiBECKG0tjZmLIWwlg$lrhwRb71d69bkJW4MSPmzR9YvD2p/XYXZ2Yqf9qcT.c', 'Adil', 'Lane', 'Education', 'VII', 'Cebu', 'Cebu', 0, 0, 0),
(5, 'pearl_cresswell@email.com', '$pbkdf2-sha256$10$XmsNAWBsLUXIOQcgBOB8zw$KWDrTLkRg70x7s0uAtLxEmCKiYNYtC.JqishyfAhrDM', 'Pearl', 'Cresswell', 'Technology', 'VII', 'Cebu', 'Mandaue', 0, 0, 0),
(6, 'zakariyah.rosas32@email.com', '$pbkdf2-sha256$10$.5/TGsN4j7EWYsy5F4KwNg$juqqsUKgyzmUar71b7/D/BL8ve88v6dMTMMwsnfnaVo', 'Zakariyah', 'Rosas', 'Hospitality Management', 'VII', 'Cebu', 'Lapu-Lapu', 0, 0, 0),
(7, 'dougie_marks@email.com', '$pbkdf2-sha256$10$1hpD6L2X8j5HqBVCyJmTMg$qAS3rg.AkcAKLkS9pjHFw9JXlq3ytNMX2eFluZbiAsY', 'Dougie', 'Marks', 'Hospitality Management', 'VII', 'Cebu', 'Mandaue', 0, 0, 0),
(8, 'nimrah.wilkinson@email.com', '$pbkdf2-sha256$10$kLJ2bk3JmdMao1SqNca4tw$pIoQ0rSyizbEic3/A.Q0FZjBmq6UgRYg8cXH8oWSJZ4', 'Nimrah', 'Wilkinsons', 'Manufacturing', 'VII', 'Cebu', 'Mandaue', 0, 0, 0),
(9, 'appleton.cherry@email.com', '$pbkdf2-sha256$10$p7T23vtf6x3DmJNSqvX.fw$8U/Zi2bZZp97hexJ4CF7nxlr84Csjl/QZsY5vkXVE/g', 'Cherry', 'Appleton', 'Manufacturing', 'VII', 'Cebu', 'Mandaue', 0, 0, 0),
(10, 'wyatt_amaya@email.com', '$pbkdf2-sha256$10$3DvHmJMyRqgVAiCkFOK8Nw$cMLZkbYBwnmawVnQfhNZePTB9Jg3tYURsY70YB8oXao', 'Amaya', 'Wyatt', 'Education', 'VII', 'Cebu', 'Cebu', 0, 0, 0),
(11, 'mikolaj_ratliff@email.com', '$pbkdf2-sha256$10$KkXI2ft/D2HMeW9t7b137g$cxC01mVHbmHWk2RKCLBb5ANHSBE2wDQjjh8EQaLlBQI', 'Mikolaj', 'Ratliff', 'Technology', 'VII', 'Cebu', 'Lapu-Lapu', 0, 0, 0),
(12, 'barry.stevie@email.com', '$pbkdf2-sha256$10$WIsxxti7VyqltHaOsfaeMw$I1k5hjOXNnMIBG1lm3ABPha0rjyNWo5z6PJW.5aKzfA', 'Barry', 'Stevie', 'Technology', 'VII', 'Cebu', 'Lapu-Lapu', 0, 0, 0),
(13, 'liya_devine@email.com', '$pbkdf2-sha256$10$zRljbO1d650z5hwjxBjD.A$NjK1BaiM7lK27lSelV3tAjCA0MTAY3WJkbTPOJiqE0w', 'Liya', 'Devine', 'Manufacturing', 'VII', 'Cebu', 'Cebu', 0, 0, 0),
(14, 'ria.richardson@email.com', '$pbkdf2-sha256$10$RYixtra2trZW6p1Tag3hnA$n7cop5pL4Ohd7Fe4rz2HmL9/ypQUd0CEH3Au/XT6Onc', 'Ria', 'Richardson', 'BPO', 'VII', 'Cebu', 'Cebu', 0, 0, 0),
(15, 'glenda_hall@email.com', '$pbkdf2-sha256$10$bG3tPQfAmNM6B0CoVSrF.A$1UglRytUA0O.l8kAgFS923lmXWdSgYn1AwvqVGPtFdM', 'Glenda', 'Hall', 'Manufacturing', 'VII', 'Cebu', 'Cebu', 0, 0, 0),
(16, 'rosie_gillespie@email.com', '$pbkdf2-sha256$10$pVQqxVhL6d2bsxYCIKQ05g$DqitBqL.je/AZdwNmrS9GkkKN0H1aaoAeqxgjhii3dQ', 'Rosie', 'Gillepsie', 'BPO', 'VII', 'Cebu', 'Lapu-Lapu', 0, 0, 0),
(17, 'ford.matthias@email.com', '$pbkdf2-sha256$10$7x3jHEOI0VorhfD.v9daSw$AvXnU5C1ZTzqtPz5woaQ6VvEnURp96rqITmmWrrBdP4', 'Matthias', 'Ford', 'BPO', 'VII', 'Cebu', 'Lapu-Lapu', 0, 0, 0),
(18, 'inaaya_mill@email.com', '$pbkdf2-sha256$10$9b6XktJ6z/lfCyGkFKJ07g$JDG/voDLejrv1WmnMbNmSDHCmSd5qLX3UqczpHw049w', 'Inaaya', 'Mill', 'Education', 'VII', 'Cebu', 'Mandaue', 0, 0, 0),
(19, 'blundwell.aisling@email.com', '$pbkdf2-sha256$10$BeB8r/Xee895jxGiNIawFg$NjsL5EekcT7Pw5DxzyHzbYr2SjMG/P3WTTk5oQJ0b3k', 'Aisling', 'Blundwell', 'Hospitality Management', 'VII', 'Cebu', 'Mandaue', 0, 0, 0),
(20, 'fowler_macey@email.com', '$pbkdf2-sha256$10$VeodIwRAqLUWAsCYk/Je6w$MPGONdx7krOjmvjl7wHbMnwg2mXcvu5ZkcHcgE3fj8g', 'Macey', 'Fowler', 'Education', 'VII', 'Cebu', 'Cebu', 0, 0, 0),
(21, 'lillie_mai.drummond@email.com', '$pbkdf2-sha256$10$VwrB.N87Z0xpjVHq3RuD8A$BfsdL0TcW9bM1d1sz53r3n3eMqU3YMd6xBvnNF0r6Ls', 'Lillie', 'Drummond', 'BPO', 'VII', 'Cebu', 'Mandaue', 0, 0, 0),
(22, 'tomi.brook@email.com', '$pbkdf2-sha256$10$MKa0VirlXCultNa615oTAg$5M5OXT8QYaPZNT3nDm.32XDy.1ashtIUiyBrS5hytS4', 'Tomi', 'Brook', 'BPO', 'VII', 'Cebu', 'Mandaue', 0, 0, 0),
(23, 'jeremiah_o.quinn@email.com', '$pbkdf2-sha256$10$WSslhNC6t5ZSqtUawxiDEA$fUn3rdK/YHzO1tZjrugjNZDH8YkeDJSlxE5Qe3DfVxI', 'Jeremiah', 'Quinn', 'BPO', 'VII', 'Cebu', 'Lapu-Lapu', 0, 0, 0),
(24, 'mack_searle@email.com', '$pbkdf2-sha256$10$f29NaS0lBKCU8t7bm1MqhQ$znCodkVrFbPkT14FMqcTsoZw0a5DAEYa8qVvrtQLK2o', 'Mack', 'Searle', 'Education', 'VII', 'Cebu', 'Lapu-Lapu', 0, 0, 0),
(25, 'ebonie.hood@email.com', '$pbkdf2-sha256$10$HiPk/J.Tspaydk4pBWBsbQ$ESBg2XU/cLfL4lAcOLUtdoOca0cgCz7M.RPeSyjzZl0', 'Ebonie', 'Hood', 'Education', 'VII', 'Cebu', 'Lapu-Lapu', 0, 0, 0),
(26, 'sue_hoofman@email.com', '$pbkdf2-sha256$10$RAjhHMN4L6WUUsrZO2fsfQ$ezR8KsDNxE27e5WYMX6edxF4Sc1GYL2amwuisNsfFHs', 'Sue', 'Hoofman', 'Education', 'VII', 'Cebu', 'Cebu', 0, 0, 0),
(27, 'petty.tasneem@email.com', '$pbkdf2-sha256$10$JcS4d25NqRWi1DpnLOWcsw$oIwc/hwU/DxDoPeADZLYaOJOB4eVphqp.Gr.Hmv6K.U', 'Petty', 'Tasneem', 'Hospitality Management', 'VII', 'Cebu', 'Lapu-Lapu', 0, 0, 0),
(28, 'dawe.larissa@email.com', '$pbkdf2-sha256$10$1zpn7F1rzXkvpbR2jtE6hw$0sSlUguOM9MtUvh8v3DIcueBrzKv/06UPS/pgKFwE4k', 'Larissa', 'Dawe', 'Hospitality Management', 'VII', 'Cebu', 'Mandaue', 0, 0, 0),
(29, 'kaye_yara@email.com', '$pbkdf2-sha256$10$5Fyr1TpHyJnT2puTMgbAuA$xUZsQ99Pv4mqLRhtAIS/8HuSXSCWbABzlZPPpaKLxvg', 'Kaye', 'Yara', 'Technology', 'VII', 'Cebu', 'Cebu', 0, 0, 0),
(30, 'burt_cherish@email.com', '$pbkdf2-sha256$10$JwTg/H.PMYZQKsV4L2UMAQ$N8bSUeHvyv5604Yqxk6EdrOAlMrPbFOFJBnlanFqgpA', 'Burt', 'Cherish', 'Hospitality Management', 'VII', 'Cebu', 'Cebu', 0, 0, 0),
(31, 'jeniffer_ramsey@email.com', '$pbkdf2-sha256$10$Ykyp9d4755yzdu59j7GWEg$x5FmxW5luGbLPZ1G.xnzS0M03qMfEhQlRjSUWM0aIIQ', 'Jeniffer', 'Ramsey', 'Hospitality Management', 'VII', 'Cebu', 'Cebu', 0, 0, 0),
(32, 'arjun.lancaster@email.com', '$pbkdf2-sha256$10$Wcu51zoHQOhdi7E2hlCKsQ$rd/JHhpjF6UVxCyQPbpmI.MwTUC7sAmYFMWNbkIIJbY', 'Arjun', 'Lancaster', 'Technology', 'VII', 'Cebu', 'Mandaue', 0, 0, 0),
(33, 'kiki_wiggins@email.com', '$pbkdf2-sha256$10$KEXonbPWeu8d45xT6h1DqA$NB0r/UyWMZrIzD8CBP9QpMZCRjrolxfq1R4eYtUg6tk', 'Kiki', 'Wiggins', 'Manufacturing', 'VII', 'Cebu', 'Mandaue', 0, 0, 0),
(34, 'haigh.alys@email.com', '$pbkdf2-sha256$10$HwPAOGdMCeHcu5cSAgCgtA$a86Pu88YhNBVA91I7vf7mYiDfwjL6ojSc4R69rwM7uo', 'Alys', 'Haigh', 'Technology', 'VII', 'Cebu', 'Lapu-Lapu', 0, 0, 0),
(35, 'wynn_zack@email.com', '$pbkdf2-sha256$10$spayFmIs5TyHUCqFEOI8hw$oF4GEikpsDTUOhm915mrvwy2C/pxt6S0Ki3/5/yWxhk', 'Zack', 'Wynn', 'Technology', 'VII', 'Cebu', 'Lapu-Lapu', 0, 0, 0),
(36, 'mosley_elvis@email.com', '$pbkdf2-sha256$10$ZgwBACAkhBBCyNnb.x9DaA$MxXw9jqM2V/fVwD21BoNAJKSo66Aj/zPflAeVqJaeBM', 'Elvis', 'Mosley', 'Education', 'VII', 'Cebu', 'Lapu-Lapu', 0, 0, 0),
(37, 'mari_wade@email.com', '$pbkdf2-sha256$10$yTmHUOo9Z6zVuncupbQ2xg$cguXPCT7TRypsLMwlU4qqkZHhJeuAi5UhW3.XfTi8uM', 'Mari', 'Wade', 'Manufacturing', 'VII', 'Cebu', 'Cebu', 0, 0, 0),
(38, 'kaila.alexander@email.com', '$pbkdf2-sha256$10$OwfA.B9jjNFaq9V6D.Gcsw$HQiawtv2gVnpa/VeV9Vh63xbiM9NZ.odCbtsMMvH09M', 'Alexander', 'Kaila', 'Education', 'VII', 'Cebu', 'Mandaue', 0, 0, 0),
(39, 'heath_yusha@email.com', '$pbkdf2-sha256$10$xDhnbG0N4TzHmBPi/N87Jw$jdVuOnKqhcklKupc0G/V4tFGd7UMSEER5Zsl7UGUnfk', 'Heath', 'Yusha', 'BPO', 'VII', 'Cebu', 'Mandaue', 0, 0, 0),
(40, 'monroe.jeffrey@email.com', '$pbkdf2-sha256$10$mPNeCyGEUGothTDGuLf23g$njIuFIkyN2d.vm9M.BukqZ778n5gnSnQI32l9PLpl7Q', 'Jeffrey', 'Monroe', 'BPO', 'VII', 'Cebu', 'Mandaue', 0, 0, 0),
(41, 'elon_musk420@telsta.com', '$pbkdf2-sha256$10$Q0iJEcI4R4gxBsA4p/SeUw$WI1NqURSVmnXq8Pu1t6dGhjZw8KEuxBRMi0QbE7gk8M', 'Melon', 'Musk', 'Technology', 'VII', 'Cebu', 'Cebu', 0, 0, 1),
(42, 'zuckthemark@libra.com', '$pbkdf2-sha256$10$xniPsTbGmPOekxLCuPceYw$rBe7Ku9jPUkMeSs.8Gkuzp75vI0cSZsahnSNxrpq3Mg', 'Mark', 'Zuckerburger', 'Education', 'VII', 'Cebu', 'Lapu-Lapu', 0, 0, 1),
(43, 'jeffersonsozeb@thecongo.com', '$pbkdf2-sha256$10$dY6RslbqXcv5n5OSknJO6Q$EzrDlU4kCdFoHvGUfh5xAwEuaWoYxrfK7tJ0Mz00wqg', 'Jefferson', 'Sozeb', 'Hospitality Management', 'VII', 'Cebu', 'Mandaue', 0, 0, 1),
(44, 'mackja@alibobo@com', '$pbkdf2-sha256$10$V2rtPSckhPCeM.Z8j3HuPQ$al2tk6aH8Uo/o.dEt77PwJNli1XV6yCiL8o32aVzuz8', 'Mack', 'Ja', 'BPO', 'VII', 'Cebu', 'Cebu', 0, 0, 1),
(45, 'gillbates@doors.com', '$pbkdf2-sha256$10$BoDQWgvBWCsFIKR0zrlXSg$W2yd31IXyUWNn9oEJXdg32mnMuIGwuTdMk83zfYHBH8', 'Gill', 'Bates', 'Technology', 'VII', 'Cebu', 'Lapu-Lapu', 0, 0, 1),
(46, 'bernivillamor@ctos.com', '$pbkdf2-sha256$10$Mqa0tlaqVWpNaW0NgZCyVg$/P0k4g2qOLbB3TbGbCweU7Zpm6hjfUcJpFF972oIS20', 'Berni', 'Villamor', 'Education', 'VII', 'Cebu', 'Mandaue', 0, 0, 1),
(47, 'henrycantsee@shoemart.com', '$pbkdf2-sha256$10$ipFy7t2bkxJCSMmZ8z7HGA$gPLAifd1KeetC/Lyt0l5566WQThWoYtypBYBXGq1CZc', 'Henry', 'See', 'Hospitality Management', 'VII', 'Cebu', 'Cebu', 0, 0, 1),
(48, 'sanfrancisco@backrow.com', '$pbkdf2-sha256$10$cO79X.u99x6DcC7l/J.Tsg$IYOiZ1ES4cjqnmWLldwfUuzzwz670XS/CVJzgHl3tUw', 'San', 'Francisco', 'BPO', 'VII', 'Cebu', 'Lapu-Lapu', 0, 0, 1),
(49, 'villarsintia@subdivision.com', '$pbkdf2-sha256$10$7l3rfc957x3DOAdASCnlPA$xpCuCJDKkFmysAWZKUKdh7aZ2lA0NHSHZnd0EtORyKE', 'Sintia', 'Villar', 'BPO', 'VII', 'Cebu', 'Mandaue', 0, 0, 1),
(50, 'belledolphin@bathwater.com', '$pbkdf2-sha256$10$x/gfI2TMmVNKaa0VQogxZg$t0G/yOFxFZ.RKLbpdGlbOh2XT4hUNb66sYbXxBKNKQM', 'Belle', 'Dolphin', 'Technology', 'VII', 'Cebu', 'Cebu', 0, 0, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `applicant`
--
ALTER TABLE `applicant`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `applicantUser_id` (`applicantUser_id`),
  ADD KEY `Applicant_ratings_id_fe645b9e_fk_Rating_id` (`ratings_id`);

--
-- Indexes for table `employer`
--
ALTER TABLE `employer`
  ADD PRIMARY KEY (`employerUser_id`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Posts_applicantID_id_258a9861_fk_Applicant_id` (`applicantID_id`);

--
-- Indexes for table `rating`
--
ALTER TABLE `rating`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rating_rateremail`
--
ALTER TABLE `rating_rateremail`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Rating_raterEmail_rating_id_employer_id_21dd7319_uniq` (`rating_id`,`employer_id`),
  ADD KEY `Rating_raterEmail_employer_id_f93bf9f5_fk_Employer_` (`employer_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `applicant`
--
ALTER TABLE `applicant`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rating`
--
ALTER TABLE `rating`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `rating_rateremail`
--
ALTER TABLE `rating_rateremail`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `applicant`
--
ALTER TABLE `applicant`
  ADD CONSTRAINT `Applicant_applicantUser_id_59d35d70_fk_User_id` FOREIGN KEY (`applicantUser_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `Applicant_ratings_id_fe645b9e_fk_Rating_id` FOREIGN KEY (`ratings_id`) REFERENCES `rating` (`id`);

--
-- Constraints for table `employer`
--
ALTER TABLE `employer`
  ADD CONSTRAINT `Employer_employerUser_id_2976ecb3_fk_User_id` FOREIGN KEY (`employerUser_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `posts`
--
ALTER TABLE `posts`
  ADD CONSTRAINT `Posts_applicantID_id_258a9861_fk_Applicant_id` FOREIGN KEY (`applicantID_id`) REFERENCES `applicant` (`id`);

--
-- Constraints for table `rating_rateremail`
--
ALTER TABLE `rating_rateremail`
  ADD CONSTRAINT `Rating_raterEmail_employer_id_f93bf9f5_fk_Employer_` FOREIGN KEY (`employer_id`) REFERENCES `employer` (`employerUser_id`),
  ADD CONSTRAINT `Rating_raterEmail_rating_id_f174f84e_fk_Rating_id` FOREIGN KEY (`rating_id`) REFERENCES `rating` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
